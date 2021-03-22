from tkinter import *
from tkinter import messagebox
from Giocatore import Giocatore
from Squadra import Squadra

#funzione che resetta la GUI ad ogni nuovo giocatore schedulato
def resettaValoriAsta():
    pass




#funzione che serva a nascondere le label vuote
def nascondiLabel():
    for i in range(12):
        if i==0:
            if infoSquadra1.cget("text")==" ":   
                infoSquadra1.grid_remove()
        if i==1:
            if infoSquadra2.cget("text")==" ":   
                infoSquadra2.grid_remove()
        if i==2:
            if infoSquadra3.cget("text")==" ":   
                infoSquadra3.grid_remove()
        if i==3:
            if infoSquadra4.cget("text")==" ":   
                infoSquadra4.grid_remove()
        if i==4:
            if infoSquadra5.cget("text")==" ":   
                infoSquadra5.grid_remove()
        if i==5:
            if infoSquadra6.cget("text")==" ":   
                infoSquadra6.grid_remove()
        if i==6:
            if infoSquadra7.cget("text")==" ":   
                infoSquadra7.grid_remove()
        if i==7:
            if infoSquadra8.cget("text")==" ":   
                infoSquadra8.grid_remove()
        if i==8:
            if infoSquadra9.cget("text")==" ":   
                infoSquadra9.grid_remove()
        if i==9:
            if infoSquadra10.cget("text")==" ":   
                infoSquadra10.grid_remove()
        if i==10:
            if infoSquadra11.cget("text")==" ":   
                infoSquadra11.grid_remove()
        if i==11:
            if infoSquadra12.cget("text")==" ":   
                infoSquadra12.grid_remove()


#modifica la stampa a video, quindi le labels, che mostra le informazioni inerenti alle squadre
def mostraSquadre():
    global listaSquadre, infoSquadra1, infoSquadra2, infoSquadra3, infoSquadra4, infoSquadra5, infoSquadra6, infoSquadra7, infoSquadra8, infoSquadra9, infoSquadra10, infoSquadra11, infoSquadra12
    for i in range(len(listaSquadre)):
        if i == 0:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra1.config(text=stringa)
        elif i == 1:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra2.config(text=stringa)
        elif i == 2:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra3.config(text=stringa)
        elif i == 3:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra4.config(text=stringa)
        elif i == 4:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra5.config(text=stringa)
        elif i == 5:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra6.config(text=stringa)
        elif i == 6:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra7.config(text=stringa)
        elif i == 7:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra8.config(text=stringa)
        elif i == 8:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra9.config(text=stringa)
        elif i == 9:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra10.config(text=stringa)
        elif i == 10:
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra11.config(text=stringa)
        elif i == 11: 
            nG=listaSquadre[i].getNomeGiocatore()
            cr=listaSquadre[i].getCreditiGiocatore()
            nS=listaSquadre[i].getNomeSquadra()
            numP=listaSquadre[i].getNumeroPortieri()
            numD=listaSquadre[i].getNumeroDifensori()
            numC=listaSquadre[i].getNumeroCentrocampisti()
            numA=listaSquadre[i].getNumeroAttaccanti()
            stringa=nS+"\n"+nG+"\n"+"Crediti: "+str(cr)+"\n"+"Numero P: "+ str(numP)+"\n"+"Numero D: "+ str(numD)+"\n"+"Numero C: "+ str(numC)+"\n"+"Numero A: "+ str(numA)
            infoSquadra12.config(text=stringa)                       


#crea la finestra che servirà per gestire l'asta
def inizializzazioneFinestra():
    global finestra, infoSquadra1, infoSquadra2, infoSquadra3, infoSquadra4, infoSquadra5, infoSquadra6, infoSquadra7, infoSquadra8, infoSquadra9, infoSquadra10, infoSquadra11, infoSquadra12
    finestra = Tk()
    finestra.geometry('1250x400')  
    finestra.grid_columnconfigure(0, minsize=100)
    finestra.grid_columnconfigure(1, minsize=100)
    finestra.grid_columnconfigure(2, minsize=100)
    finestra.grid_columnconfigure(3, minsize=100)
    finestra.grid_columnconfigure(4, minsize=100)
    finestra.grid_columnconfigure(5, minsize=100)
    finestra.grid_columnconfigure(6, minsize=100)
    finestra.grid_columnconfigure(7, minsize=100)
    finestra.grid_columnconfigure(8, minsize=100)
    finestra.grid_columnconfigure(9, minsize=100)
    finestra.grid_columnconfigure(10, minsize=100)
    finestra.grid_columnconfigure(11, minsize=100)
    finestra.grid_rowconfigure(5, minsize=100)
    infoSquadra1=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra2=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra3=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra4=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra5=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra6=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra7=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra8=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra9=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra10=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra11=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra12=Label(finestra, text=" ", relief=GROOVE)
    infoSquadra1.grid(column=0, row=6)
    infoSquadra2.grid(column=1, row=6)
    infoSquadra3.grid(column=2, row=6)
    infoSquadra4.grid(column=3, row=6)
    infoSquadra5.grid(column=4, row=6)
    infoSquadra6.grid(column=5, row=6)
    infoSquadra7.grid(column=6, row=6)
    infoSquadra8.grid(column=7, row=6)
    infoSquadra9.grid(column=8, row=6)
    infoSquadra10.grid(column=9, row=6)
    infoSquadra11.grid(column=10, row=6)
    infoSquadra12.grid(column=11, row=6)

    bottoneIniziaAsta=Button(finestra, text="Inizia Asta")
    bottoneIniziaAsta.grid(column=1, row=5)
    bottoneProssimoGiocatore=Button(finestra, text="Prossimo giocatore")
    bottoneProssimoGiocatore.grid(column=10, row=5)

    mostraSquadre()
    nascondiLabel()

    finestra.mainloop()
    

#funzione inizializzazione che viene chiamata dalla finestra precedente a cui viene passata la lista dei giocatori e la lista delle squadre
def inizializzazione(lG:list, lS:list):
    global listaGiocatori, listaSquadre
    listaGiocatori = lG.copy()
    listaSquadre = lS.copy()
    inizializzazioneFinestra()
