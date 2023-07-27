
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")

# - İki takımın tekli maç ist. birleştir -
def combineTeamGames(IDs):
    full_games = pd.DataFrame()
    for id in IDs:
        matchingGames = all_games[all_games.GAME_ID == id]
        if(matchingGames.empty):
            continue
        matchingGames = matchingGames[matchingGames['WL'].notnull()]
        matchupStr = matchingGames.iloc[0].MATCHUP
        if (' vs. ' in matchupStr):
            matchingGames["HOME"] = [0,1]
        else:
            matchingGames["HOME"] = [1,0]
        full_games = pd.concat((full_games, matchingGames))
        
    joined = pd.merge(full_games, full_games, suffixes=['_A', '_B'], on=[
                      'SEASON_ID', 'GAME_ID', 'GAME_DATE'])
    
    # KENDİYLE EŞLEŞEN SATIRLARI ÇIKAR
    result = joined[joined.TEAM_ID_A != joined.TEAM_ID_B]


    return result


# - Takım kısaltmasını bulmak için-
def getTeamAbbr(teamId):
    for team in nba_teams:
        if team['id'] == teamId:
            myStr = ''.join(team['abbreviation'])
            return myStr

# - Sadece bir takımın maçları ve ist-
def searchForTeamGames(teamId):
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamId)
    games = gamefinder.get_data_frames()[0]
    allGames = pd.DataFrame()
    for year in range(prevSeason, season+1):
        games_givenSeason = games[games.SEASON_ID.str[-4:] == str(year)]
        allGames = pd.concat((allGames, games_givenSeason))
    return allGames


# - İki takımın birbirine karşı maçları ve ist-
def searchTeamAgainstTeam(homeTeamId, awayTeamId):
    homeTeamGames = searchForTeamGames(homeTeamId)
    awayTeamAbbr = getTeamAbbr(awayTeamId)
    homeVersusAway = homeTeamGames[homeTeamGames.MATCHUP.str.contains(awayTeamAbbr)]
    homeVersusAwayGameIDs = homeVersusAway.GAME_ID.values
    homeVersusAway = combineTeamGames(homeVersusAwayGameIDs)
    return homeVersusAway.sort_values('GAME_DATE')




#----------------------------#
season = 2023
prevSeason = 2017  # Hangi sezondan hangi sezonanın ilki


# Oynan tüm maçlar
for i in range(1,5):
    time.sleep(5*i)
    try:
        result = leaguegamefinder.LeagueGameFinder()
        all_games = result.get_data_frames()[0]
        nba_teams = teams.get_teams()
    except TimeoutError:
        print("Tüm maçları alırken timeout hatası")
        continue
    else:
        break



final_df = pd.DataFrame()
for i in range(0, len(nba_teams)):
    print(f"{i} / {len(nba_teams) - 1}")
    temp_df = pd.DataFrame()
    for j in range(i + 1, len(nba_teams)):
        temp_df = searchTeamAgainstTeam(nba_teams[i]["id"], nba_teams[j]["id"])
        final_df = pd.concat((final_df, temp_df))
final_df.to_csv(f'NBAGamesBetween{prevSeason}-{season}.csv', index=False)

