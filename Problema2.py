def Cruzmasgrande(matrix):
    
    n = len(matrix)  # Guardamos el tamaño de la matriz (asume que es cuadrada n×n)
    # Inicializamos las matrices auxiliares
    left = [[0] * n for i in range(n)]    # Almacena cantidad de 1s consecutivos hacia la izquierda
    right = [[0] * n for i in range(n)]   # Almacena cantidad de 1s consecutivos hacia la derecha
    top = [[0] * n for i in range(n)]     # Almacena cantidad de 1s consecutivos hacia arriba
    bottom = [[0] * n for i in range(n)]  # Almacena cantidad de 1s consecutivos hacia abajo
    
    # Llenamos las matrices left y top recorriendo la matriz de izquierda a derecha y de arriba a abajo
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:  # Solo calculamos para celdas con valor 1
                # Para left: si estamos en la primera columna (j=0), left=1, sino sumamos 1 al valor previo
                left[i][j] = 1 if j == 0 else left[i][j - 1] + 1
                # Para top: si estamos en la primera fila (i=0), top=1, sino sumamos 1 al valor superior
                top[i][j] = 1 if i == 0 else top[i - 1][j] + 1
    
    # Llenamos las matrices right y bottom recorriendo la matriz de derecha a izquierda y de abajo a arriba
    for i in range(n - 1, -1, -1):  # Empezamos desde la última fila hacia arriba
        for j in range(n - 1, -1, -1):  # Empezamos desde la última columna hacia la izquierda
            if matrix[i][j] == 1:  # Solo calculamos para celdas con valor 1
                # Para right: si estamos en la última columna (j=n-1), right=1, sino sumamos 1 al valor siguiente
                right[i][j] = 1 if j == n - 1 else right[i][j + 1] + 1
                # Para bottom: si estamos en la última fila (i=n-1), bottom=1, sino sumamos 1 al valor inferior
                bottom[i][j] = 1 if i == n - 1 else bottom[i + 1][j] + 1
    
    tamañoMaximo = 0  # Variable para almacenar el tamaño máximo de cruz encontrado
    
    # Recorremos toda la matriz para calcular el tamaño máximo de cruz posible
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:  # Solo las celdas con valor 1 pueden ser centros de cruces
                # El tamaño del brazo más corto determina el tamaño máximo de la cruz
                size = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                
                # Calculamos el tamaño total de la cruz:
                # Para cada dirección tenemos (size-1) celdas + 1 celda central = 4*(size-1)+1
                tamañoMaximo = max(tamañoMaximo, (4 * (size - 1)) + 1)
    
    return tamañoMaximo

matriz = [
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 ] ,
[ 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ] ,
[ 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 1 ] ,
[ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 ] ,
[ 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ] ,
[ 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 ] ,
[ 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 0 ]
]
print(Cruzmasgrande(matriz))