from Giocatore import Giocatore

class Squadra:
    
    def __init__(self, giocatore:Giocatore, nome:str, listaPortieri:list, listaDifensori:list,listaCentrocampisti:list,listaAttaccanti:list):
        self.giocatore=giocatore
        self.nome=nome
        self.listaPortieri=listaPortieri
        self.listaDifensori=listaDifensori
        self.listaCentrocampisti=listaCentrocampisti
        self.listaAttaccanti=listaAttaccanti
    
    def getNomeGiocatore(self):
        return self.giocatore.getNome()

    def getCreditiGiocatore(self):
        return self.giocatore.getCrediti()

    def getNomeSquadra(self):
        return self.nome

    def getNumeroPortieri(self):
        num=len(self.listaPortieri)
        return num

    def getNumeroDifensori(self):
        num=len(self.listaDifensori)
        return num
    
    def getNumeroCentrocampisti(self):
        num=len(self.listaCentrocampisti)
        return num
    
    def getNumeroAttaccanti(self):
        num=len(self.listaAttaccanti)
        return num
    
    def aggiungiPortiere(self, giocatore):
        self.listaPortieri.append(giocatore)

    def aggiungiDifensore(self, giocatore):
        self.listaDifensori.append(giocatore)
    
    def aggiungiCentrocampista(self, giocatore):
        self.listaCentrocampisti.append(giocatore)
    
    def aggiungiAttaccante(self, giocatore):
        self.listaAttaccanti.append(giocatore)

    def scalaCrediti(self, togliere):
        crediti=self.giocatore.getCrediti()
        self.giocatore.setCrediti(crediti-togliere)

    #aggiungi difensori
    #aggiungi centrocampisti
    #aggiungi attaccantu