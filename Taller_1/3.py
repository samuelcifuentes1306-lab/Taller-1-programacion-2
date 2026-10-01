def is_sorted_for(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True




def is_sorted_while(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            return False
        i += 1
    return True

lista = [1, 2, 3, 4, 5]
lista2 = [1, 3, 2, 4, 5]
print (is_sorted_for(lista))
print (is_sorted_for(lista2))
print (is_sorted_while(lista))
print (is_sorted_while(lista2))