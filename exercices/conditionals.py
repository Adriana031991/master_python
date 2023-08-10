# ejemplo 1
# print('\n####### EJERCICIO 1 ########\n')

# color = input('adivina cual es el color de la encuesta ')

# if color != 'blue':
#     print(f"El color es incorrecto")
# else :
#     print(f"Correcto el color es: {color}")
    
    
# print('\n####### EJERCICIO 2 ########\n')

# year = int(input('En que año estamos '))

# if year >= 2021:
#     print(f"\nEl año es mayor a 2021")
# else:
#     print(f"\nEl año es menor a 2021")

# print('\n####### EJERCICIO 3 ########\n')

# name = input('escriba un nombre ')
# edad = int(input('escriba una edad '))
# residencia = input('escriba el pais de residencia ')
# mayoria_edad = 18

# if residencia != 'Colombia':
#      print(f"{name} no es colombiano")

# else:
#     print(f"{name} es colombiano")
    
#     if edad >= mayoria_edad:
#         print(f"{name} es mayor de edad")
        
#     else:
#         print(f"{name} No es mayor de edad")
      


print('\n####### EJERCICIO 4 ########\n')

diasSemana = {1:'lunes', 2:'martes', 3:'miercoles', 4:'jueves', 5:'viernes', 6:'sabado', 7:'domingo'}
dia = int(input('escriba un numero \n'))

if dia ==1:
   print(f"El dia de la semana es lunes")
elif dia ==2:
   print(f"El dia de la semana es martes")
elif dia ==3:
   print(f"El dia de la semana es miercoles")
elif dia ==4:
   print(f"El dia de la semana es jueves")
elif dia ==5:
   print(f"El dia de la semana es viernes")
else:
   print(f"Es fin de semana")



print('\n####### EJERCICIO 5 ########\n')

diasSemana = {1:'lunes', 2:'martes', 3:'miercoles', 4:'jueves', 5:'viernes', 6:'sabado', 7:'domingo'}
number = int(input('escriba un numero \n'))

for key, value in diasSemana.items():
    if number == key:
        print(f"El dia de la semana es {value}")


