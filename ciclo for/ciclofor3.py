import sys
n= 5 
suma= 0 
menor= sys.maxsize

for i in range(n):
    num= int(input('ingrese un numero:'))
    suma += num 
    if num< menor:
        menor = num 
print('promedio:', suma/n )
print(('menor:', menor))
    
    