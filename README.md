# PROYECTO-PROGRAMACION
## Qué es Python?
Python es un lenguaje de información fácil de leer  y fácil de escribir, es un lenguaje multiparadigma se utiliza para desarrollar en diferente tipo de escenario , pero las personas se han enfocado en el desarrollo de: IOT, inteligencia artificial, backend, date science.
lo utilizamos por que es fácil, elegante, buenas practicas. 

# Qué es una variable?
una variable es como una caja que contiene información como (nombre, edad, numero de cedula, etc.)
el identificador de una variable no puede comenzar con un numero , debe estar en minúsculas  la palabra dentro del mismo se separa con guion bajo.  

## Nombrando una variable


- Elegir un nombre significativo que tenga relación con el dato que representará.

- Se debe mantener consistencia en el estilo a utilizar en nombres que contengan más de una palabra, por ejemplo:
```python
fecha_actual o fechaActual
```
-  El nombre de la variable se debe iniciar con una letra minúscula

- debe tener un máximo de 15 caracteres. 
```python
**forma incorrecta:**    1numero , Dia -1, Nombre. 
                    
**forma correcta:**      numero1 , dia_1, nombre.
 ```
 ## Asignando valores a una variable
 La creación de variables se realiza a través de la asignación de  un valor a la misma.
• El operador de asignación en Python es el ´´“=“'´´.

- la asignación de una variable  no se debe realizar de izquierda a derecha eso nos marcara error ejemplo:
```python
20 = x
```

- la asignación de una variable se debe realizar de  derecha a  izquierda ejemplo: (esta es la manera correcta)
```python
x = 20 
```
Una variable es un valor que puede cambiar a lo largo de la ejecución de nuestro algoritmo.

## diferente tipo de asignaciones
**Asignación en la misma línea:**
```python
x = 20 ; y = 10 ; z = 15
```
**• Asignación múltiple:**
```python
day, month, year = “miércoles”,”mayo”, 2016
```
**• Asignación del mismo valor:**
```python
largo = ancho = 5
```
**• Asignación de intercambio:**
```python
base = 30; altura = 40
base, altura = altura, base
```


## Operadores básicos
* suma ```(+)```
* resta ```(-)```
* multiplicacion ```(*)```
* division ```(/)```
* division euclidiana (cociente)```(//)```
* módulo ```(%)```
* potencia ```(** )```


### Suma
Para sumar en Python se utiliza el signo ´´+´´,  ejemplo :

ejemplo 1 
```python
suma= 25+ 3
print(suma)
[output] 28 
```

ejemplo 2 
```python
print('suma:', 25 + 30)
[output] 55
```

También, se puede sumar con variables:
ejemplo 1 
```python
X =20 ; y =30 
suma= x+y
print(suma)
[output] 50 
```
ejemplo 2
```python
altu=25; base=30 
suma= altu + base 
print(suma)
[output] 55
```
ingreso de valor por consola
```python
 num1=int(input("ingrese un numero:"))
 num2=int(input("ingrese un numero:"))
 sum1=num1+num2
 print(num1,'-',num2,'=',sum1)

```




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
palabra reselvada continue (salte hacia el siglo for)
y no se ejecute lo que esta adebajo del continue
j= 0 
for i in range (10):
    j += 2
    print('i:', i ,'j:',j )
    if j >= 2 and j<=18:
     continue
    print('el valor de j:', j )

cerrar entre ```[]```
