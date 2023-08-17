class item_Fiscal:
    def __init__ (self, nota):
        self.nf = nota[0]
        self.serie = nota[1]
        self.material = nota[2]
        self.baseCalculo = float(nota[3])
        self.pisDev = float(nota[4])
        self.cofisDev = float(nota[5])

    def imprime (self):
        print(self.nf,self.serie,self.material,self.baseCalculo,self.pisDev,self.cofisDev)


      # self.nf
        # self.serie
        # self.material
        # self.baseCalculo
        # self.PisDev
        # self.CofisDev
        #
        # print(self.campo1)
        # print(self.campo2)
        # print(self.campo3)
        # print(self.campo4)

#
# tupla_personalizada.py
# class TuplaPersonalizada:
#     def __init__(self, *args):
#         self._tupla = tuple(args)
#
#     def __str__(self):
#         return str(self._tupla)
#
#     def get_element(self, index):
#         if 0 <= index < len(self._tupla):
#             return self._tupla[index]
#         else:
#             raise IndexError("Índice fora dos limites da tupla")
#
#
# Arquivo conjunto_de_tuplas.py:
#
# from tupla_personalizada import TuplaPersonalizada
#
# class ConjuntoDeTuplas:
#     def __init__(self):
#         self.tuplas = []
#
#     def adicionar_tupla(self, *args):
#         nova_tupla = TuplaPersonalizada(*args)
#         self.tuplas.append(nova_tupla)
#
#     def mostrar_tuplas(self):
#         for index, tupla in enumerate(self.tuplas, start=1):
#             print(f"Tupla {index}: {tupla}")
#
#
#
# Arquivo main.py:
# from conjunto_de_tuplas import ConjuntoDeTuplas
#
# # Criando uma instância da classe ConjuntoDeTuplas
# conjunto = ConjuntoDeTuplas()
#
# # Adicionando tuplas ao conjunto
# conjunto.adicionar_tupla(1, 2, 3)
# conjunto.adicionar_tupla("a", "b", "c")
# conjunto.adicionar_tupla(10, 20, 30, 40)
#
# # Mostrando as tuplas no conjunto
# conjunto.mostrar_tuplas()
#
#
