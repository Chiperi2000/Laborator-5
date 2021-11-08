lista = [3, 2, 8, 4, 3, 4, 5, 1, 2, 1]
lista_noua = [] 

for i in lista:
    if i not in lista_noua: 
        lista_noua.append(i) 
lista = lista_noua 

print("Acesta este elementul unic:")
print(lista_noua)
