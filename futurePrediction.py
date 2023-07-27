import pickle
import pandas as pd
import random as rnd 
import numpy as np
from sklearn.preprocessing import MinMaxScaler

with open("model_pkl", 'rb') as f:
    model = pickle.load(f)

df = pd.read_csv("NBAGamesBetween2017-2023.csv")

columns = ['PTS_A','FGM_A', 'FG_PCT_A','FG3M_A', 'FTM_A', 'FTA_A', 'FT_PCT_A', 'OREB_A', 'DREB_A', 'REB_A', 'AST_A', 'STL_A', 'BLK_A', 'TOV_A', 'HOME_A', 'PTS_B', 'FG_PCT_B', 'FG3M_B', 'FG3A_B', 'FG3_PCT_B',
 'FT_PCT_B', 'OREB_B', 'DREB_B', 'REB_B', 'AST_B', 'STL_B', 'BLK_B', 'TOV_B', 'PF_B', 'HOME_B']

# teamAbbs = ['BOS', 'ATL', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU',
#        'LAC', 'LAL', 'MIA', 'MIL', 'MIN', 'BKN', 'NYK', 'ORL', 'IND',
#        'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'OKC', 'TOR', 'UTA', 'MEM',
#        'WAS', 'DET', 'CHA']

teamA = None
teamB = None
teamALast = None
teamBLast = None
global teamA_PTS_Mean ,teamA_PTS_STD ,teamA_OPP_PTS_MEAN , teamA_OPP_PTS_STD, teamB_PTS_Mean, teamB_PTS_STD, teamB_OPP_PTS_MEAN, teamB_OPP_PTS_STD, teamA_FGM_Mean, teamA_FGM_STD, teamA_OPP_FGM_MEAN, teamA_OPP_FGM_STD, teamB_FGM_Mean,teamB_FGM_STD, teamB_OPP_FGM_MEAN, teamB_OPP_FGM_STD, teamA_FGPCT_Mean, teamA_FGPCT_STD, teamA_OPP_FGPCT_MEAN, teamA_OPP_FGPCT_STD, teamB_FGPCT_Mean, teamB_FGPCT_STD, teamB_OPP_FGPCT_MEAN, teamB_OPP_FGPCT_STD, teamA_FG3M_Mean,teamA_FG3M_STD, teamA_OPP_FG3M_MEAN, teamA_OPP_FG3M_STD, teamB_FG3M_Mean, teamB_FG3M_STD, teamB_OPP_FG3M_MEAN, teamB_OPP_FG3M_STD, teamA_FTM_Mean, teamA_FTM_STD, teamA_OPP_FTM_MEAN, teamA_OPP_FTM_STD, teamB_FTM_Mean,teamB_FTM_STD,teamB_OPP_FTM_MEAN,teamB_OPP_FTM_STD,teamA_FTA_Mean,teamA_FTA_STD,teamA_OPP_FTA_MEAN,teamA_OPP_FTA_STD,teamB_FTA_Mean,teamB_FTA_STD,teamB_OPP_FTA_MEAN,teamB_OPP_FTA_STD,teamA_FTPCT_Mean,teamA_FTPCT_STD,teamA_OPP_FTPCT_MEAN,teamA_OPP_FTPCT_STD,teamB_FTPCT_Mean,teamB_FTPCT_STD,teamB_OPP_FTPCT_MEAN,teamB_OPP_FTPCT_STD,teamA_OREB_Mean,teamA_OREB_STD,teamA_OPP_OREB_MEAN,teamA_OPP_OREB_STD,teamB_OREB_Mean,teamB_OREB_STD,teamB_OPP_OREB_MEAN,teamB_OPP_OREB_STD,teamA_DREB_Mean,teamA_DREB_STD,teamA_OPP_DREB_MEAN,teamA_OPP_DREB_STD,teamB_DREB_Mean,teamB_DREB_STD,teamB_OPP_DREB_MEAN,teamB_OPP_DREB_STD,teamA_REB_Mean,teamA_REB_STD,teamA_OPP_REB_MEAN,teamA_OPP_REB_STD,teamB_REB_Mean,teamB_REB_STD,teamB_OPP_REB_MEAN,teamB_OPP_REB_STD,teamA_AST_Mean,teamA_AST_STD,teamA_OPP_AST_MEAN,teamA_OPP_AST_STD,teamB_AST_Mean,teamB_AST_STD,teamB_OPP_AST_MEAN,teamB_OPP_AST_STD,teamA_STL_Mean,teamA_STL_STD,teamA_OPP_STL_MEAN,teamA_OPP_STL_STD,teamB_STL_Mean,teamB_STL_STD,teamB_OPP_STL_MEAN,teamB_OPP_STL_STD,teamA_BLK_Mean,teamA_BLK_STD,teamA_OPP_BLK_MEAN,teamA_OPP_BLK_STD,teamB_BLK_Mean,teamB_BLK_STD,teamB_OPP_BLK_MEAN,teamB_OPP_BLK_STD,teamA_TOV_Mean,teamA_TOV_STD,teamA_OPP_TOV_MEAN,teamA_OPP_TOV_STD,teamB_TOV_Mean,teamB_TOV_STD,teamB_OPP_TOV_MEAN,teamB_OPP_TOV_STD,teamA_FG3A_Mean,teamA_FG3A_STD,teamA_OPP_FG3A_MEAN,teamA_OPP_FG3A_STD,teamB_FG3A_Mean,teamB_FG3A_STD,teamB_OPP_FG3A_MEAN,teamB_OPP_FG3A_STD,teamA_FG3PCT_Mean,teamA_FG3PCT_STD,teamA_OPP_FG3PCT_MEAN,teamA_OPP_FG3PCT_STD,teamB_FG3PCT_Mean,teamB_FG3PCT_STD,teamB_OPP_FG3PCT_MEAN,teamB_OPP_FG3PCT_STD,teamA_PF_Mean,teamA_PF_STD,teamA_OPP_PF_MEAN,teamA_OPP_PF_STD,teamB_PF_Mean,teamB_PF_STD,teamB_OPP_PF_MEAN,teamB_OPP_PF_STD,teamA_PF_Mean,teamA_PF_STD,teamA_OPP_PF_MEAN,teamA_OPP_PF_STD
    
    
def calcGauss():
    global teamA_PTS_Mean ,teamA_PTS_STD ,teamA_OPP_PTS_MEAN , teamA_OPP_PTS_STD, teamB_PTS_Mean, teamB_PTS_STD, teamB_OPP_PTS_MEAN, teamB_OPP_PTS_STD, teamA_FGM_Mean, teamA_FGM_STD, teamA_OPP_FGM_MEAN, teamA_OPP_FGM_STD, teamB_FGM_Mean,teamB_FGM_STD, teamB_OPP_FGM_MEAN, teamB_OPP_FGM_STD, teamA_FGPCT_Mean, teamA_FGPCT_STD, teamA_OPP_FGPCT_MEAN, teamA_OPP_FGPCT_STD, teamB_FGPCT_Mean, teamB_FGPCT_STD, teamB_OPP_FGPCT_MEAN, teamB_OPP_FGPCT_STD, teamA_FG3M_Mean,teamA_FG3M_STD, teamA_OPP_FG3M_MEAN, teamA_OPP_FG3M_STD, teamB_FG3M_Mean, teamB_FG3M_STD, teamB_OPP_FG3M_MEAN, teamB_OPP_FG3M_STD, teamA_FTM_Mean, teamA_FTM_STD, teamA_OPP_FTM_MEAN, teamA_OPP_FTM_STD, teamB_FTM_Mean,teamB_FTM_STD,teamB_OPP_FTM_MEAN,teamB_OPP_FTM_STD,teamA_FTA_Mean,teamA_FTA_STD,teamA_OPP_FTA_MEAN,teamA_OPP_FTA_STD,teamB_FTA_Mean,teamB_FTA_STD,teamB_OPP_FTA_MEAN,teamB_OPP_FTA_STD,teamA_FTPCT_Mean,teamA_FTPCT_STD,teamA_OPP_FTPCT_MEAN,teamA_OPP_FTPCT_STD,teamB_FTPCT_Mean,teamB_FTPCT_STD,teamB_OPP_FTPCT_MEAN,teamB_OPP_FTPCT_STD,teamA_OREB_Mean,teamA_OREB_STD,teamA_OPP_OREB_MEAN,teamA_OPP_OREB_STD,teamB_OREB_Mean,teamB_OREB_STD,teamB_OPP_OREB_MEAN,teamB_OPP_OREB_STD,teamA_DREB_Mean,teamA_DREB_STD,teamA_OPP_DREB_MEAN,teamA_OPP_DREB_STD,teamB_DREB_Mean,teamB_DREB_STD,teamB_OPP_DREB_MEAN,teamB_OPP_DREB_STD,teamA_REB_Mean,teamA_REB_STD,teamA_OPP_REB_MEAN,teamA_OPP_REB_STD,teamB_REB_Mean,teamB_REB_STD,teamB_OPP_REB_MEAN,teamB_OPP_REB_STD,teamA_AST_Mean,teamA_AST_STD,teamA_OPP_AST_MEAN,teamA_OPP_AST_STD,teamB_AST_Mean,teamB_AST_STD,teamB_OPP_AST_MEAN,teamB_OPP_AST_STD,teamA_STL_Mean,teamA_STL_STD,teamA_OPP_STL_MEAN,teamA_OPP_STL_STD,teamB_STL_Mean,teamB_STL_STD,teamB_OPP_STL_MEAN,teamB_OPP_STL_STD,teamA_BLK_Mean,teamA_BLK_STD,teamA_OPP_BLK_MEAN,teamA_OPP_BLK_STD,teamB_BLK_Mean,teamB_BLK_STD,teamB_OPP_BLK_MEAN,teamB_OPP_BLK_STD,teamA_TOV_Mean,teamA_TOV_STD,teamA_OPP_TOV_MEAN,teamA_OPP_TOV_STD,teamB_TOV_Mean,teamB_TOV_STD,teamB_OPP_TOV_MEAN,teamB_OPP_TOV_STD,teamA_FG3A_Mean,teamA_FG3A_STD,teamA_OPP_FG3A_MEAN,teamA_OPP_FG3A_STD,teamB_FG3A_Mean,teamB_FG3A_STD,teamB_OPP_FG3A_MEAN,teamB_OPP_FG3A_STD,teamA_FG3PCT_Mean,teamA_FG3PCT_STD,teamA_OPP_FG3PCT_MEAN,teamA_OPP_FG3PCT_STD,teamB_FG3PCT_Mean,teamB_FG3PCT_STD,teamB_OPP_FG3PCT_MEAN,teamB_OPP_FG3PCT_STD,teamA_PF_Mean,teamA_PF_STD,teamA_OPP_PF_MEAN,teamA_OPP_PF_STD,teamB_PF_Mean,teamB_PF_STD,teamB_OPP_PF_MEAN,teamB_OPP_PF_STD,teamA_PF_Mean,teamA_PF_STD,teamA_OPP_PF_MEAN,teamA_OPP_PF_STD

    teamA_PTS = (rnd.gauss(teamA_PTS_Mean, teamA_PTS_STD) + rnd.gauss(teamB_OPP_PTS_MEAN, teamB_OPP_PTS_STD))/2
    teamA_FGM = (rnd.gauss(teamA_FGM_Mean, teamA_FGM_STD) + rnd.gauss(teamB_OPP_FGM_MEAN, teamB_OPP_FGM_STD))/2
    teamA_FGPCT = (rnd.gauss(teamA_FGPCT_Mean, teamA_FGPCT_STD) + rnd.gauss(teamB_OPP_FGPCT_MEAN, teamB_OPP_FGPCT_STD))/2
    teamA_FG3M = (rnd.gauss(teamA_FG3M_Mean, teamA_FG3M_STD) + rnd.gauss(teamB_OPP_FG3M_MEAN, teamB_OPP_FG3M_STD))/2
    teamA_FTM = (rnd.gauss(teamA_FTM_Mean, teamA_FTM_STD) + rnd.gauss(teamB_OPP_FTM_MEAN, teamB_OPP_FTM_STD))/2
    teamA_FTA = (rnd.gauss(teamA_FTA_Mean, teamA_FTA_STD) + rnd.gauss(teamB_OPP_FTA_MEAN, teamB_OPP_FTA_STD))/2
    teamA_FTPCT = (rnd.gauss(teamA_FTPCT_Mean, teamA_FTPCT_STD) + rnd.gauss(teamB_OPP_FTPCT_MEAN, teamB_OPP_FTPCT_STD))/2
    teamA_OREB = (rnd.gauss(teamA_OREB_Mean, teamA_OREB_STD) + rnd.gauss(teamB_OPP_OREB_MEAN, teamB_OPP_OREB_STD))/2
    teamA_DREB = (rnd.gauss(teamA_DREB_Mean, teamA_DREB_STD) + rnd.gauss(teamB_OPP_DREB_MEAN, teamB_OPP_DREB_STD))/2
    teamA_REB = (rnd.gauss(teamA_REB_Mean, teamA_REB_STD) + rnd.gauss(teamB_OPP_REB_MEAN, teamB_OPP_REB_STD))/2
    teamA_AST = (rnd.gauss(teamA_AST_Mean, teamA_AST_STD) + rnd.gauss(teamB_OPP_AST_MEAN, teamB_OPP_AST_STD))/2
    teamA_STL = (rnd.gauss(teamA_STL_Mean, teamA_STL_STD) + rnd.gauss(teamB_OPP_STL_MEAN, teamB_OPP_STL_STD))/2
    teamA_BLK = (rnd.gauss(teamA_BLK_Mean, teamA_BLK_STD) + rnd.gauss(teamB_OPP_BLK_MEAN, teamB_OPP_BLK_STD))/2
    teamA_TOV = (rnd.gauss(teamA_TOV_Mean, teamA_TOV_STD) + rnd.gauss(teamB_OPP_TOV_MEAN, teamB_OPP_TOV_STD))/2
    teamA_HOME = 0

    teamB_PTS = (rnd.gauss(teamB_PTS_Mean, teamB_PTS_STD) + rnd.gauss(teamA_OPP_PTS_MEAN, teamA_OPP_PTS_STD))/2
    teamB_FGPCT = (rnd.gauss(teamB_FGPCT_Mean, teamB_FGPCT_STD) + rnd.gauss(teamA_OPP_FGPCT_MEAN, teamA_OPP_FGPCT_STD))/2
    teamB_FG3M = (rnd.gauss(teamB_FG3M_Mean, teamB_FG3M_STD) + rnd.gauss(teamA_OPP_FG3M_MEAN, teamA_OPP_FG3M_STD))/2
    teamB_FG3A = (rnd.gauss(teamB_FG3A_Mean, teamB_FG3A_STD) + rnd.gauss(teamA_OPP_FG3A_MEAN, teamA_OPP_FG3A_STD))/2
    teamB_FG3PCT = (rnd.gauss(teamB_FG3PCT_Mean, teamB_FG3PCT_STD) + rnd.gauss(teamA_OPP_FG3PCT_MEAN, teamA_OPP_FG3PCT_STD))/2
    teamB_FTPCT = (rnd.gauss(teamB_FTPCT_Mean, teamB_FTPCT_STD) + rnd.gauss(teamA_OPP_FTPCT_MEAN, teamA_OPP_FTPCT_STD))/2
    teamB_OREB = (rnd.gauss(teamB_OREB_Mean, teamB_OREB_STD) + rnd.gauss(teamA_OPP_OREB_MEAN, teamA_OPP_OREB_STD))/2
    teamB_DREB = (rnd.gauss(teamB_DREB_Mean, teamB_DREB_STD) + rnd.gauss(teamA_OPP_DREB_MEAN, teamA_OPP_DREB_STD))/2
    teamB_REB = (rnd.gauss(teamB_REB_Mean, teamB_REB_STD) + rnd.gauss(teamA_OPP_REB_MEAN, teamA_OPP_REB_STD))/2
    teamB_AST = (rnd.gauss(teamB_AST_Mean, teamB_AST_STD) + rnd.gauss(teamA_OPP_AST_MEAN, teamA_OPP_AST_STD))/2
    teamB_STL = (rnd.gauss(teamB_STL_Mean, teamB_STL_STD) + rnd.gauss(teamA_OPP_STL_MEAN, teamA_OPP_STL_STD))/2
    teamB_BLK = (rnd.gauss(teamB_BLK_Mean, teamB_BLK_STD) + rnd.gauss(teamA_OPP_BLK_MEAN, teamA_OPP_BLK_STD))/2
    teamB_TOV = (rnd.gauss(teamB_TOV_Mean, teamB_TOV_STD) + rnd.gauss(teamA_OPP_TOV_MEAN, teamA_OPP_TOV_STD))/2
    teamB_PF = (rnd.gauss(teamB_PF_Mean, teamB_PF_STD) + rnd.gauss(teamA_OPP_PF_MEAN, teamA_OPP_PF_STD))/2
    teamB_HOME = 1
    return [teamA_PTS,teamA_FGM,teamA_FGPCT,teamA_FG3M,teamA_FTM,teamA_FTA,teamA_FTPCT,teamA_OREB,teamA_DREB,teamA_REB,teamA_AST,teamA_STL,teamA_BLK,teamA_TOV,teamA_HOME,teamB_PTS,teamB_FGPCT,teamB_FG3M,teamB_FG3A,teamB_FG3PCT,teamB_FTPCT,teamB_OREB,teamB_DREB,teamB_REB,teamB_AST,teamB_STL,teamB_BLK,teamB_TOV,teamB_PF,teamB_HOME]
    

def gameSim():
    scaler = MinMaxScaler()
    stats = calcGauss()
    columns = ['PTS_A','FGM_A','FGA_A','FG_PCT_A','FG3M_A','FG3A_A','FG3_PCT_A','FTM_A','FTA_A','FT_PCT_A','DREB_A','REB_A','AST_A','STL_A','BLK_A','HOME_A','FGM_B','FGA_B','FG_PCT_B','FG3M_B','FG3A_B','FG3_PCT_B','FT_PCT_B','REB_B',
    'AST_B','STL_B','BLK_B','TOV_B','PF_B','HOME_B']

    stats = np.array(stats)
    stats_transformed = scaler.fit_transform(stats[:, np.newaxis])
    stats_reshape  = stats_transformed.reshape(1,30)

    dfToPredict = pd.DataFrame(data=stats_reshape, columns=columns)

    return model.predict(dfToPredict)
    
def simulateGames(n, teamA_Abbr, teamB_Abbr):
    global teamA,teamB,teamALast,teamBLast
    global teamA_PTS_Mean ,teamA_PTS_STD ,teamA_OPP_PTS_MEAN , teamA_OPP_PTS_STD, teamB_PTS_Mean, teamB_PTS_STD, teamB_OPP_PTS_MEAN, teamB_OPP_PTS_STD, teamA_FGM_Mean, teamA_FGM_STD, teamA_OPP_FGM_MEAN, teamA_OPP_FGM_STD, teamB_FGM_Mean,teamB_FGM_STD, teamB_OPP_FGM_MEAN, teamB_OPP_FGM_STD, teamA_FGPCT_Mean, teamA_FGPCT_STD, teamA_OPP_FGPCT_MEAN, teamA_OPP_FGPCT_STD, teamB_FGPCT_Mean, teamB_FGPCT_STD, teamB_OPP_FGPCT_MEAN, teamB_OPP_FGPCT_STD, teamA_FG3M_Mean,teamA_FG3M_STD, teamA_OPP_FG3M_MEAN, teamA_OPP_FG3M_STD, teamB_FG3M_Mean, teamB_FG3M_STD, teamB_OPP_FG3M_MEAN, teamB_OPP_FG3M_STD, teamA_FTM_Mean, teamA_FTM_STD, teamA_OPP_FTM_MEAN, teamA_OPP_FTM_STD, teamB_FTM_Mean,teamB_FTM_STD,teamB_OPP_FTM_MEAN,teamB_OPP_FTM_STD,teamA_FTA_Mean,teamA_FTA_STD,teamA_OPP_FTA_MEAN,teamA_OPP_FTA_STD,teamB_FTA_Mean,teamB_FTA_STD,teamB_OPP_FTA_MEAN,teamB_OPP_FTA_STD,teamA_FTPCT_Mean,teamA_FTPCT_STD,teamA_OPP_FTPCT_MEAN,teamA_OPP_FTPCT_STD,teamB_FTPCT_Mean,teamB_FTPCT_STD,teamB_OPP_FTPCT_MEAN,teamB_OPP_FTPCT_STD,teamA_OREB_Mean,teamA_OREB_STD,teamA_OPP_OREB_MEAN,teamA_OPP_OREB_STD,teamB_OREB_Mean,teamB_OREB_STD,teamB_OPP_OREB_MEAN,teamB_OPP_OREB_STD,teamA_DREB_Mean,teamA_DREB_STD,teamA_OPP_DREB_MEAN,teamA_OPP_DREB_STD,teamB_DREB_Mean,teamB_DREB_STD,teamB_OPP_DREB_MEAN,teamB_OPP_DREB_STD,teamA_REB_Mean,teamA_REB_STD,teamA_OPP_REB_MEAN,teamA_OPP_REB_STD,teamB_REB_Mean,teamB_REB_STD,teamB_OPP_REB_MEAN,teamB_OPP_REB_STD,teamA_AST_Mean,teamA_AST_STD,teamA_OPP_AST_MEAN,teamA_OPP_AST_STD,teamB_AST_Mean,teamB_AST_STD,teamB_OPP_AST_MEAN,teamB_OPP_AST_STD,teamA_STL_Mean,teamA_STL_STD,teamA_OPP_STL_MEAN,teamA_OPP_STL_STD,teamB_STL_Mean,teamB_STL_STD,teamB_OPP_STL_MEAN,teamB_OPP_STL_STD,teamA_BLK_Mean,teamA_BLK_STD,teamA_OPP_BLK_MEAN,teamA_OPP_BLK_STD,teamB_BLK_Mean,teamB_BLK_STD,teamB_OPP_BLK_MEAN,teamB_OPP_BLK_STD,teamA_TOV_Mean,teamA_TOV_STD,teamA_OPP_TOV_MEAN,teamA_OPP_TOV_STD,teamB_TOV_Mean,teamB_TOV_STD,teamB_OPP_TOV_MEAN,teamB_OPP_TOV_STD,teamA_FG3A_Mean,teamA_FG3A_STD,teamA_OPP_FG3A_MEAN,teamA_OPP_FG3A_STD,teamB_FG3A_Mean,teamB_FG3A_STD,teamB_OPP_FG3A_MEAN,teamB_OPP_FG3A_STD,teamA_FG3PCT_Mean,teamA_FG3PCT_STD,teamA_OPP_FG3PCT_MEAN,teamA_OPP_FG3PCT_STD,teamB_FG3PCT_Mean,teamB_FG3PCT_STD,teamB_OPP_FG3PCT_MEAN,teamB_OPP_FG3PCT_STD,teamA_PF_Mean,teamA_PF_STD,teamA_OPP_PF_MEAN,teamA_OPP_PF_STD,teamB_PF_Mean,teamB_PF_STD,teamB_OPP_PF_MEAN,teamB_OPP_PF_STD,teamA_PF_Mean,teamA_PF_STD,teamA_OPP_PF_MEAN,teamA_OPP_PF_STD

    teamA = df[df["TEAM_ABBREVIATION_A"] == teamA_Abbr]
    teamB = df[df["TEAM_ABBREVIATION_A"] == teamB_Abbr]

    teamA = teamA.sort_values("GAME_DATE", ascending=False)
    teamALast = teamA.head(5).copy()
    teamB = teamB.sort_values("GAME_DATE", ascending=False)
    teamBLast = teamB.head(5).copy()
    
    # Gauss Dağılım için gerekli olan değerler
    #PTS - A için
    teamA_PTS_Mean = teamALast.PTS_A.mean()
    teamA_PTS_STD = teamALast.PTS_A.std()
    teamA_OPP_PTS_MEAN = teamALast.PTS_B.mean()
    teamA_OPP_PTS_STD = teamALast.PTS_B.std()

    #PTS - B için
    teamB_PTS_Mean = teamBLast.PTS_A.mean() #teamB tablosunun team a takımına bakıyoruz. Değişken ismimimiz teamb olsada df de team_a olarak kayıtlı
    teamB_PTS_STD = teamBLast.PTS_A.std()
    teamB_OPP_PTS_MEAN = teamBLast.PTS_B.mean()
    teamB_OPP_PTS_STD = teamBLast.PTS_B.std()


    #FGM - A için
    teamA_FGM_Mean = teamALast.FGM_A.mean()
    teamA_FGM_STD = teamALast.FGM_A.std()
    teamA_OPP_FGM_MEAN = teamALast.FGM_B.mean()
    teamA_OPP_FGM_STD = teamALast.FGM_B.std()

    #FGM - B için 
    teamB_FGM_Mean = teamBLast.FGM_A.mean() 
    teamB_FGM_STD = teamBLast.FGM_A.std()
    teamB_OPP_FGM_MEAN = teamBLast.FGM_B.mean()
    teamB_OPP_FGM_STD = teamBLast.FGM_B.std()

    #FG_PCT - A İçin
    teamA_FGPCT_Mean = teamALast.FG_PCT_A.mean()
    teamA_FGPCT_STD = teamALast.FG_PCT_A.std()
    teamA_OPP_FGPCT_MEAN = teamALast.FG_PCT_B.mean()
    teamA_OPP_FGPCT_STD = teamALast.FG_PCT_B.std()

    #FG_PCT - B için 
    teamB_FGPCT_Mean = teamBLast.FG_PCT_A.mean()
    teamB_FGPCT_STD = teamBLast.FG_PCT_A.std()
    teamB_OPP_FGPCT_MEAN = teamBLast.FG_PCT_B.mean()
    teamB_OPP_FGPCT_STD = teamBLast.FG_PCT_B.std()

    #FG3M - A İçin
    teamA_FG3M_Mean = teamALast.FG3M_A.mean()
    teamA_FG3M_STD = teamALast.FG3M_A.std()
    teamA_OPP_FG3M_MEAN = teamALast.FG3M_B.mean()
    teamA_OPP_FG3M_STD = teamALast.FG3M_B.std()

    #FG3M - B için 
    teamB_FG3M_Mean = teamBLast.FG3M_A.mean() 
    teamB_FG3M_STD = teamBLast.FG3M_A.std()
    teamB_OPP_FG3M_MEAN = teamBLast.FG3M_B.mean()
    teamB_OPP_FG3M_STD = teamBLast.FG3M_B.std()

    #FTM - A İçin
    teamA_FTM_Mean = teamALast.FTM_A.mean()
    teamA_FTM_STD = teamALast.FTM_A.std()
    teamA_OPP_FTM_MEAN = teamALast.FTM_B.mean()
    teamA_OPP_FTM_STD = teamALast.FTM_B.std()

    #FTM - B için 
    teamB_FTM_Mean = teamBLast.FTM_A.mean()
    teamB_FTM_STD = teamBLast.FTM_A.std()
    teamB_OPP_FTM_MEAN = teamBLast.FTM_B.mean()
    teamB_OPP_FTM_STD = teamBLast.FTM_B.std()

    #FTA - A İçin
    teamA_FTA_Mean = teamALast.FTA_A.mean()
    teamA_FTA_STD = teamALast.FTA_A.std()
    teamA_OPP_FTA_MEAN = teamALast.FTA_B.mean()
    teamA_OPP_FTA_STD = teamALast.FTA_B.std()

    #FTA - B için 
    teamB_FTA_Mean = teamBLast.FTA_A.mean()
    teamB_FTA_STD = teamBLast.FTA_A.std()
    teamB_OPP_FTA_MEAN = teamBLast.FTA_B.mean()
    teamB_OPP_FTA_STD = teamBLast.FTA_B.std()

    #FT_PCT - A İçin
    teamA_FTPCT_Mean = teamALast.FT_PCT_A.mean()
    teamA_FTPCT_STD = teamALast.FT_PCT_A.std()
    teamA_OPP_FTPCT_MEAN = teamALast.FT_PCT_B.mean()
    teamA_OPP_FTPCT_STD = teamALast.FT_PCT_B.std()

    #FT_PCT - B için 
    teamB_FTPCT_Mean = teamBLast.FT_PCT_A.mean() 
    teamB_FTPCT_STD = teamBLast.FT_PCT_A.std()
    teamB_OPP_FTPCT_MEAN = teamBLast.FT_PCT_B.mean()
    teamB_OPP_FTPCT_STD = teamBLast.FT_PCT_B.std()

    #OREB - A İçin
    teamA_OREB_Mean = teamALast.OREB_A.mean()
    teamA_OREB_STD = teamALast.OREB_A.std()
    teamA_OPP_OREB_MEAN = teamALast.OREB_B.mean()
    teamA_OPP_OREB_STD = teamALast.OREB_B.std()

    #OREB - B için 
    teamB_OREB_Mean = teamBLast.OREB_A.mean() 
    teamB_OREB_STD = teamBLast.OREB_A.std()
    teamB_OPP_OREB_MEAN = teamBLast.OREB_B.mean()
    teamB_OPP_OREB_STD = teamBLast.OREB_B.std()

    #DREB - A İçin
    teamA_DREB_Mean = teamALast.DREB_A.mean()
    teamA_DREB_STD = teamALast.DREB_A.std()
    teamA_OPP_DREB_MEAN = teamALast.DREB_B.mean()
    teamA_OPP_DREB_STD = teamALast.DREB_B.std()

    #DREB - B için 
    teamB_DREB_Mean = teamBLast.DREB_A.mean() 
    teamB_DREB_STD = teamBLast.DREB_A.std()
    teamB_OPP_DREB_MEAN = teamBLast.DREB_B.mean()
    teamB_OPP_DREB_STD = teamBLast.DREB_B.std()

    #REB - A İçin
    teamA_REB_Mean = teamALast.REB_A.mean()
    teamA_REB_STD = teamALast.REB_A.std()
    teamA_OPP_REB_MEAN = teamALast.REB_B.mean()
    teamA_OPP_REB_STD = teamALast.REB_B.std()

    #REB - B için 
    teamB_REB_Mean = teamBLast.REB_A.mean() 
    teamB_REB_STD = teamBLast.REB_A.std()
    teamB_OPP_REB_MEAN = teamBLast.REB_B.mean()
    teamB_OPP_REB_STD = teamBLast.REB_B.std()

    #AST - A İçin
    teamA_AST_Mean = teamALast.AST_A.mean()
    teamA_AST_STD = teamALast.AST_A.std()
    teamA_OPP_AST_MEAN = teamALast.AST_B.mean()
    teamA_OPP_AST_STD = teamALast.AST_B.std()

    #AST - B için 
    teamB_AST_Mean = teamBLast.AST_A.mean() 
    teamB_AST_STD = teamBLast.AST_A.std()
    teamB_OPP_AST_MEAN = teamBLast.AST_B.mean()
    teamB_OPP_AST_STD = teamBLast.AST_B.std()

    #STL - A İçin
    teamA_STL_Mean = teamALast.STL_A.mean()
    teamA_STL_STD = teamALast.STL_A.std()
    teamA_OPP_STL_MEAN = teamALast.STL_B.mean()
    teamA_OPP_STL_STD = teamALast.STL_B.std()

    #STL - B için 
    teamB_STL_Mean = teamBLast.STL_A.mean()
    teamB_STL_STD = teamBLast.STL_A.std()
    teamB_OPP_STL_MEAN = teamBLast.STL_B.mean()
    teamB_OPP_STL_STD = teamBLast.STL_B.std()

    #BLK - A İçin
    teamA_BLK_Mean = teamALast.BLK_A.mean()
    teamA_BLK_STD = teamALast.BLK_A.std()
    teamA_OPP_BLK_MEAN = teamALast.BLK_B.mean()
    teamA_OPP_BLK_STD = teamALast.BLK_B.std()

    #BLK - B için 
    teamB_BLK_Mean = teamBLast.BLK_A.mean()
    teamB_BLK_STD = teamBLast.BLK_A.std()
    teamB_OPP_BLK_MEAN = teamBLast.BLK_B.mean()
    teamB_OPP_BLK_STD = teamBLast.BLK_B.std()

    #TOV - A İçin
    teamA_TOV_Mean = teamALast.TOV_A.mean()
    teamA_TOV_STD = teamALast.TOV_A.std()
    teamA_OPP_TOV_MEAN = teamALast.TOV_B.mean()
    teamA_OPP_TOV_STD = teamALast.TOV_B.std()

    #TOV - B için 
    teamB_TOV_Mean = teamBLast.TOV_A.mean() 
    teamB_TOV_STD = teamBLast.TOV_A.std()
    teamB_OPP_TOV_MEAN = teamBLast.TOV_B.mean()
    teamB_OPP_TOV_STD = teamBLast.TOV_B.std()

    #FG3A - A İçin
    teamA_FG3A_Mean = teamALast.FG3A_A.mean()
    teamA_FG3A_STD = teamALast.FG3A_A.std()
    teamA_OPP_FG3A_MEAN = teamALast.FG3A_B.mean()
    teamA_OPP_FG3A_STD = teamALast.FG3A_B.std()

    #FG3A - B için 
    teamB_FG3A_Mean = teamBLast.FG3A_A.mean()
    teamB_FG3A_STD = teamBLast.FG3A_A.std()
    teamB_OPP_FG3A_MEAN = teamBLast.FG3A_B.mean()
    teamB_OPP_FG3A_STD = teamBLast.FG3A_B.std()

    #FG3_PCT - A İçin
    teamA_FG3PCT_Mean = teamALast.FG3_PCT_A.mean()
    teamA_FG3PCT_STD = teamALast.FG3_PCT_A.std()
    teamA_OPP_FG3PCT_MEAN = teamALast.FG3_PCT_B.mean()
    teamA_OPP_FG3PCT_STD = teamALast.FG3_PCT_B.std()

    #FG3_PCT - B için 
    teamB_FG3PCT_Mean = teamBLast.FG3_PCT_A.mean() 
    teamB_FG3PCT_STD = teamBLast.FG3_PCT_A.std()
    teamB_OPP_FG3PCT_MEAN = teamBLast.FG3_PCT_B.mean()
    teamB_OPP_FG3PCT_STD = teamBLast.FG3_PCT_B.std()

    #PF - A İçin
    teamA_PF_Mean = teamALast.PF_A.mean()
    teamA_PF_STD = teamALast.PF_A.std()
    teamA_OPP_PF_MEAN = teamALast.PF_B.mean()
    teamA_OPP_PF_STD = teamALast.PF_B.std()

    #PF - B için 
    teamB_PF_Mean = teamBLast.PF_A.mean() 
    teamB_PF_STD = teamBLast.PF_A.std()
    teamB_OPP_PF_MEAN = teamBLast.PF_B.mean()
    teamB_OPP_PF_STD = teamBLast.PF_B.std()

    #FGA - A İçin
    teamA_PF_Mean = teamALast.PF_A.mean()
    teamA_PF_STD = teamALast.PF_A.std()
    teamA_OPP_PF_MEAN = teamALast.PF_B.mean()
    teamA_OPP_PF_STD = teamALast.PF_B.std()



    wins = 0
    losses = 0
    for i in range(n):
        result = gameSim()
        if result == 1:
            wins = wins + 1
        elif result == 0:
            losses = losses + 1
        
    return wins,losses