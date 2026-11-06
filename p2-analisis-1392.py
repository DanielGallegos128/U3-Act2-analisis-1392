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
agrupaods = df.groupby('Antiguedad_Meses')
print(agrupaods)
# Gasto mensual promedio por meses
print("-+-+-+ Promedio de gasto mensual +-+-+-")
print(agrupaods['Gasto_Mensual'].mean())

# Cancela o no por meses
print("-+-+-+ Cancela el servicio +-+-+-")
print(agrupaods['Cancela_Servicio'].max())