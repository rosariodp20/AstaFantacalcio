import openpyxl



def CreaTabella(squadre):   #mi importo tutte le istanze delle squadre

    TabellaFinale=openpyxl.Workbook()
    Foglio=TabellaFinale.active
    Foglio.title="Tabella Squadre"
    #TabellaFinale.save('RecapAsta.xlsx')
    nomeCol="A"
    numRiga=str(1)
    numCella=nomeCol+numRiga
    #ListaPortieri=list()
    #listaDifensori=list()
    #listaCentrocampisti=list()
    #listaAttaccanti=list()

    cont=0

    for squadra in squadre:

        listaPortieri=squadra.getListaPortieri()
        listaDifensori=squadra.getListaDifensori()
        listaCentrocampisti=squadra.getListaCentrocampisti()
        listaAttaccanti=squadra.getListaAttaccanti()

        NomeSquadra=squadra.getNomeSquadra()
        Foglio[numCella].value=NomeSquadra        #A1

        numRiga=str(int(numRiga)+1)
        numCella=nomeCol+numRiga         #A2
        Foglio[numCella].value="Portieri"

        numRiga=str(int(numRiga)+1)
        numCella=nomeCol+numRiga          #A3

        for portiere in listaPortieri:
            nomePort=portiere.getNome()
            squadraPort=portiere.getSquadra()
            costoPort=portiere.getValore()

            StringaPortiere=str(nomePort)+" "+str(costoPort)+" "+str(squadraPort)
            Foglio[numCella].value=str(StringaPortiere)

            numRiga=str(int(numRiga)+1)
            numCella=nomeCol+numRiga

        Foglio[numCella].value="Difensori"

        numRiga=str(int(numRiga)+1)
        numCella=nomeCol+numRiga

        for difensore in listaDifensori:
            nomeDif=difensore.getNome()
            squadraDif=difensore.getSquadra()
            costoDif=difensore.getValore()

            StringaDifensore=str(nomeDif)+" "+str(costoDif)+" "+str(squadraDif)
            Foglio[numCella].value=str(StringaDifensore)

            numRiga=str(int(numRiga)+1)
            numCella=nomeCol+numRiga

        Foglio[numCella].value="Centrocampisti"

        numRiga=str(int(numRiga)+1)
        numCella=nomeCol+numRiga

        for centrocampista in listaCentrocampisti:
            nomeCentr=centrocampista.getNome()
            squadraCentr=centrocampista.getSquadra()
            costoCentr=centrocampista.getValore()

            StringaCentrocampista=str(nomeCentr)+" "+str(costoCentr)+" "+str(squadraCentr)
            Foglio[numCella].value=str(StringaCentrocampista)

            numRiga=str(int(numRiga)+1)
            numCella=nomeCol+numRiga

        Foglio[numCella].value="Attaccanti"

        numRiga=str(int(numRiga)+1)
        numCella=nomeCol+numRiga

        for attaccante in listaAttaccanti:
            nomeAtt=attaccante.getNome()
            squadraAtt=attaccante.getSquadra()
            costoAtt=attaccante.getValore()

            StringaAttaccante=str(nomeAtt)+" "+str(costoAtt)+" "+str(squadraAtt)
            Foglio[numCella].value=str(StringaAttaccante)

            numRiga=str(int(numRiga)+1)
            numCella=nomeCol+numRiga

        numRiga=str(1)

        if cont==0:
            nomeCol="B"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==1:
            nomeCol="C"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==2:
            nomeCol="D"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==3:
            nomeCol="E"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==4:
            nomeCol="F"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==5:
            nomeCol="G"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==6:
            nomeCol="H"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==7:
            nomeCol="I"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==8:
            nomeCol="L"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==9:
            nomeCol="M"
            numCella=nomeCol+numRiga
            cont=cont+1

        elif cont==10:
            nomeCol="N"
            numCella=nomeCol+numRiga
            cont=cont+1

    TabellaFinale.save('RecapAsta.xlsx')
