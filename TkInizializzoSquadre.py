from tkinter import *
from tkinter import messagebox

numeroCrediti = 0
numeroPartecipanti = 0



def creaFinestra(numeroGiocatore):
    finestra = Tk()  
    finestra.geometry('200x150')  
    finestra.title('Asta Fantacalcio')
    giocatore="Nome Giocatore n° "+numeroGiocatore
    labelNomeGiocatore=Label(finestra, text=giocatore)
    labelNomeSquadra=Label(finestra, text=numeroCrediti)
    labelNomeGiocatore.grid(column=0, row=0)
    labelNomeSquadra.grid(column=0, row=1)

    finestra.mainloop()


def inizializzazione(crediti, partecipanti):
    global numeroCrediti, numeroPartecipanti
    numeroPartecipanti=int(partecipanti)
    numeroCrediti=int(crediti)
    for i in range(numeroPartecipanti):
        creaFinestra(i+1)






