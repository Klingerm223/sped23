
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



arq_sped = open("spedmai23n.txt", "r", encoding="utf-8")
linhas_sped = arq_sped.readlines()
linhas2_sped = []
linhas3_sped = []
notas = linhas3_nf

for lin in linhas_sped:
    linhas3_sped.append(lin.split('|'))

cont = 0

for lin in linhas3_sped:
    if lin[1] == 'C100':
        result = list(filter_value(notas, lin[8]))
        if result:
            cont = 1
            print('C100 - passei aqui 1', str(cont), lin[8])
            continue

    if lin[1] == 'C100' and not result:
        cont = 0
        print('C100 - passei aqui 2', str(cont),lin[8])

    if lin[1] == 'C170' and cont == 1:

        try:
            print('C170 - passei aqui 3', str(cont),lin[8] )
            result.pop(0)
            continue
        except IndexError as error:
            print('Deu ruim')

    if lin[1] == 'C175':
        print('C175 - PASSEI AQUI 4',lin[8])
        cont=0


print('####################################')
# for lin in linhas3:
#   print(lin)

with open('sped_correcao.txt', 'w') as arq1:
    for lin in linhas3_sped:
        tx = str(lin)
        arq1.write(tx)
        arq1.write('\n')

arq_notas.close()
arq_sped.close()
arq1.close()
