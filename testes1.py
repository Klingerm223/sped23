from notaFiscal import notaFiscal

def filter_value(someList, value):
    for x, y, z, w, a, b  in someList:
        if x == value:
            yield x, y, z, w, a , b

arq_notas = open("notas.txt", "r", encoding="utf-8")
linhas_nf = arq_notas.readlines()
linhas3_nf = []
for lin in linhas_nf:
    linhas3_nf.append(tuple(lin.split()))

notas = linhas3_nf
#print(linhas3_nf)


arq_sped = open("spedmai23n.txt", "r", encoding="utf-8")
linhas_sped = arq_sped.readlines()
linhas2_sped = []
linhas3_sped = []


for lin in linhas_sped:
    linhas3_sped.append(lin.split('|'))

for lin in linhas3_sped:
    print(lin[8])