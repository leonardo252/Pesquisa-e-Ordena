import matplotlib.pyplot as plt
from random import randint
import timeit

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    plt.plot(x,y, label = "Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

    
def geraLista(tam):
    lista = []
    while(len(lista) < tam):
        n = randint(1,2*tam)
        if n not in lista: lista.append(n)
    return lista

tam = [100,1000,10000,20000,30000,40000,50000,1000000]
time=[]

for i in tam:
    tempo =   timeit.timeit("geraLista({})".format(i),setup="from __main__ import geraLista",number=1)
    time.append(tempo)
    print(time)

print("Quantidade de numeros: ",tam)
print("Tempo: ", time)
desenhaGrafico(time, tam, "tempo", "Numeros Gerados")
