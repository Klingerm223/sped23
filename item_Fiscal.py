class itemFiscal:
    def __init__ (self, nota):
        self.nf = nota[0]
        self.serie = nota[1]
        self.material = nota[2]
        self.baseCalculo = float(nota[3])
        self.pisDev = float(nota[4])
        self.cofisDev = float(nota[5])

    def __str__(self):
        return str(self.nf+','+self.serie+','+self.material+','+str(self.baseCalculo)+','+str(self.pisDev)+','+str(self.cofisDev))

    def getPisDev(self):
        return self.pisDev

    def getCofisDev(self):
        return self.cofisDev

    def getBaseCalculo (self):
        return self.baseCalculo





#self.nf,self.serie,self.material,self.baseCalculo,self.pisDev,self.cofisDev)

