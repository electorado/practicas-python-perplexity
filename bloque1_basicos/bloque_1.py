nombre = input("Cómo te llamas? ")
print(f"Hola {nombre}")

x = int(input("dame un número"))
y = int(input("cuánto quieres sumarle"))
print(f"la suma de {x} y {y} es {x+y}")

paroimpar = int(input("Escribe un número "))
if paroimpar % 2 == 0:
    print(f"{paroimpar} es par")
else:
    print(f"{paroimpar} es impar")

num1 = int(input("dame un número "))
num2 = int(input("dame otro "))
if num1 < num2:
    print(f"{num1} es menor que {num2}")
elif num2 < num1:
    print(f"{num2} es menor que {num1}")
elif num1 == num2:
    print(f"{num1} es igual a {num2}")

edad = int(input("Qué edad tienes? "))
if edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")