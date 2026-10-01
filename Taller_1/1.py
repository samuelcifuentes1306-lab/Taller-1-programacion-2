def count_ocurrences_for(lista, numero):
    apariciones = 0
    for elemento in lista:
        if numero == elemento: apariciones +=1
    return apariciones 

def count_ocurrences_while(lista, numero):
    contador = 0
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            contador += 1
        i += 1
    return contador

lista = [1, 2, 3, 4, 3, 3, 5]
numero = 3 
print(count_ocurrences_for(lista, numero))
print(count_ocurrences_while(lista, numero))