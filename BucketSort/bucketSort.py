import matplotlib.pyplot as plt
from random import randint
import timeit
import numpy as np
import scipy.interpolate as interpolate


def desenhaGraficoSuave(x,y,l,k,n, xl = "Nº de Elementos", yl = "Tempo(s)"):
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.subplot(n)
    plt.plot(xnew, suave(xnew), label="Curva Suave: "+k)
    #plt.plot(x,y, label="Curva Sem Suaveização: "+k)
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

def bucketSort(vetor):
    maior = max(vetor)
    comprimento = len(vetor)
    tamanho = maior/comprimento
 
    buckets = [[] for _ in range(comprimento)]
    for i in range(comprimento):
        j = int(vetor[i]/tamanho)
        if j != comprimento:
            buckets[j].append(vetor[i])
        else:
            buckets[comprimento - 1].append(vetor[i])
 
    for i in range(comprimento):
        insertionSort(buckets[i])
 
    result = []
    for i in range(comprimento):
        result = result + buckets[i]
 
    return result

def insertionSort(vector):
    for i in range(1, len(vector)):
        valor_atual = vector[i]
        posi = i

        while(posi>0 and vector[posi-1]>valor_atual):
            vector[posi] = vector[posi-1]
            posi = posi-1

        vector[posi] = valor_atual

    return(vector)


numsT = [1000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

def casoMedio(nums0):
    nums = nums0
    time = []
    for r in nums:
        print(r)
        vector = geraLista(r)
        tempo = timeit.timeit("bucketSort({})".format(vector),setup="from __main__ import bucketSort",number=1)
        time.append(tempo)

    desenhaGraficoSuave(nums, time,'Bucket Sort', "Caso Medio",111, "Nº de Elementos", "Tempo(s)")

def piorCaso(nums1):
    nums=nums1
    time1=[]
    for r in nums:
        print (r)
        vector1 = listaDecrescente(r)
        tempo = timeit.timeit("bucketSort({})".format(vector1),setup="from __main__ import bucketSort",number=1)
        time1.append(tempo)

    desenhaGraficoSuave(nums, time1, 'Bucket Sort', "Pior Caso",111, "Nº de Elementos", "Tempo(s)")

def melhorCaso(nums2):
    nums=nums2
    time2=[]
    for r in nums:
        print (r)
        vector1 = listaCrescente(r)
        tempo = timeit.timeit("bucketSort({})".format(vector1),setup="from __main__ import bucketSort",number=1)
        time2.append(tempo)

    desenhaGraficoSuave(nums, time2, 'Bucket Sort', "Melhor Caso",111, "Nº de Elementos", "Tempo(s)")


casoMedio(numsT)
piorCaso(numsT)
melhorCaso(numsT)
plt.show()
