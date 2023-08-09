title = 'title of this excercise'

num = 90
num1 = 9.0
num2 = -9.0

boolean = True

char = 'a'

title = 'second title of this excercise'

num = 190
num1 = 19.0
num2 = -19.0

boolean = False

char = 'g'

lista = [11,22,33,44]
listaStr = ['a', 22, 'aa']
tuplaNoCambia = ('hola', 33, 'tt')
diccionario = {"name": "victor", 'apellido': 'julio', 'curso': 90}
rango = range(20)


print(title, 'type ->' ,type(title))
print(num, 'type ->' ,type(num))
print(num1, 'type ->' ,type(num1))
print(num2, 'type ->' ,type(num2))
print(boolean, 'type ->' ,type(boolean))
print(char, 'type ->' ,type(char))

print('--------------------------')

print(lista, 'type ->' ,type(lista))
print(listaStr, 'type ->' ,type(listaStr))
print(tuplaNoCambia, 'type ->' ,type(tuplaNoCambia))
print(diccionario, 'type ->' ,type(diccionario))
print(rango, 'type ->' ,type(rango))

# concatenacion

print('--------------------------')

name = 'adriana'
lastname = 'franklin'

print(f"{name} {lastname}"  )
print("Hola soy {} {}".format(name, lastname))
print(name + ' ' + lastname)

print(f"")


print('\n-------CASTEO------------\n')

number = int('123')
# no se puede castear una cadena de texto que no sea numeros
print(number, ' type -> ' ,type(number))

number1 = float('123')
# no se puede castear una cadena de texto que no sea numeros
print(number1, ' type -> ' ,type(number1))


print('\n-----OPERADORES MATEMATICOS--------------\n')

suma = num + num1
resta = num - num1
multi = num * num1
div = num / num1
mod = num % num1

print(f"la suma entre {num} y {num1} es: {suma}")
print(f"la resta entre {num} y {num1} es: {resta}")
print(f"la multiplicacion entre {num} y {num1} es: {multi}")
print(f"la division entre {num} y {num1} es: {div}")
print(f"la modulo entre {num} y {num1} es: {mod}")


print('\n-----OPERADORES INCREMENTO Y DECREMENTO--------------\n')

num +=20
num1 -= 30
num2 /= 2

print(num)
print(num1)
print(num2)
num %= 5
print(num)