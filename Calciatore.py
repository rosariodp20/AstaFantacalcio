class Calciatore:

    def __init__(self, nome, squadra, ruolo):
        self.nome=nome
        self.squadra=squadra
        self.ruolo=ruolo

    def getNome(self):
        return self.nome

    def getSquadra(self):
        return self.squadra

    def getRuolo(self):
        return self.ruolo