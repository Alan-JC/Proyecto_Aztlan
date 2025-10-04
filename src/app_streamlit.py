import streamlit as st
import pandas as pd
import joblib
# titulo

# Título del proyecto
st.title("🌌 Proyecto Aztlán: Detectores de Exoplanetas")
st.write("""
Este proyecto educativo muestra cómo la inteligencia artificial (IA) puede ayudarnos 
a descubrir planetas fuera de nuestro sistema solar, mientras aprendemos sobre ciencia, 
datos y programación.
""")

# Cargar el modelo (asegúrate de entrenarlo antes o usar un modelo ya guardado)
model = joblib.load("models/model_xgb.pkl")

# Interfaz de usuario
st.subheader("🔭 Prueba los parámetros de un planeta:")

radius = st.slider("Radio del planeta (en radios terrestres)", 0.1, 20.0, 1.0)
period = st.slider("Periodo orbital (días)", 0.1, 1000.0, 365.0)
temp = st.slider("Temperatura de la estrella (Kelvin)", 2000, 10000, 5778)

if st.button("Predecir"):
    # Crear un DataFrame con los datos ingresados
    X_new = pd.DataFrame([[radius, period, temp]],
                         columns=["planet_radius", "orbital_period", "stellar_temp"])

    # Hacer la predicción
    pred = model.predict(X_new)

    # Mostrar el resultado
    if pred[0] == 1:
        st.success("🌍 ¡Posible exoplaneta confirmado!")
    else:
        st.warning("🪐 No confirmado... sigue explorando el universo.")
