import matplotlib.pyplot as plt
def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    plt.plot(x,y, label = "Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()  
       
x = [1,2,3,4,5,6,7,8,9,10]
y = list(map(lambda z: z**2, x))
desenhaGrafico(x,y)
