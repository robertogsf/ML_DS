import pandas as pd

# Cargar el dataset en un DataFrame
df = pd.read_csv('students-data.csv')

# Imprimir las primeras 5 filas del DataFrame
print(df.head(5))

# Calcular la media de 'GPA'
media = df['GPA'].mean()
print(f'La media de GPA es: {media}')

# Filtrar las filas donde 'GPA' es mayor que 85
df_filtrado = df[df['GPA'] > 85]

# Guardar el DataFrame resultante en un nuevo archivo JSON
df_filtrado.to_json('df_filtrado.json', orient='records', lines=True)
