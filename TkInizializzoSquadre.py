from tkinter import *
from tkinter import messagebox
from Giocatore import Giocatore
from Squadra import Squadra
import TkInizioAsta

#funzione che serve per creare i giocatori e le squadre e aggiugnerli in una lista. Arrivati
#all'ultimo giocatore da inserire viene chiamata la funzione inizializzazione di TkInzioAsta.py
def vaiAvanti(numeroGiocatore):
    global finestra, listaGiocatori, listaSquadre, entryNomeGiocatore, entryNomeSquadra, numeroCrediti, numeroPartecipanti
    if numeroGiocatore<numeroPartecipanti:
        nomeGiocatore=entryNomeGiocatore.get()
        giocatore = Giocatore(nomeGiocatore,numeroCrediti)
        listaGiocatori.append(giocatore)
        nomeSquadra=entryNomeSquadra.get()
        squadra= Squadra(giocatore,nomeSquadra,[],[],[],[])
        listaSquadre.append(squadra)
        finestra.destroy()
    else:
        nomeGiocatore=entryNomeGiocatore.get()
        giocatore = Giocatore(nomeGiocatore,numeroCrediti)
        listaGiocatori.append(giocatore)
        nomeSquadra=entryNomeSquadra.get()
        squadra= Squadra(giocatore,nomeSquadra,[],[],[],[])
        listaSquadre.append(squadra)
        finestra.destroy()
        TkInizioAsta.inizializzazione(listaGiocatori,listaSquadre)


#funzione che crea una finestra per ogni squadra da inserire e giocatore
def creaFinestra(numeroGiocatore):
    global finestra, entryNomeSquadra, entryNomeGiocatore
    finestra = Tk() 
    finestra.geometry('200x150')  
    finestra.title('Asta Fantacalcio')
    giocatore="Nome Giocatore n° "+str(numeroGiocatore)
    labelNomeGiocatore=Label(finestra, text=giocatore)
    labelNomeGiocatore.grid(column=0, row=0)
    entryNomeGiocatore=Entry(finestra)
    entryNomeGiocatore.grid(column=0, row=1)
    labelNomeSquadra=Label(finestra, text="Nome Squadra")
    labelNomeSquadra.grid(column=0, row=2)
    entryNomeSquadra=Entry(finestra)
    entryNomeSquadra.grid(column=0, row=3)
    bottoneSubmit=Button(finestra, text="Avanti", command=lambda: vaiAvanti(numeroGiocatore)) #command=inserisci00
    bottoneSubmit.grid(column=0, row=4)
    finestra.mainloop()


#iniziallizazione chiamata dalla finestra precedente che ha passato il numero di crediti e il numero di partecipanti
def inizializzazione(crediti, partecipanti):
    global numeroCrediti, numeroPartecipanti, listaGiocatori, listaSquadre
    listaGiocatori=[]
    listaSquadre=[]
    numeroPartecipanti=int(partecipanti)
    numeroCrediti=int(crediti)
    #viene chiamato il costruttore delle finestre per ogni squadra da inserire e giocatore
    for i in range(numeroPartecipanti):
        creaFinestra(i+1)






