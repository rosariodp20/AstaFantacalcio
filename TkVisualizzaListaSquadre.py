from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from Giocatore import Giocatore
from Squadra import Squadra
from Calciatore import Calciatore
import TkVisualizzaSquadre

def vaiAvanti():
    global listaS, cbSquadre, finestra
    for s in listaS:
        if s.getNomeSquadra()==cbSquadre.get():
            finestra.destroy()
            TkVisualizzaSquadre.inizializzazione(s, listaS)            
            break

    

def creaFinestra():
    global listaSquadre, cbSquadre, finestra
    finestra = Tk()  
    finestra.geometry('260x150')  
    finestra.title('Asta Fantacalcio')
    #chiamo la funzione per centrare
    finestra.eval('tk::PlaceWindow . center')
    #creo font
    myFont = Font(family="Arial Black", size=10)
    #creo label e cb
    labelScegliSquadra=Label(finestra, text="Scegli squadra da visualizzare",font=myFont)
    labelScegliSquadra.grid(column=0, row=0)
    cbSquadre=ttk.Combobox(finestra,state="readonly", values=listaSquadre)
    cbSquadre.grid(column=0, row=1)
    cbSquadre.current(0)
    bottoneSubmit=Button(finestra, text="Visualizza", command=vaiAvanti) 
    bottoneSubmit.grid(column=0, row=2)
    #setto grandezze minime righe e colonne
    finestra.grid_columnconfigure(0, minsize=260)
    finestra.grid_rowconfigure(0, minsize=40)
    finestra.grid_rowconfigure(1, minsize=40)
    finestra.grid_rowconfigure(2, minsize=40)
    #serve per mantenere aperta la finestra
    finestra.mainloop()

def inizializzazione(lS):
    global listaSquadre, listaS
    listaS=lS.copy()
    listaSquadre=[]
    for s in lS:
        listaSquadre.append(s.getNomeSquadra())
    creaFinestra()
