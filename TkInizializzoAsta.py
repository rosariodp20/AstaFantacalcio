from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import TkInizializzoSquadre

#funzione chiamata dal bottoneSubmit che serve a chiudere la finestra ed aprire la successiva
def vaiAvanti():
    global finestra, numeroCrediti, numeroPartecipanti, cbNumeroCrediti, cbNumeroPartecipanti
    numeroPartecipanti=cbNumeroPartecipanti.get()
    numeroCrediti=cbNumeroCrediti.get()
    finestra.destroy()
    TkInizializzoSquadre.inizializzazione(numeroCrediti,numeroPartecipanti)

#creo una finestra     
finestra = Tk()  
finestra.geometry('270x150')  
finestra.title('Asta Fantacalcio')


#inserisco le apposite label, le entry e il bottone per proseguire
labelNumeroPartecipanti=Label(finestra, text="Numero partecipanti")
labelNumeroPartecipanti.grid(column=0, row=0)
cbNumeroPartecipanti=ttk.Combobox(finestra,state="readonly", values=[2,3,4,5,6,7,8,9,10,11,12])
cbNumeroPartecipanti.grid(column=0, row=1)
cbNumeroPartecipanti.current(0)
labelNumeroCrediti=Label(finestra, text="Numero crediti")
labelNumeroCrediti.grid(column=0, row=2)
cbNumeroCrediti=ttk.Combobox(finestra,state="readonly", values=[100,200,300,400,500,600,700,800,900,1000])
cbNumeroCrediti.grid(column=0, row=3)
cbNumeroCrediti.current(0)
bottoneSubmit=Button(finestra, text="Avanti", command=vaiAvanti) 
bottoneSubmit.grid(column=0, row=4)



#serve per mantenere aperta la finestra
finestra.mainloop()


