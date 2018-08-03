import matplotlib.pyplot as plt
from random import randint
import timeit
import numpy as np
import scipy.interpolate as interpolate
from threading import Thread

def desenhaGraficoSuave(x,y,l, n, xl = "Nº de Elementos", yl = "Tempo(s)"):
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.subplot(n)
    plt.plot(xnew, suave(xnew), label="Curva Suave")
    plt.plot(x,y, label="Curva Sem Suaveização")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title(l, fontsize=12)
    

def geraLista(tam):
    lista = []
    while(len(lista) < tam):
        n = randint(1,100)
        lista.append(n)
        #if n not in lista: lista.append(n)
    return lista

def listaCrescente(tam):
    lista = []
    for i in range(tam):
        lista.append(i+1)
    return lista

def listaDecrescente(tam):
    lista =[]
    while (tam > 0):
        lista.append(tam)
        tam = tam-1
    return lista

def ordena(vector):
    tam = len(vector)
    while(tam > 1):
        troca = False
        x = 0
        while(x < (tam-1)):
            if(vector[x] > vector[x+1]):
                troca = True
                aux= vector[x]
                vector[x] = vector[x+1]
                vector[x+1] = aux
            x +=1
        if not troca:
            break
        tam -= 1

    return vector

nums = [1000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
#nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def casoMedio(nums1):
	nums = nums1
	time = []
	for r in nums:
	    print(r)
	    vector = geraLista(r)
	    tempo = timeit.timeit("ordena({})".format(vector),setup="from __main__ import ordena",number=1)
	    time.append(tempo)

	desenhaGraficoSuave(nums, time,'Caso Medio',211, "Nº de Elementos", "Tempo(s)")

def piorCaso(nums1):
	nums=nums1
	time1=[]
	for r in nums:
		print (r)
		vector1 = listaDecrescente(r)
		tempo = timeit.timeit("ordena({})".format(vector1),setup="from __main__ import ordena",number=1)
		time1.append(tempo)

	desenhaGraficoSuave(nums, time1, 'Pior Caso',212, "Nº de Elementos", "Tempo(s)")

'''
if __name__ == '__main__':

	ordena1 = Thread(target=casoMedio,args=[nums])
	ordena2 = Thread(target=piorCaso,args=[nums])

	ordena1.start()
	ordena2.start()

	plt.show()
'''
casoMedio(nums)
piorCaso(nums)

plt.show()
#print(tempo)

#print(ordena(vector))
