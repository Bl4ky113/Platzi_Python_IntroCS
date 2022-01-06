# Python. Pesanmiento Computacional

## Objetivos del Curso
- Aprender a resolver los problemas de manera computancional
- Entender los puntos comunes entre los lenguajes de programación
- Desarrollar Bases para una carrera de CS

## El Computo

El computo viene de las computadoras.

Los primeros computadores fueron menos que mecanicos, empezando por calculos manuales a punta de pluma y papel.
Despues con el telar de Jacquar, empezamos a ver las intrucciones almacenadas en "punch cards"¿
El Motor Analitico de Babbage, fue en pocas palabras un abaco mejoradisimo, repartiendo el proceso y la información del programa,
dando luz a el primer lenguaje de programación.

En resumen, la historia de las comutadoras, y que computo es realizar varias operaciones matematicas, nada dificil.

## Intro a Lenguajes de Programación

### Conocimientos:
- Declarativo:
	Es la conocimiento de relaciones entre diferentes variables, ejemplo:
		x = 1
		se declara que x tiene una relación de valor con 1.

- Imperativo:
	Es el conocimiento que nos lleva a un resultado, siendo la base de los algoritmos.

- Algoritmos:
	Son la lista finita de pasos, que toman unas entradas, para al final dar una salida.

Los lenguajes de programación son para los humanos, para despues traducirlos y pasarlos a el computador.
Y estos deben ser Turing Completeness, es decir que pudean hacer cualquier algoritmo del pasado o inclusive 
del futuro, haciendo uso de comandos o herramientas primitivas.

Ademas de esto, tambien los lenguajes tienen 3 principales componentes:

1. Sintaxis:
	Define si la secuencia de caracteres correcta
2. Semántica Estatica: 
	Define que enunciados con sintaxis correcta tienen significado
3. Semántica:
	Define el significado de lo escrito. Teniendo solo un significado.

## Lenguajes de Programación
Se pueden diferencias entre diferentes categorias:
	- Bajo / Alto nivel
		Dependiendo de la claridad y forma de escribirlo varia el nivel, siendo alto casí hablar o escribir normalmente, mientras que 
		bajo es llegar a casí el nivel de la máquina, código binario.

	- General / Dominio Especifico
		Los generales son lenguajes que nos van a permitir hacer variadas cosas al usarlo, mientras que los de dominio especifico, solo 
		en enfocan en un sector
	- Interpretado / Copilado
		Los interpretados son los que la maquina va interpretando el código al pasar las acciones, mientras que el copilado nos hace
		traducirlo completamente a el lenguaje de la máquina.

Python es un lenguaje de programación de Alto Nivel, General y Interpretado

Python cuenta con objLiterales los cuales pueden ser valores sencillos cómo
	- ints
	- bools
	- float
	- str

Y operadores para interactuar con estos objs
	- +, -, /, *
	- **, %
	- =, ==, !=, >, <, >=, <=
	- entre otros

El orden para usarlos es:
	objLit operador objLit

El faltar esta regla nos dara un error de sintaxis y el poner algo ilogico, cómo dividir un str por un bool, nos va a dar 
un error de semantica estatica.

Me voy a saltar un poco de las notas, porqué estan muy básicas :c. Pase todo un módulo, pero esto suena interesante.

## Enueración Exaustiva
Algunas veces vamos a tener que mirar a varias opciones para resolver un problema, afortunadamente con las computadoras, 
podemos realizar de una forma rapida miles de operaciones en segundos. Dandonos una gran ventaja.

Para aprovecharla, deberiamos usarla para hacer diferentes operaciones sencillas o no muy complejas a grandes proporciones.

Sin embargo al hacer algo muy rapido perdemos mucha de la presición. Entonces debemos encontrar un rango donde estemos con la respuesta 
indicada, pero sin demorarnos mucho tiempo.

## Aproximación de Soluciones
Para aproximar las soluciones que requieran de un alto procesamiento y velocidad, debemos tener un rango de aceptación o de verificación de nuestros
resultados. Este rango se va a llamar Epsilon. Al determinar Epsilon, generalmente una medida de 2 o más decimales. 0.001. Vamos a 
calcular cada incremento de un valor, potenciandolo a la segunda potencia. Para que así al hacer varias operaciones no se pase de epsilon.

## Búsqueda Binaria
Ya tenemos una forma rápida, pero que no nos da una respuesta en el error o la aproximación. Una forma medio para dar con la aproximación y 
ahora tenemos una forma RAPIDISIMA para hacer un algoritmo que tenga una secuencia constante.

Es decir, los números naturales son constantes porque el 1 va antes del 2, el 2 antes del 3, y así. Teniendo una secuencia de suma de 1 en 1 constante. 

Esto nos va a permitir que al buscar por ejemplo una raiz cuadrada, tengamos mucha más precisión si hacemos una busqueda binaria de Metodo Númerico de bisección. Es decir, vamos a tomar el grupo de números desde 0 hasta el objetivo, ejemplo: 7.

Vamos a determinar un Epsilon, o rango aceptable de nuestros resultados. Un punto bajo, generalmente 0, y un punto alto, que va a ser el mismo 
objetivo. Vamos a realizar una respuesta que va a ser la mitad de estos puntos:

(punto_bajo + punto_alto) / 2 = (0 + 7) / 2 = 3.5

Ahí hemos hecho una bisection o haber partido a la mitad los datos. Vamos a meternos en un loop donde vamos a verificar si la mitad de esos datos,
en este caso 3.5, cuando se potencia a el cuadrado y la diferencia entre ese y el objetivo es igual o mayor a epsilon. Si si nos da el resultado 
deseado, ahora buena, tenemos nuestro resultado final. Sin embargo esto casí nunca va a pasar, por lo tanto vamos a hacer el mismo proceso de bisectar.

Pero hay otro problema, tenemos dos piezas, y para no gastar recursos, cual de las dos deberiamos bisectar? Sencillo. Si la respuesta anterior 
es menor que el objetivo, vamos a tomarlo cómo el punto bajo, es decir hemos elegido la parte mayor. Si es a el contrario, respuesta mayor a el 
objetivo, vamos a tomar esa respuesta como el nuevo punto alto, es decir hemos elegido la parte menor. 

Y apartir de elegir esa mitad, ya sea la menor o la mayor, vamos a bisectarla otra vez hasta obtener el resultado deseado.

Cumpliendo así la funcion de un loop. Pero mucho más optimizado.

## Functions y Abstracción

### Abstracción
Es la forma en la que nosotros debemos aprender a usar algo, pero no necesitamos exactamente saber cómo funciona internamente para hacer de su uso.
Ejemplo los módulos, librerias de codigo. O cosas más comunes cómo los electrodomesticos, vehiculos, entre otros.

### Decomposición
Es la forma en la que vamos a dividir en pequeñas partes a nuestro código, haciendolo más compacto y evitar repetirnos usando herramientas cómo
las functions.

Una explicación sencilla de que es una function y sus partes e propiedades.

## Scope 
El alcance o Scope es el alcance que tienen los objetos de python, ya sean classes, functions, variables, entre otros.
El scope global es el scope que siempre va a estar disponible, cómo las librerias importadas o variables globales.
Generalmente entre modulos, cómo las clases y las functions, no se pueden usar objectos fuera del scope, ademas de los globales.
Entre más "profundo" bloques de código se declare un objeto, no va a poder ser usado en otros bloques exteriores.

## Documentación
Siempre que vamos a hacer una function, deberiamos documentar su funcion de forma resumida, explicar que son cada parametro recibido y cual va a serel uso, y difinir que es y que va a ser el return de la function.

Esto se hace para que los demás devs puedan leer de una mejor forma nuestro código, si queremos leer la documentación de una function, podemos hacer
uso de help(function). 

Estos comentarios se deben hacer con triple comillas dobles. """   """

## Recursividad
El concepto de recursividad es aquel de una function que para realizar su función debe llamarse a si misma otra vez. Pasando otros parametros, 
generalmente modificados dentro de la misma function. Un ejemplo de esto es la secuencia fibonnacci. Que tiene la siguiente formula:

n = (n - 1) + (n - 2)

o un resultado factorial:

n! = n * (n - 1)!

En ambos vamos a tener que realizar varias veces una operación o función con diferentes valores hasta dar con el resultado. 
Ademas de la función, debemos agregar alguna forma para parar la recurción, ya que nos puede dar un error si la funtion se llama muchas veces 
a sí misma, por ahí más de 900 veces. 

## Test de Black Box
La caja negra es el concepto de lo desconocido, principalmente una function que no sabemos que va a contener, pero que sabemos que al darle un input
nos va a dar un output exacto. Esto nos puede ayudar a hacer pruebas de código de una forma muy sencilla. 

Para hacer este tipos de pruebas vamos a importar el módulo de unittest. Vamos a hacer una clase en el archivo principal, __main__. Y en 
esta clase vamos a pasarle el argumento: unittest.TestCase.

Ahora dentro de esta clase vamos a hacer diferentes functions para hacer prueba a partes de nuestro código. Para ejemplo, una suma de valores, 
vamos a usar la function de nuestra clase assertEqual() de la siguiente forma en el siguiente contexto:

Tenemos una function que suma dos números, vamos a sumar 2 + 2, el output de este debe ser 4. Sencillo. Vamos a hacer una function en 
la clase de BlackBox para probar esta function.

escribimos el resultado, en una variable preferiblemente y lo vamos a usar.
resultado = suma(2, 2)

despues con self, que tiene el valor de unittest.TestCase, vamos a llamar la function assertEqual(), que nos va a permitir 
verificar el resultado esperado y el resultado dado por la funtion, haciendolo de la siguiente forma:

self.asserEqual(resultado, 4)

Ahora esto puede ser igual a un if resultado == 4, haga una cosa. Sin embargo lo especial de este metodo es la información que nos proveé, 
cómo una prueba. Nos da tiempo de ejecución, resultados, y si no son iguales va a saltar el error. Dandonos una mejor prueba frente a cambios 
que pueden ocurrir en el código.

Y se me olvida agregar, cómo esto debe ser hecho en el archivo principal. __main__. Vamos a tener que decirle que haga las pruebas cómo tal.
En el bloque de:

if __name__ == "__main__":
	unittest.main()

simplemente agregamos que se ejecuten los tests y unittest los correra automaticamente.

Y esto para que me sirve? Para hacer diferentes tests

### Modular Testing
Testear cada módulo, function o elemento por aparte para ver si solo funciona bien.

### Integration Testing
Testear diferentes grupos de módulos, functions o elementos para ver si sí pueden funcionar en conjunto, hasta tener un 
test global o total del programa

## Cristal Box 
Mientras que la BlackBox es una caja desconocida, la cristal box es un tipo de prueba en el que ya sabemos que hay en la caja, y tenemos 
los mismos datos, sabemos que inputs se necesitan para ciertas outputs. Y se puede aplicar de casí la misma forma que una BlackBox, entonces
cual es la diferencia?

La principal diferencia es que con la BlackBox, no tenemos hecha o aun totalmente definida la function, pero si sus outputs y inputs. Siendo 
perfecta para probar MIENTRAS SE ESTA DESARROLLANDO.

Mientas que con las cristal box, tenemos definida y en parte funcionando la function, y en parte sus outputs y inputs. Siendo perfecta para 
probar todo los posibles resultados de la function, dentro de un margen. Saliendo a la luz los posibles errores que tienen.


