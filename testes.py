def filter_value(someList, value):
    for a, b, c, d, e in someList:
        if a == value:
            yield a, b, c, d, e

arq = open("notas.txt", "r", encoding="utf-8")
linhas = arq.readlines()
linhas3 = []
for lin in linhas:
    #linhas2 = lin.split()
    linhas3.append(tuple(lin.split()))

print(linhas3[5])





