# for i in range(11):
#     print(i)

#n_suma = int(input("Dame un número "))
# suma = 0
#for i in range(n_suma+1):
#     suma += i
# print (suma)

# n_mult = int(input("Dame un número "))
# multiplicacion = 1
# for i in range(n_mult+1):
#     multiplicacion = i * n_mult
#     print(f"{i} por {n_mult} es {multiplicacion}")

# secreto = 7
# num_adivinado = int(input("Dame un número "))
#
# while num_adivinado != secreto:
#     if num_adivinado > secreto:
#         print("Más bajo")
#         num_adivinado = int(input("Dame un número "))
#     elif num_adivinado < secreto:
#         print("más alto")
#         num_adivinado = int(input("Dame un número "))
# else:
#     print("Adivinaste")

num_menguante = int(input("Dame un número "))
for i in range (num_menguante,0,-1):
    print(i)
