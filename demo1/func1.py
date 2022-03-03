def par_impar(n):
 if n%2 == 0:
    print(n, 'es par')
 else:
    print(n,'es impar')
    
par_impar(10)
par_impar(5)
par_impar(30)


def suma(a, b):
    return a + b



def es_bisiesto(anho):
    if anho%4 == 0 and anho%100 != 0 or anho%400 == 0:
        return True
    else:
        return False


def par_impar(n):
    if n%2 == 0:
        print(n,'es par')
    else:
        print(n,'es par')

par_impar(2)
par_impar(7)
par_impar(16)
par_impar(6)


result= es_bisiesto(2003)
print(result)
print(es_bisiesto(2003))


val1= suma(4, 9)
print(val1)