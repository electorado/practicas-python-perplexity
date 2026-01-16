from utilidades import pedir_numeros, max_min, media

n = int(input("¿Con cuántas notas vas a trabajar? : "))
lista = pedir_numeros(n)

mayor, menor = max_min(lista)
print(f"Tu nota mayor es {mayor} y la menor {menor}")

media, mensaje = media(lista)
print(f"Tu nota media es: {media:.2f}{mensaje}")

