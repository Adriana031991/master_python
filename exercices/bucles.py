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