def filter_value(someList, value):
    for x, y, z, w, a in someList:
        if x == value:
            yield x, y, z, w, a

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
            lin[27] = result[0][1]
            lin[28] = result[0][2]
            cont = 1
            print('passei aqui 1', str(cont),lin[8])
            continue

    if lin[1] == 'C100' and not result:
        cont = 0
        print('passei aqui 2', str(cont))

    if lin[1] == 'C17    try:
            print('passei aqui 3', str(cont))
            lin[20] = result[0][4]
            result.pop(0)
            continue
        except IndexError as error:
            print('Deu ruim')

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
