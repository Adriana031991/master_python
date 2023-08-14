# print("·······Ejercicio 1··········")

# def tablaMultiplicar(numero):
#     numero = int(numero)
#     contador1 = 1
#     while contador1 <= 10:
#         print(f" {numero} X {contador1} = {numero * contador1}")
#         contador1 += 1

#     else:
#         print("tabla terminada")
#         print("······························\n")


# numero = input("cual es la tabla que quiere observar?: ")
# if numero == "":
#     numero = 0

# tablaMultiplicar(numero)


# print("\n·······Ejercicio 2··········")

# def funcionConParametroOpcional(param1, param2=None):
#     print(param1)
#     if param2 != None:
#         print(param2)


# funcionConParametroOpcional("Hola")


print("\n·······Ejercicio 3··········")


def operacionesMatematicas(numA, numB, operador):
    operadores = ["suma", "resta", "multiplica", "divide"]

    if numA != 0 and numB != 0:
        return {
            "suma": print(f"\nla suma entre {numA} y {numB} es: {numA+numB}"),
            "resta": print(f"\nla resta entre {numA} y {numB} es: {numA-numB}"),
            "multiplica": print(
                f"la multiplicacion entre {numA} y {numB} es: {numA*numB}"
            ),
            "divide": print(f"la division entre {numA} y {numB} es: {numA/numB}"),
        }.get(
            operador,
            print(
                f"El operador {operador} no esta en el siguiente listado: {operadores}."
            ),
        )

    else:
        print(
            f"El usuario no ha ingresado los numeros para realizar los calculos basicos."
        )


num = input("\ningrese el primer numero: ")
num1 = input("ingrese el segundo numero: ")
operador = input("por favor escriba: suma, resta , multiplica, ó divide ")

if num != "":
    numA = int(num)
if num1 != "":
    numB = int(num1)
else:
    numA = 0
    numB = 0


operacionesMatematicas(numA, numB, operador)
