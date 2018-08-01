from random import randint
import timeit

'''
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
'''

def geraLista(tam):
    lista = []
    while(len(lista) < tam):
        n = randint(1,2*tam)
        if n not in lista: lista.append(n)
    return lista



tam = [100,1000,10000,20000,30000,40000,50000]
time=[]

tempo =   timeit.timeit("geraLista({})".format(tam),setup="from __main__ import geraLista",number=1)

lista = geraLista(100)
print(lista)
print("Tamanho: ", len(lista))
print("Quantidade de numeros: ",tam)
print("Tempo: ", tempo)
