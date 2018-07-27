from random import randint

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        lista.append(n)
        #if n not in lista: lista.append(n)
    	
    return lista

def ordena(vector = []):
	print('O vector inicial: ', end='')
	for i in vector:
		print(i, end=' ')
	print("\n")

	tam = len(vector)
	print("Tamanho do vetor: %d" % (tam))

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

	print('O vector reordenado: ', end='')
	for i in vector:
		print(i, end=' ')
	print("\n")

if __name__ == '__main__':
	vector = geraLista(10000)
	ordena(vector)