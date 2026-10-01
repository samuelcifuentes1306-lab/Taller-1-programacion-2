def reverse_string_for(cadena):
    resultado = ""
    for caracter in cadena:
        resultado = caracter + resultado  # lo pega ADELANTE, no atrás
    return resultado


def reverse_string_while(cadena):
    resultado = ""
    i = len(cadena) - 1
    while i >= 0:
        resultado += cadena[i]
        i -= 1
    return resultado
cadena = "recursividad"
print (reverse_string_for(cadena))