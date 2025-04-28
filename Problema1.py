#Problema 1: teclado Nokia


#Definición del teclado

teclado = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]  

#En este diccionario almacenamos los valores adyacentes

adyacentes = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}

memo = {} #Diccionario para la memoización

#Con esta función calcularemos el número de combinaciones 
def dp(numero, longitud):
    #Caso base
    if longitud == 0:
        return 1; #Si la lnogitud es 0, retornamos 1
    if(numero, longitud) in memo: #Si ya habíamos encontrado la solución, simplemente la devolvemos
        return memo[(numero, longitud)]
    total = 0 #Variable para almacenar las combinaciones totales
    for digito in adyacentes[numero]: #Recorremos cada uno de los digitos adyacentes
        total += dp(digito, longitud -1) #Aplicamos la recursión
    memo[(numero, longitud)] = total #Guardamos los resultados
    return total

def contar_combinaciones(n):
    total = 0
    for digito in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: #Aplicamos la función para cada dígito
        total += dp(digito, n-1)
    return total

print(contar_combinaciones(10))
