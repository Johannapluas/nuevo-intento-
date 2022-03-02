# fundamentos de programacion -
# Qué es Python?
 Python es un lenguaje de información fácil de leer  y fácil de escribir, es un lenguaje multiparadigma se utiliza para desarrollar en diferente tipo de escenario , pero las personas se an enfocado en el desarrollo de: IOT, inteligencia artificial, backend, date science.
lo utilizamos por que es fácil, elegante, buenas practicas. 

# Qué es una variable?
una variable es como una caja que contiene información como (nombre, edad, numero de cedula, etc.)
el identificador de una variable no puede comenzar con un numero y debe estar en minúsculas  la palabra dentro del mismo se separa con guion bajo.  

## Nombrando una variable

- Elegir un nombre significativo que tenga relación con el dato que representará.

- Se debe mantener consistencia en el estilo a utilizar en nombres que contengan más de una palabra, por ejemplo:
fecha_actual o fechaActual

-  El nombre de la variable se debe iniciar con una letra minúscula

- debe tener un máximo de 15 caracteres. 

**forma incorrecta:**    1numero , Dia -1, Nombre. 
                    
**forma correcta:**      numero1 , dia_1, nombre.
 
                                  

## Asignando valores a una variable
 La creación de variables se realiza a través de la asignación de  un valor a la misma.
• El operador de asignación en Python es el “=“.

- la asignación de una variable  no se debe realizar de izquierda a derecha eso nos marcara error ejemplo:

20 = x

- la asignación de una variable se debe realizar de  derecha a  izquierda ejemplo: (esta es la manera correcta)
x = 20 

Una variable es un valor que puede cambiar a lo largo de la ejecución de nuestro algoritmo.

'''python 
print('Hola mundo')

x = 100

print(x)
'''

## diferente tipo de asignaciones
**Asignación en la misma línea:**
x = 20 ; y = 10 ; z = 15
**• Asignación múltiple:**
day, month, year = “miércoles”,”mayo”, 2016
**• Asignación del mismo valor:**
largo = ancho = 5
**• Asignación de intercambio:**
base = 30; altura = 40
base, altura = altura, base

# Asignaciones en la misma línea
x = 12; y =10; z=4

print('x:', x)
print(y)
print(z)

print('x=', x, 'y=', y, 'z=',z)


# Asignación múltiple
dia, mes, anho = "Lunes", "Mayo", 2022
print(dia, mes, anho)

print('Hoy es', dia)
print(', el mes actual es', mes)
print('y el año es', anho)

print('Hoy es', dia, ', el mes actual es', mes, 'y el año es', anho)

# 'Hoy es Martes, el mes actual es Diciembre y el año es 2021'

# Asignación del mismo valor
var1 = var2 = 10

# Asignación de intercambio
base = 10; altura = 100
base, altura = altura, base

print('base: ', base)
print('altura: ', altura)

## Operadores básicos


### Suma

### Resta

### Multiplicación

### División

### Módulo

# Tipos de datos en Python

## Integer

## Float

## String

## Casting en Python

a = 1   # <class 'int'>
b = 2.3 # <class 'float'>

a = a + b
print(a)       # 3.3
print(type(a)) # <class 'float'>

## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
# palabra reselvada continue (salte hacia el siglo for)
# y no se ejecute lo que esta adebajo del continue
j= 0 
for i in range (10):
    j += 2
    print('i:', i ,'j:',j )
    if j >= 2 and j<=18:
     continue
    print('el valor de j:', j )


