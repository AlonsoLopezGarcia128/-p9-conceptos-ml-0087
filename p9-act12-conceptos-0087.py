import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos5 = {
    'distancia_km': [2.1, 5.5, 1.8, 4.2, 3.0],
    'trafico_nivel': [2, 2, 1, 3, 2],
    'edad_repartidor': [31, 26, 43, 34, 23],
    'tiempo_entrega_min': [18, 45, 12, 38, 22]
}

df = pd.DataFrame(datos5)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
