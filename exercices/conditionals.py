# ejemplo 1
print('\n####### EJERCICIO 1 ########\n')

color = input('adivina cual es el color de la encuesta ')

if color != 'blue':
    print(f"El color es incorrecto")
else :
    print(f"Correcto el color es: {color}")
    
    
print('\n####### EJERCICIO 2 ########\n')

year = int(input('En que año estamos '))

if year >= 2021:
    print(f"\nEl año es mayor a 2021")
else:
    print(f"\nEl año es menor a 2021")
