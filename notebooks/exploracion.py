# notebooks/exploracion.py

import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar CSVs y limpiar metadatos
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, comment="#", sep=",")  # Ignora líneas de comentario
        # Eliminar filas con valores faltantes en columnas importantes
        cols = ['planet_radius', 'orbital_period', 'stellar_temp', 'confirmed']
        df = df.dropna(subset=[c for c in cols if c in df.columns])
        return df
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return None

# Lista de archivos a explorar
datasets = {
    "Kepler": "data/kepler.csv",
    "K2": "data/k2.csv",
    "TESS": "data/tess.csv"
}


for name, path in datasets.items():
    print(f"\n==== Explorando {name} ====")
    df = load_data(path)
    if df is not None and not df.empty:
        print(f"Columnas disponibles: {df.columns.tolist()}")
        print("Primeras filas:")
        print(df.head())

        # Estadísticas básicas
        print("\nEstadísticas descriptivas:")
        print(df.describe())

        # Graficar distribución de radio del planeta si existe
        if 'planet_radius' in df.columns:
            plt.figure(figsize=(6,4))
            plt.hist(df['planet_radius'], bins=20, color='skyblue', edgecolor='black')
            plt.title(f"Distribución de radios de planetas ({name})")
            plt.xlabel("Radio del planeta (R_Tierra)")
            plt.ylabel("Cantidad")
            plt.show()
    else:
        print(f"No se pudo cargar datos de {name}")
