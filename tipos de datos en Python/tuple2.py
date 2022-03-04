ejemplo = input("Introduce una muestra de números separados por comas: ")
ejemplo = ejemplo.split(',')
n = len(ejemplo)
for i in range(n):
    ejemplo[i] = int(ejemplo[i])
ejemplo = tuple(ejemplo)
sum = 0
sumsq = 0
for i in ejemplo:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean*2)*(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)