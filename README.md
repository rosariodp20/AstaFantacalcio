# AstaFantacalcio
Un'applicazione Python per la gestione delle aste per il fantacalcio.

## Requisiti
Per fare funzionare in modo corretto l'applicazione occorre avere i seguenti moduli:
-openpyxl che è possibile installare nel seguente modo
```
pip install openpyxl 
```

##Funzionamento

L'applicazione permette agli utenti di gestire in maniera automatica l'asta per il fantacalcio.
Inizialmente verrà richiesto il numero di partecipanti all'asta e il numero di crediti fissati per iniziare.
Successivamente si potranno inserire i nomi dei partecipanti e il nome delle relative squadre.
Una volta terminata questa fase sarà possibile iniziare l'asta. 
Viene caricato automaticamente il file .xlsx di Fantacalcio.it contente la lista dei giocatori con relativo ruoli e squadre.
Automaticamente verranno effettuate le aste per i portieri, i difensori, i centrocampisti e gli attaccanti nell'ordine riportato.
Ogni squadra alla fine dell'asta dovrà avere 3 portiere, 8 difensori, 8 centrocampisti e 6 attaccanti.
Alla fine dell'asta verrà generato un file Excel contente tutte le rose.

##Gestione della fine dei crediti
Se un giocatore termina i crediti prima che termini la rosa, gli verranno assegnati d'ufficio dei giocatori random al costo di un credito, e verrà segnalato alla fine dell'asta chi ha sforato il budget.
