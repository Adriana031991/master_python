# print('######### primero ######')

# pais = 'colombia'.capitalize() #str
# continente = 'america'.capitalize() #str

# print(f' el pais {pais} está en el continente {continente}')

# print('######### segundo ######')
# imprimir numeros pares

# opt1
# for x in range(0, 121, 2):
#  print(x)

# opt2
# contador = 1
# while contador <=120:
#     res = contador % 2 == 0
#     if res :
#         print(contador)
#     contador += 1


# print('######### tercero ######')

# imprimir los cuadrados de los primeros 60 numeros

# contador = 1
# while contador <= 60:
#     a = contador*contador
#     print(a)
#     contador += 1

# for item in range(0,61):
#     b = item*item
#     print(b)


# print('######### cuarto ######')

# pedir dos numeros al usuario y hacer todas las operaciones matematicas

# num = int(input("\ningrese el primer numero: "))
# num1 = int(input("ingrese el segundo numero: "))


# suma = num + num1
# resta = num - num1
# multi = num * num1
# div = num / num1
# mod = num % num1
# print("\n·········· Calculadora···················\n")
# print(f"la suma entre {num} y {num1} es: {suma}")
# print(f"la resta entre {num} y {num1} es: {resta}")
# print(f"la multiplicacion entre {num} y {num1} es: {multi}")
# print(f"la division entre {num} y {num1} es: {div}")
# print(f"la modulo entre {num} y {num1} es: {mod}")


# print('######### Quinto ######')

# programa que muestre todos los numeros entre dos que se le solicite al usuario

# num2 = int(input("\ningrese el primer numero: "))
# num3 = int(input("ingrese el segundo numero: "))

# if num3 > num2:
#     for item in range(num2, num3 + 1, 1):
#         print(item)

# else:
#     for item in range(num3, num2 + 1, 1):
#         print(item)


# print('######### Sexto ######')

# todas las tablas de multiplicar


# contador1 = 1
# while contador1 <= 10:
#     for item in range(1, 11):
#         print(f"················Tabla del {contador1} ··················")
#         for itemT in range(1, 11):
#             print(f" {itemT} X {contador1} = {itemT * contador1}")
#         else:
#             print("tabla terminada")
#         contador1 += 1


# print('######### Septimo ######')
# mostrar numeros impares entre dos numeros dados por el usuario

# num4 = int(input("\ningrese el primer numero: "))
# num5 = int(input("ingrese el segundo numero: "))


# if num5 > num4:
#     for item in range(num4, num5 + 1):
#         if item % 2 == 1:
#             print(f"El numero impar es: {item}")

# else:
#     for item in reversed(range(num5 - 1, num4 + 1)):
#         if item % 2 == 1:
#             print(f"El numero impar es: {item}")


# print('######### Octavo ######')

# cual es el x porciento de x numero

# num6 = int(input("\ningrese el primer numero: "))
# num7 = int(input("ingrese el porcentaje a calcular: "))

# value = num6 * (num7 / 100)
# print(f"el porcentaje de {num6} es: {value}%.")

# print('######### Noveno ######')

# pedir al usuario indefinidamente e imprimir ese numero hasta que se escirba 111

# while True:
#     num8 = int(input("\ningrese el numero: "))
#     print(num8)
#     if num8 != 111:
#         continue
#     else:
#         print(f"el numero {num8} es correcto ")
#         break

# print('######### Decimo ######')

# pide 15 notas a usuario y sacar en pantalla cuantos han aprobado y cuantos han perdido

notas = []
aprobados = 0
perdidos = 0

numAlum = int(input("\ningrese la cantidad de alumnos: "))

for item in range(1, numAlum + 1):
    nota = float(input(f"\ningrese la nota del estudiante numero {item}: "))
    notas.append(nota)


for x in notas:
    if x >= 5:
        aprobados += 1

    else:
        perdidos += 1

print(f"\n{aprobados} estudiantes aprobaron y {perdidos} estudiantes perdieron")
