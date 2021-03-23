from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import TkInizializzoSquadre
from tkinter.font import Font


#funzione chiamata dal bottoneSubmit che serve a chiudere la finestra ed aprire la successiva
def vaiAvanti():
    global finestra, numeroCrediti, numeroPartecipanti, cbNumeroCrediti, cbNumeroPartecipanti
    numeroPartecipanti=cbNumeroPartecipanti.get()
    numeroCrediti=cbNumeroCrediti.get()
    finestra.destroy()
    TkInizializzoSquadre.inizializzazione(numeroCrediti,numeroPartecipanti)

#creo una finestra     
finestra = Tk()  
finestra.geometry('260x205')  
finestra.title('Asta Fantacalcio')
#chiamo la funzione per centrare
finestra.eval('tk::PlaceWindow . center')
#creo font
myFont = Font(family="Arial Black", size=12)
#inserisco le apposite label, le entry e il bottone per proseguire
labelNumeroPartecipanti=Label(finestra, text="Numero partecipanti",font=myFont)
labelNumeroPartecipanti.grid(column=0, row=0)
cbNumeroPartecipanti=ttk.Combobox(finestra,state="readonly", values=[2,3,4,5,6,7,8,9,10,11,12])
cbNumeroPartecipanti.grid(column=0, row=1)
cbNumeroPartecipanti.current(0)
labelNumeroCrediti=Label(finestra, text="Numero crediti",font=myFont)
labelNumeroCrediti.grid(column=0, row=2)
cbNumeroCrediti=ttk.Combobox(finestra,state="readonly", values=[100,200,300,400,500,600,700,800,900,1000])
cbNumeroCrediti.grid(column=0, row=3)
cbNumeroCrediti.current(0)
bottoneSubmit=Button(finestra, text="Avanti", command=vaiAvanti) 
bottoneSubmit.grid(column=0, row=4)
#setto le grandezze minime dell righe e le colonne
finestra.grid_columnconfigure(0, minsize=260)
finestra.grid_rowconfigure(0, minsize=40)
finestra.grid_rowconfigure(1, minsize=40)
finestra.grid_rowconfigure(2, minsize=40)
finestra.grid_rowconfigure(3, minsize=40)
finestra.grid_rowconfigure(4, minsize=40)



#serve per mantenere aperta la finestra
finestra.mainloop()


