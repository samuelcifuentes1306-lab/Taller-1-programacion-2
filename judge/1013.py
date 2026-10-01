linea = input().split()
a = int(linea[0])
b = int(linea[1])
c = int(linea[2])

def mayor(a,b): 
    return (a+b+abs(a-b))/2
print(mayor(mayor(a,b),c),"eh o maoir")