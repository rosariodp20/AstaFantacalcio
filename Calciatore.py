class Calciatore:

    def __init__(self, nome, squadra, ruolo, valore=0):
        self.nome=nome
        self.squadra=squadra
        self.ruolo=ruolo
        self.valore=valore

    def getNome(self):
        return self.nome

    def getSquadra(self):
        return self.squadra

    def getRuolo(self):
        return self.ruolo
    
    def getValore(self):
        return self.valore

    def incrementaValore(self, incremento):
        self.valore+=incremento