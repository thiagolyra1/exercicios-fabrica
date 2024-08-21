def unique_list(lista):
    x = []
    for numero in lista:
        if numero not in x:
            x.append(numero)
    return x
    
print(unique_list([1,2,2,2,2,2,3,3,3,3,44,55,6,7,8,8,90,10,10]))

lista2 = [1,2,2,2,2,2,3,3,3,3,44,55,6,7,8,8,90,10,10]

listaunica = set(lista2)

print()
print(listaunica)
