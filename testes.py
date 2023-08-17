
from notaFiscal import notaFiscal
def filter_value(someList, value):
    for a, b, c, d, e in someList:
        if a == value:
            yield a, b, c, d, e

arq = open("notas.txt", "r", encoding="utf-8")
linhas = arq.readlines()
linhas3 = []
cont=0
listadeNotas = []
for lin in linhas:
    linhas3.append(tuple(lin.split()))

for lin in tuplas:




#print(linhas3[0])



#print(linhas3[5])

#item.imprime()
# conjuntoNotas = []
# notas = notaFiscal()
# notas.add_item(linhas3[1])
# notas.add_item(linhas3[2])
# notas.add_item(linhas3[3])
#
# notas.mostrarItensNotas()
# print(notas.calcTotalPisDev())
# print(notas.calcTotalConfisDev())
# print(notas.calcBaseCalculo())
# conjuntoNotas.append(notas)
# print(conjuntoNotas[0].mostrarItensNotas())









