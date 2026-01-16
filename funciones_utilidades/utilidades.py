def pedir_numeros(n):
    nums = []
    for i in range(n):
        num = float(input(f"Número {i+1}: "))
        nums.append(num)
    return nums

def max_min(lista):
    mayor = lista[0]
    menor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    return mayor, menor

def media(lista):
    suma = 0
    for nota in lista:
        suma += nota
    media = suma / len(lista)

    if media >= 5:
        mensaje = ", has aprobado"
    else:
        mensaje = ", has suspendido"
    return media, mensaje