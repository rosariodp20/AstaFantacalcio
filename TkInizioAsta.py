from tkinter import *
from tkinter import messagebox
from Giocatore import Giocatore
from Squadra import Squadra
from tkinter.font import Font
import ListeCalciatori

#funzione che gestisce la fine dell asta
def astaFinita():
    global flagAstaIniziata, listaSquadre, listaGiocatori, labelNomeGiocatoreUltimaOfferta, labelR, calciatorePOP
    flagAstaIniziata=0
    for squadra in listaSquadre:
        if labelNomeGiocatoreUltimaOfferta.cget("text")==squadra.getNomeGiocatore():
            if labelR.cget("text")=="P":
                squadra.aggiungiPortiere(calciatorePOP)
                #scalare crediti



#funzione che gestisce i rilanci
def rilancia(event):
    global flagAstaIniziata, labelTempo, labelR  
    if flagAstaIniziata==1:
        if (event.char=="q" or event.char=="Q") and infoSquadra1.cget("text")!=" " and ((listaSquadre[0].getNumeroPortieri()!=3 and labelR.cget("text")=="P") or (listaSquadre[0].getNumeroDifensori()!=8 and labelR.cget("text")=="D") or(listaSquadre[0].getNumeroCentrocampisti()!=8 and labelR.cget("text")=="C") or(listaSquadre[0].getNumeroAttaccanti()!=6 and labelR.cget("text")=="A")):  
            labelTempo.config(text="10")
            print("ha premuto il giocatore 1")
            #incremento variabile valore attuale +1 del calciatore
            #mostro nella label
            #cambio nome giocatore ultima offerta
        elif (event.char=="w" or event.char=="W") and infoSquadra1.cget("text")!=" " and ((listaSquadre[0].getNumeroPortieri()!=3 and labelR.cget("text")=="P") or (listaSquadre[0].getNumeroDifensori()!=8 and labelR.cget("text")=="D") or(listaSquadre[0].getNumeroCentrocampisti()!=8 and labelR.cget("text")=="C") or(listaSquadre[0].getNumeroAttaccanti()!=6 and labelR.cget("text")=="A")):  
            labelTempo.config(text="10")
            print("ha premuto il giocatore 1")
            #incremento variabile valore attuale +5 del calciatore
            #mostro nella label
            #cambio nome giocatore ultima offerta


#funzione che resetta la GUI ad ogni nuovo giocatore schedulato
def resettaValoriAsta():
    pass

def aggiornaTimer():
    global labelTempo,finestra
    tem=int(labelTempo.cget("text"))
    tem-=1
    labelTempo.config(text=str(tem))
    if tem!= 0:
        finestra.after(1000, aggiornaTimer)
    else:
        astaFinita()


def prossimoCalciatore():
    global calciatorePOP, listaPorteri, listaDifensori, listaCentrocampisti, listaAttaccanti
    #lo appendo alla giusta lista
    #nuova pop calciatore
    #modifico le label

    
    #contatoreP=0
    #contatoreD=0
    #contatoreC=0
    #contatoreA=0
    #for squadra in listaSquadre:
    #    contatoreP+=squadra.getNumeroPortieri()
    #    contatoreD+=squadra.getNumeroDifensori()
    #    contatoreC+=squadra.getNumeroCentrocampisti()
    #    contatoreA+=squadra.getNumeroAttaccanti()
    #
    #if contatoreP<(len(listaSquadre)*3):


#funzione che fa iniziare l'asta
def inizioAsta():
    global finestra, listaSquadre, listaGiocatori, flagAstaIniziata, labelTempo, calciatorePOP
    ######CONTROLLI MIRO
    flagAstaIniziata=1
    labelTempo.config(text="10")
    finestra.after(1000, aggiornaTimer)
    
        

    



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
    global finestra, infoSquadra1, infoSquadra2, infoSquadra3, infoSquadra4, infoSquadra5, infoSquadra6, infoSquadra7, infoSquadra8, infoSquadra9, infoSquadra10, infoSquadra11, infoSquadra12, labelTempo, labelR, labelNomeGiocatoreUltimaOfferta, calciatorePOP
    finestra = Tk()
    finestra.geometry('1400x800')  
    #setta le dimensioni minime di righe e colonne
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
    finestra.grid_rowconfigure(0, minsize=50)
    finestra.grid_rowconfigure(1, minsize=50)
    finestra.grid_rowconfigure(2, minsize=50)
    finestra.grid_rowconfigure(3, minsize=50)
    finestra.grid_rowconfigure(4, minsize=50)
    finestra.grid_rowconfigure(5, minsize=50)
    finestra.grid_rowconfigure(6, minsize=50)

    #label per le info dei giocatori
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

    #creo font
    myFont = Font(family="Arial Black", size=16)

    #bottoni interfaccia
    bottoneIniziaAsta=Button(finestra, text="Inizia Asta", command=inizioAsta)
    bottoneIniziaAsta.grid(column=1, row=5)
    bottoneProssimoGiocatore=Button(finestra, text="Prossimo giocatore")
    bottoneProssimoGiocatore.grid(column=10, row=5)

    #label timer
    labelTimer = Label(finestra, text="Timer: ", font=myFont, fg="#077324")
    labelTimer.grid(column=6, row=4)
    labelTempo = Label(finestra, text="10", font=myFont, fg="#077324")
    labelTempo.grid(column=7, row=4)

    #label ruolo 
    labelRuolo = Label(finestra, text="Ruolo: ", font=myFont, fg="#013966")
    labelRuolo.grid(column=6, row=3)
    labelR = Label(finestra, text=calciatorePOP.getRuolo(), font=myFont, fg="#013966")
    labelR.grid(column=7, row=3)

    #label nome calciatore e squadra
    labelNomeCalciatore = Label(finestra, text=calciatorePOP.getNome(), font=myFont)
    labelNomeCalciatore.grid(column=6, row=2)
    labelSqCalciatore = Label(finestra, text=calciatorePOP.getSquadra(), fg="#5c0000", font=myFont)
    labelSqCalciatore.grid(column=7, row=2)

    #label ultima offerta e valore attuale
    labelNomeUltimaOfferta=Label(finestra, text="Ultima offerta:", font=myFont, fg="#330230")
    labelNomeGiocatoreUltimaOfferta=Label(finestra, text="Nome Giocatore", font=myFont, fg="#330230")
    labelValoreAttuale=Label(finestra, text="Valore attuale:", font=myFont, fg="#a65e00")
    labelValoreAttualeNumero=Label(finestra, text="0", font=myFont)
    labelNomeUltimaOfferta.grid(column=9, row=0)
    labelNomeGiocatoreUltimaOfferta.grid(column=9, row=1)
    labelValoreAttuale.grid(column=9, row=3)
    labelValoreAttualeNumero.grid(column=9, row=4)

    mostraSquadre()
    nascondiLabel()

    #sempre per intercettare i tasti della tastiera
    finestra.bind("<Key>", rilancia)

    finestra.mainloop()
    

#funzione inizializzazione che viene chiamata dalla finestra precedente a cui viene passata la lista dei giocatori e la lista delle squadre
def inizializzazione(lG:list, lS:list):
    global listaGiocatori, listaSquadre, listaPorteri, listaDifensori, listaCentrocampisti, listaAttaccanti, flagAstaIniziata, calciatorePOP
    listaGiocatori = lG.copy()
    listaSquadre = lS.copy()
    
    ListeCalciatori.CreaIstanzeCalciatori()
    listaAttaccanti=ListeCalciatori.getAttaccanti().copy()
    listaPorteri=ListeCalciatori.getPortieri().copy()
    listaDifensori=ListeCalciatori.getDifensori().copy()
    listaCentrocampisti=ListeCalciatori.getCentrocampisti().copy()
    flagAstaIniziata=0
    calciatorePOP=listaPorteri.pop()

    print(listaPorteri)
    inizializzazioneFinestra()

