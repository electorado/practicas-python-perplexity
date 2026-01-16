nums =[]
suma = 0
print("Ingresa 5 números que quieras sumar")
for i in range (5):
    num = int(input(f"Número {i+1}: "))
    nums.append(num)
    suma += num
print(f"La suma de tus números es {suma}")

mayor = 0
menor = 0

for num in nums:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
print(f"El número mayor es {mayor} y el número menor es {menor}")

lista = [30, 33, 25, 42, 66, 31, 68, 99, 82, 21, 22, 66]
pares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
print(pares)

notas = [3.99, 5.8, 9, 9]
suma = 0
aprobado = ""
for i in notas:
    suma += i
if (suma/len(notas)) > 5:
    aprobado = ", has aprobado."
else:
    aprobado = ", has suspendido."
print(f"Tu nota media es: {suma/len(notas)}{aprobado}")

lenguajes = ["python", "java", "sql", "bash", "CSS", "JS"]
lenguaje = input("En qué lenguaje sueles programar? ")

if lenguaje.casefold() in lenguajes:
    print(f"Nosotros utilizamos {lenguaje}")
else:
    print(f"Nosotros no utilizamos {lenguaje}")