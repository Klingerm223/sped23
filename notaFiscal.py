from item_Fiscal import itemFiscal

class notaFiscal:
    def __init__(self):
        self.itensNota = []
    def add_item (self,*args):
        novoItem = itemFiscal(*args)
        self.itensNota.append(novoItem)


    def mostrarItensNotas(self):
        for index, tupla in enumerate(self.itensNota, start=1):
            print(tupla)

    def calcTotalPisDev (self):
        total:float = 0.00
        for index, tupla in enumerate(self.itensNota, start=1):
            total += tupla.getPisDev()
        return total


    def calcTotalConfisDev (self):
        total:float = 0.00
        for index, tupla in enumerate(self.itensNota, start=1):
            total += tupla.getCofisDev()
        return total

    def calcBaseCalculo (self):
        total:float = 0.00
        for index, tupla in enumerate(self.itensNota, start=1):
            total += tupla.getBaseCalculo()
        return total











