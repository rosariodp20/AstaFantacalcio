class Giocatore:
    
    def __init__(self, nome, crediti):
        self.nome=nome
        self.crediti=crediti

    def getNome(self):
        return self.nome

    def getCrediti(self):
        return self.crediti

    def setCrediti(self, cred):
        self.crediti=cred