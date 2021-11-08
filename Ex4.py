def bubbleSort(lista):
    for contor in range(len(lista)-1,0,-1):
        for i in range(contor):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = [5,12,3,18,45,78,23,21,32]
bubbleSort(lista)
print(lista)