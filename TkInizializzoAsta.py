from tkinter import *
from tkinter import messagebox
import TkInizializzoSquadre

def vaiAvanti():
    global finestra, numeroCrediti, numeroPartecipanti, entryNumeroCrediti, entryNumeroPartecipanti
    numeroPartecipanti=entryNumeroPartecipanti.get()
    numeroCrediti=entryNumeroCrediti.get()
    finestra.destroy()
    TkInizializzoSquadre.inizializzazione(numeroCrediti,numeroPartecipanti)

    
finestra = Tk()  
finestra.geometry('270x150')  
finestra.title('Asta Fantacalcio')

labelNumeroPartecipanti=Label(finestra, text="Numero partecipanti")
labelNumeroPartecipanti.grid(column=0, row=0)
entryNumeroPartecipanti=Entry(finestra)
entryNumeroPartecipanti.grid(column=0, row=1)
labelNumeroCrediti=Label(finestra, text="Numero crediti")
labelNumeroCrediti.grid(column=0, row=2)
entryNumeroCrediti=Entry(finestra)
entryNumeroCrediti.grid(column=0, row=3)
bottoneSubmit=Button(finestra, text="Avanti", command=vaiAvanti) #command=inserisci00
bottoneSubmit.grid(column=0, row=4)



finestra.mainloop()


