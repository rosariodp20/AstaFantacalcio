from tkinter import *
from tkinter import messagebox
from Giocatore import Giocatore
from Squadra import Squadra
import TkInizioAsta
from tkinter.font import Font

#funzione che serve per creare i giocatori e le squadre e aggiugnerli in una lista. Arrivati
#all'ultimo giocatore da inserire viene chiamata la funzione inizializzazione di TkInzioAsta.py
def vaiAvanti(numeroGiocatore):
    global finestra, listaGiocatori, listaSquadre, entryNomeGiocatore, entryNomeSquadra, numeroCrediti, numeroPartecipanti, i
    i=numeroGiocatore-1
    if numeroGiocatore<numeroPartecipanti:
        if entryNomeGiocatore.get()!="" and entryNomeSquadra.get()!="":       
            nomeGiocatore=entryNomeGiocatore.get()
            giocatore = Giocatore(nomeGiocatore,numeroCrediti)
            listaGiocatori.append(giocatore)
            nomeSquadra=entryNomeSquadra.get()
            squadra= Squadra(giocatore,nomeSquadra,[],[],[],[])
            listaSquadre.append(squadra)
            finestra.destroy()
        else:
            messagebox.showinfo("Errore", "Inserire i campi richiesti")
            i-=1
    else:
        if entryNomeGiocatore.get()!="" and entryNomeSquadra.get()!="": 
            nomeGiocatore=entryNomeGiocatore.get()
            giocatore = Giocatore(nomeGiocatore,numeroCrediti)
            listaGiocatori.append(giocatore)
            nomeSquadra=entryNomeSquadra.get()
            squadra= Squadra(giocatore,nomeSquadra,[],[],[],[])
            listaSquadre.append(squadra)
            finestra.destroy()
            TkInizioAsta.inizializzazione(listaGiocatori,listaSquadre)
        else:
            messagebox.showinfo("Errore", "Inserire i campi richiesti")
            i-=1


#funzione che crea una finestra per ogni squadra da inserire e giocatore
def creaFinestra(numeroGiocatore):
    global finestra, entryNomeSquadra, entryNomeGiocatore
    finestra = Tk() 
    finestra.geometry('260x210')  
    finestra.title('Asta Fantacalcio')
    finestra.iconbitmap('icona.ico')
    giocatore="Nome Giocatore n° "+str(numeroGiocatore)
    #chiamo la funzione per centrare
    finestra.eval('tk::PlaceWindow . center')
    #creo font
    myFont = Font(family="Arial Black", size=12)
    #creo label e entry
    labelNomeGiocatore=Label(finestra, text=giocatore,font=myFont)
    labelNomeGiocatore.grid(column=0, row=0)
    entryNomeGiocatore=Entry(finestra)
    entryNomeGiocatore.grid(column=0, row=1)
    labelNomeSquadra=Label(finestra, text="Nome Squadra",font=myFont)
    labelNomeSquadra.grid(column=0, row=2)
    entryNomeSquadra=Entry(finestra)
    entryNomeSquadra.grid(column=0, row=3)
    bottoneSubmit=Button(finestra, text="Avanti", command=lambda: vaiAvanti(numeroGiocatore)) #command=inserisci00
    bottoneSubmit.grid(column=0, row=4)
    #setto le grandezze minime dell righe e le colonne
    finestra.grid_columnconfigure(0, minsize=260)
    finestra.grid_rowconfigure(0, minsize=40)
    finestra.grid_rowconfigure(1, minsize=40)
    finestra.grid_rowconfigure(2, minsize=40)
    finestra.grid_rowconfigure(3, minsize=40)
    finestra.grid_rowconfigure(4, minsize=40)
    finestra.mainloop()
    



#iniziallizazione chiamata dalla finestra precedente che ha passato il numero di crediti e il numero di partecipanti
def inizializzazione(crediti, partecipanti):
    global numeroCrediti, numeroPartecipanti, listaGiocatori, listaSquadre, i
    listaGiocatori=[]
    listaSquadre=[]
    numeroPartecipanti=int(partecipanti)
    numeroCrediti=int(crediti)
    i=0
    #viene chiamato il costruttore delle finestre per ogni squadra da inserire e giocatore
    for i in range(numeroPartecipanti):
        creaFinestra(i+1)






