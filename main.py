from tkinter import *
import tkinter.ttk as ttk
from futurePrediction import simulateGames


def clicked():
    sonucLbl.config(text= "Hesaplanıyor")
    homeTeamAbbr = homeTeamCbox.get()
    awayTeamAbbr = awayTeamCbox.get()
    home,away = simulateGames(1000,homeTeamAbbr,awayTeamAbbr)
    resultText = f"{homeTeamAbbr} %{home/10} -- %{away/10} {awayTeamAbbr}"
    sonucLbl.config(text=resultText)


root = Tk()
root.title("NBA Tahmin")
root.minsize(415, 250)  # width, height
root.geometry("300x300+50+50")


homeTeamlbl = Label(root, text="Ev sahibi takım", font=("Arial Bold", 11) )
homeTeamlbl.grid(column=0, row=0, padx=15, pady=15)


awayTeamlbl = Label(root, text="Deplasman takımı", font=("Arial Bold", 11))
awayTeamlbl.grid(column=2, row=0, padx=15, pady=10)

homeTeamCbox = ttk.Combobox(root, width=10)
homeTeamCbox['values'] = ('BOS', 'ATL', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU','LAC', 'LAL', 'MIA', 'MIL', 'MIN', 'BKN', 'NYK', 'ORL', 'IND','PHI', 'PHX', 'POR', 'SAC', 'SAS', 'OKC', 'TOR', 'UTA', 'MEM','WAS', 'DET', 'CHA')
homeTeamCbox.current(1)
homeTeamCbox.grid(column=0, row=1, padx=5, pady=5)

awayTeamCbox = ttk.Combobox(root, width=10)
awayTeamCbox['values'] = ('BOS', 'ATL', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU','LAC', 'LAL', 'MIA', 'MIL', 'MIN', 'BKN', 'NYK', 'ORL', 'IND','PHI', 'PHX', 'POR', 'SAC', 'SAS', 'OKC', 'TOR', 'UTA', 'MEM','WAS', 'DET', 'CHA')
awayTeamCbox.current(2)
awayTeamCbox.grid(column=2, row=1, padx=5, pady=5)

btn = Button(root, text="Hesapla", command=clicked, height=3, width=15, fg="black", bg="gray")
btn.grid(column=1, row=5)

sonucLbl = Label(root, text="Hesapla butonuna basınız.", font=("Arial Bold", 8))
sonucLbl.grid(column=1,row=10, pady=5)

root.mainloop()