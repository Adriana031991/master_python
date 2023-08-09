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

print('\n####### EJERCICIO 3 ########\n')

name = input('escriba un nombre ')
edad = int(input('escriba una edad '))
residencia = input('escriba el pais de residencia ')
mayoria_edad = 18

if residencia != 'Colombia':
     print(f"{name} no es colombiano")

else:
    print(f"{name} es colombiano")
    
    if edad >= mayoria_edad:
        print(f"{name} es mayor de edad")
        
    else:
        print(f"{name} No es mayor de edad")
      

