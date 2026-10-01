def multiply_for(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado


def multiply_while(a, b):
    resultado = 0
    contador = 0
    while contador < b:
        resultado += a
        contador += 1
    return resultado

print (multiply_for(6, 4))
print (multiply_while(6, 4))