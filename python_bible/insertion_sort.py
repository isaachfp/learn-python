#Algoritmo de ordenação por inserção
#vetor = [10,7,35,20,50,13,27]
vetor = [50,35,27,20,13,10,7]
print(vetor)
num_elem = len(vetor)
j = 1
while j < num_elem:
	chave = vetor[j]
	i = j-1
#	print(i,chave)
	while (i >= 0 and vetor[i] > chave):
		vetor[i+1] = vetor[i]
		i = i-1
	vetor[i+1] = chave
	j +=1
print(vetor)
#	print(j)	
#	print()
