# Examen parcial No.2

## Problema 1

Dado un número positivo n y un teclado móvil de un Nokia 3230, que tiene dígitos del 0 al 9  
asociados con cada tecla, se desea contar el total de combinaciones posibles de dígitos  de longitud n.  
Podemos comenzar con cualquier dígitos  y presionar solo cuatro teclas adyacentes a cualquier dígitos .  
El teclado también contiene las teclas  ∗  y #, las cuales no están permitidas presionar.


### Explicar porque este problema exhibe subestructura óptima

El objetivo del problema es 

### Explique una idea/solución que exhiba subproblemas traslapados e indique cómo los mismos subproblemas se computan repetidamente.

![alt text](p1.png)

El problema exhibe traslape de subproblemas ya que hay varios subproblemas que se repiten. Por ejemplo: en el árbol de subproblemas se puede observar que hay que resolver varias veces como el del 1 o el del 5. 

### Escriba un código en Python con enfoque de memoización top-down que resuelva este problema

[Repositorio](https://github.com/PedroPabloGuzmanMayen/Parcial2_ADA.git)



### Encuentre el tiempo de complejidad para este algoritmo.

Para hallar la complejidad de este algoritmo, primero definiremos una ecuación de recurrencia. Sabemos que la solución para un dígito en específico esta dada por las soluciones de sus dígitos adyacentes en el teclado . También sabemos que debemos hallar la solución para cada uno de los dígitos del teclado (0-9). 

Por esa razón, primero definiremos una función para hallar una ecuación de recurrencia para hallar el total de combinaciones para un dígito en específico.

Sea A(e) el conjunto de números adyacentes para un dígito e y sea d un dígito entre 0 y 9 y n un número $\in N$ , tenemos: 

$$
F(d, n) =
\begin{cases}
1, & \text{si } n = 0  \\\\
\sum F(a, n-1) \text{ para toda a}  \in A(d), & \text{si } n > 0 \\\\
\end{cases}
$$

Ahora formaremos una ecuación para evaluar las combinaciones posibles de todos los dígitos posibles
$$G(n) = \sum F(d, n) para d \in {0,1,2,3,4,5,6,7.8,9}$$

Ya con la ecuación de la complejidad, formaremos un árbol de recursión para hallar la complejidad del problema

![alt text](p1.png)


En la imágen se puede observar que en el peor de los casos el nodo se dividirá en 4 subproblemas si es que el dígito tiene 4 teclas adyacentes, también se observa que el árbol tendrá un máximo de n niveles ya que se hará la recursión n-1 veces pero debemos tener en cuenta el nivel del problema inicial. Cada estado se ejecutará exactamente solo 1 vez gracias a la memoización. Otro detalle importante es que cada nodo del árbol solamente debe iterar sobre las teclas adyacentes y consultar la tabla de memoización, estas operaciones son son de tiempo constante por lo que tenemos que el costo por nodo es $$O(1)$$. También se debe tener en cuenta que se deben hacer las operaciones 10 veces ya que debemos hacerlas para cada dígito posible en el teclado. Por lo tanto, sabemos que cada nodo se ejecuta una sola vez y que debe repetirse el proceso 10 veces para tener en cuenta los casos de cada número del teclado, por esa razón tenemos queel trabajo total es de $$O(10n)$$

Por lo tanto, la complejidad temporal total del problema es de $$O(n)$$

### Usando su programa, encuentre las combinaciones totales posibles para  n  = 10.

Usando el programa realizado, el resultado con n = 10 es: 1806282






## Problema 2

Dada una matriz cuadrada de 0’s y 1’s, calcule el tamaño de la cruz (símbolo de suma +) más grande  
formada por 1’s

## Problema 3

## Problema 5

