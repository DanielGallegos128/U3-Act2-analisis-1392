import pandas as pd
import numpy as np
print("Analisis de datos Clientes  Daniel Gallegos NC=1392")

clientes = {
    "Cliente": ["User1", "User2", "User3", "User4", "User5", "User6"],
    "Antiguedad_Meses": [2, 36, 12, 48, 12, 48],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}
df = pd.DataFrame(clientes)
print(df)
print("-+-+-+ Agrupar por una sola columna Antiguedad_Meses +-+-+-")
agrupados = df.groupby('Antiguedad_Meses')
print(agrupados)
# Gasto mensual promedio por meses
print("-+-+-+ Promedio de gasto mensual +-+-+-")
print(agrupados['Gasto_Mensual'].mean())

# Cancela o no por meses
print("-+-+-+ Cancela el servicio +-+-+-")
print(agrupados['Cancela_Servicio'].max())

print("+-+-Daniel+-+-Segunda Parte-+-+1392-+-+")
print("Agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupados['Gasto_Mensual'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrega columna al DataFrame")
print("Columna Team --> Equipo")
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_multiple = df.groupby(['Antiguedad_Meses', 'Equipo'])['Gasto_Mensual'].mean()
print(agrupado_multiple)