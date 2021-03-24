from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from Giocatore import Giocatore
from Squadra import Squadra
from Calciatore import Calciatore
import TkVisualizzaListaSquadre

def tornaDietro():
    global listaS, finestra
    finestra.destroy()
    TkVisualizzaListaSquadre.inizializzazione(listaS)


def settaLabel():
    global squadra, p1, p2, p3, d1, d2, d3, d4, d5, d6, d7, d8, c1, c2, c3, c4, c5, c6, c7, c8, a1, a2, a3, a4, a5, a6
    listaP = squadra.getListaPortieri().copy()
    listaD = squadra.getListaDifensori().copy()
    listaC = squadra.getListaCentrocampisti().copy() 
    listaA = squadra.getListaAttaccanti().copy()

    for i in range (len(listaP)):
        if i==0:
            p1.config(text=listaP[0].getNome())
        elif i==1:
            p2.config(text=listaP[1].getNome())
        elif i==2:
            p3.config(text=listaP[2].getNome())
    
    for i in range (len(listaD)):
        if i==0:
            d1.config(text=listaD[0].getNome())
        elif i==1:
            d2.config(text=listaD[1].getNome())
        elif i==2:
            d3.config(text=listaD[2].getNome())
        elif i==3:
            d4.config(text=listaD[3].getNome())
        elif i==4:
            d5.config(text=listaD[4].getNome())
        elif i==5:
            d6.config(text=listaD[5].getNome())
        elif i==6:
            d7.config(text=listaD[6].getNome())
        elif i==7:
            d8.config(text=listaD[7].getNome())
        
    for i in range (len(listaC)):
        if i==0:
            c1.config(text=listaC[0].getNome())
        elif i==1:
            c2.config(text=listaC[1].getNome())
        elif i==2:
            c3.config(text=listaC[2].getNome())
        elif i==3:
            c4.config(text=listaC[3].getNome())
        elif i==4:
            c5.config(text=listaC[4].getNome())
        elif i==5:
            c6.config(text=listaC[5].getNome())
        elif i==6:
            c7.config(text=listaC[6].getNome())
        elif i==7:
            c8.config(text=listaC[7].getNome())
    
    for i in range (len(listaA)):
        if i==0:
            a1.config(text=listaA[0].getNome())
        elif i==1:
            a2.config(text=listaA[1].getNome())
        elif i==2:
            a3.config(text=listaA[2].getNome())
        elif i==3:
            a4.config(text=listaA[3].getNome())
        elif i==4:
            a5.config(text=listaA[4].getNome())
        elif i==5:
            a6.config(text=listaA[5].getNome())

    


def creaFinestra():
    global squadra, finestra, p1, p2, p3, d1, d2, d3, d4, d5, d6, d7, d8, c1, c2, c3, c4, c5, c6, c7, c8, a1, a2, a3, a4, a5, a6
    finestra = Tk()  
    finestra.geometry('400x700')  
    finestra.title('Asta Fantacalcio')
    #chiamo la funzione per centrare
    finestra.eval('tk::PlaceWindow . center')
    #creo label e cb
    nomeS=squadra.getNomeSquadra()
    labelNomeSquadra=Label(finestra, text=nomeS ,font=Font(family="Arial Black", size=16))
    labelNomeSquadra.grid(column=0, row=0)
    #setto grandezze minime righe e colonne
    finestra.grid_columnconfigure(0, minsize=400)
    finestra.grid_rowconfigure(0, minsize=40)
    #setto tutte le label
    labelP=Label(finestra, text="PORTIERI",font=Font(family="Arial Black", size=10))
    labelP.grid(column=0, row=1)
    p1=Label(finestra, text=" ")
    p1.grid(column=0, row=2)
    p2=Label(finestra, text=" ")
    p2.grid(column=0, row=3)
    p3=Label(finestra, text=" ")
    p3.grid(column=0, row=4)
    labelD=Label(finestra, text="DIFENSORI",font=Font(family="Arial Black", size=10))
    labelD.grid(column=0, row=5)
    d1=Label(finestra, text=" ")
    d1.grid(column=0, row=6)
    d2=Label(finestra, text=" ")
    d2.grid(column=0, row=7)
    d3=Label(finestra, text=" ")
    d3.grid(column=0, row=8)
    d4=Label(finestra, text=" ")
    d4.grid(column=0, row=9)
    d5=Label(finestra, text=" ")
    d5.grid(column=0, row=10)
    d6=Label(finestra, text=" ")
    d6.grid(column=0, row=11)
    d7=Label(finestra, text=" ")
    d7.grid(column=0, row=12)
    d8=Label(finestra, text=" ")
    d8.grid(column=0, row=13)
    labelC=Label(finestra, text="CENTROCAMPISTI",font=Font(family="Arial Black", size=10))
    labelC.grid(column=0, row=14)
    c1=Label(finestra, text=" ")
    c1.grid(column=0, row=15)
    c2=Label(finestra, text=" ")
    c2.grid(column=0, row=16)
    c3=Label(finestra, text=" ")
    c3.grid(column=0, row=17)
    c4=Label(finestra, text=" ")
    c4.grid(column=0, row=18)
    c5=Label(finestra, text=" ")
    c5.grid(column=0, row=19)
    c6=Label(finestra, text=" ")
    c6.grid(column=0, row=20)
    c7=Label(finestra, text=" ")
    c7.grid(column=0, row=21)
    c8=Label(finestra, text=" ")
    c8.grid(column=0, row=22)
    labelA=Label(finestra, text="ATTACCANTI",font=Font(family="Arial Black", size=10))
    labelA.grid(column=0, row=23)
    a1=Label(finestra, text=" ")
    a1.grid(column=0, row=24)
    a2=Label(finestra, text=" ")
    a2.grid(column=0, row=25)
    a3=Label(finestra, text=" ")
    a3.grid(column=0, row=26)
    a4=Label(finestra, text=" ")
    a4.grid(column=0, row=27)
    a5=Label(finestra, text=" ")
    a5.grid(column=0, row=28)
    a6=Label(finestra, text=" ")
    a6.grid(column=0, row=29)
    #bottone torna dietro
    bottoneSubmit=Button(finestra, text="Indietro", command=tornaDietro) 
    bottoneSubmit.grid(column=0, row=30)

    settaLabel()
    


def inizializzazione(s, lS):
    global squadra, listaS
    listaS=lS.copy()
    squadra=s
    creaFinestra()
