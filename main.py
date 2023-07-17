arq = open("spedmai23n.txt","r",encoding="utf-8")
linhas =  arq.readlines()
linhas2 = []
linhas3 = []
notas = ['931267' ]

for lin in linhas:
    linhas2 = lin.split('|')
    linhas3.append(linhas2)

cont = 0

for lin in linhas3:
    if lin[1] == 'C100' and lin[8] in notas:
        lin[8] = 'TESTES'
        lin[10] = 'testes'
        cont = 1
        continue
    if lin[1] == 'C100' and lin[8] not in notas:
        cont = 0
        print('passei aqui 2', str(cont))

    if lin[1] == 'C170' and cont == 1:
        lin[13] = 'TESTES'
        print('passei aqui 3', str(cont))
        continue


print('####################################')
#for lin in linhas3:
 #   print(lin)

with open('sped_correcao.txt','w') as arq1:
    for lin in linhas3:
        tx = str(lin)
        arq1.write(tx)
        arq1.write('\n')


arq.close()
arq1.close()

