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
• El operador de asignación en Python es el  ```“=“' ```.

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
También, se puede sumar con variables:
ejemplo 1 
```python
X =20 ; y =30 
suma= x+y
print(suma)
[output] 50 
```

### Resta
Para resta en Python se utiliza el signo ´´-´´,  donde se restan 2 numeros ejemplo :
ejemplo 1 
```python
resta= 70 -40  
print(resta )
[output] 30  
```

### Multiplicación
Operación aritmética que consiste en calcular el resultado (producto) de sumar un mismo número (multiplicando) tantas veces como indica otro número (multiplicador); se representa con los signos ´´**´´

ejemplo 1 
```python
multip = 70 *40  
print (multip)
[output] 2800 
```

### División
Python hace división de enteros cuando ambos operandos son enteros.El operador división el resultado que se devuelve es un número real.  se representa con los signos ´´/´´
ejemplo 1 
```python
div = 3 /2  
print (div)
[output] 1.5
```
### Módulo
el operador módulo no hace otra cosa que devolver el resto de la división entre los dos operandos.
e representa con los signos ´´%´´
ejemplo 1 
```python
m= 7 % 2
print(m)
[output] 1
```

# Tipos de datos en Python
* Numeros enteros
* Numeros de punto flotante
*  Texto (cadenas de caracteres)
*  Booleanos (Verdadero y falso)

## Integer
los numeros enteros son aquellos que no contiene decimales, pueden ser positivos o negativos ademas del cero.
 en programacion se lo conoce como int(interger, entero) o tipo long(de largo). la diferencia entre ambos es que long permite almacenar numeros mas grandes, pero ocupa mas espacio  es recomentable utilizarlo cuando sea solamente necesario.

 ejemplo:
 ```python
 x = 20 
 y = 3000
 z = -400
 ```
los números de Python están fuertemente relacionados con los números matemáticos, pero están sujetos a las limitaciones de la representación numérica en las computadoras.

Python distingue entre enteros, números de punto flotante y números complejos:
 ```python
 long= Números = Número entero en caso de overflow= 42L ó 456966786151987643L

int = Números = Número entero con precisión fija= 42
 ```

## Float
Los números reales son los que tienen decimales. En Python se expresan mediante el tipo float.
Un float en python es un tipo de variable que permite guardar numeros reales, a diferencia de un "int" (un int es tipo de variable que guarda números entero) este puede contener decimales, ejemplo de floats: 3.1415.

ejemplo:
```python
float =Números=	Coma flotante de doble precisión =	3.1415927
x = 40.5
y= 50.3
z = -3.6

```
la variable Float tambien se puede realizar con notacion cientifica, pero se debe colocar una<<e>> para indicar el valor de la potencia base 
```python
x = 40e4
y= 50e5
z = -35e7

real = 0.56e-3
print (real, type(real))
[output] 0.00056
 ```                        

## String
Las cadenas en python están entre comillas simples o comillas dobles.
```python
'hola' es lo mismo que "hola" .
```
## Casting en Python
  
Hacer un cast o casting  es la tecnica que  sirve para  convertir un tipo de dato a otro. 
```python
   int a str: str(45)
   str a int: int ("123")
   float a int: int (3.5)
```

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


