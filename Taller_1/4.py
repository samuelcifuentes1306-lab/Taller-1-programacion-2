def count_digits_for(numero):
    numero = abs(numero)
    contador = 0
    for _ in str(numero):
        contador += 1
    return contador


def count_digits_while(numero):
    numero = abs(numero)
    if numero == 0:
        return 1
    contador = 0
    while numero > 0:
        numero //= 10
        contador += 1
    return contador


numero = 123456
print(count_digits_for(numero))    
print(count_digits_while(numero))  