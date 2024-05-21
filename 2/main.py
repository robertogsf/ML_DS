import numpy as np

# Crea un array de tamaño 5x5 con valores aleatorios
array = np.random.rand(5, 5)
print("Array:\n", array)

# Calcula la suma de todos los elementos del array
suma = np.sum(array)
print("\nSuma de todos los elementos del array:", suma)

# Calcula el promedio de cada fila
promedio_filas = np.mean(array, axis=1)
print("\nPromedio de cada fila:", promedio_filas)

# Calcula el promedio de cada columna
promedio_columnas = np.mean(array, axis=0)
print("\nPromedio de cada columna:", promedio_columnas)

# Encuentra el valor máximo del array
maximo = np.max(array)
print("\nValor máximo del array:", maximo)

# Encuentra el valor mínimo del array
minimo = np.min(array)
print("\nValor mínimo del array:", minimo)
