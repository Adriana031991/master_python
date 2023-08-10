# bucle for

var =  [ord(caracter) for caracter in 'variable']
print(var)

for letra, item in zip('variable', var):
    print(f'EL valor numerico de la letra {letra} es: {item}')
            

# tablas de multiplicar

numTabla = 3

for tabla in range(1,11):
    if numTabla == 0:
      
        print(f'\ntodo numero multiplicado por 0 da 0 \n')
        break
      
    print(f' {numTabla} X {tabla} = {numTabla * tabla}')
            
            
            
# for estrctura

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
  print(x)




# bucle while

contador = 1
while contador <= 6:
  print(f'\n estoy en el numero {contador}')
  contador += 1
  
  
num_user = int(input('cual es la tabla que quiere observar?: '))
contador1 = 1
while contador1 <= 10:
      print(f' {num_user} X {contador1} = {num_user * contador1}')
      contador1 += 1
      
else:
    print('tabla terminada')