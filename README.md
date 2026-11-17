<div align="center">

# Proyecto Aztlán
### Detectores de Exoplanetas

Exploración de datos astronómicos y aprendizaje automático para estudiar señales relacionadas con planetas fuera del sistema solar.

**Python · Pandas · Scikit-learn · XGBoost · Streamlit**

</div>

---

## Descripción

Proyecto educativo que explora cómo los datos de misiones astronómicas pueden utilizarse en un flujo de análisis y clasificación de posibles exoplanetas.

El repositorio incluye conjuntos de datos de **Kepler, K2 y TESS**, un espacio de exploración y una interfaz de Streamlit para probar parámetros planetarios.

## ¿Cómo funciona el prototipo?

La interfaz permite introducir tres parámetros:

- Radio del planeta.
- Periodo orbital.
- Temperatura de la estrella.

Con esos valores, la aplicación construye una entrada para el modelo de clasificación y muestra el resultado de la predicción.

> La predicción es una salida de un modelo de aprendizaje automático y no sustituye la confirmación científica de un exoplaneta.

## Estructura del repositorio

```text
Proyecto_Aztlan/
├── data/
│   ├── k2.csv
│   ├── kepler.csv
│   └── tess.csv
├── models/
│   └── model_xgb.pkl
├── notebooks/
│   └── exploracion.py
├── src/
│   ├── app_streamlit.py
│   ├── preprocess.py
│   └── train_model.py
└── requirements.txt
```

## Tecnologías

- **Python:** lenguaje principal.
- **Pandas y NumPy:** manejo de datos.
- **Matplotlib:** visualización exploratoria.
- **Scikit-learn y XGBoost:** herramientas de aprendizaje automático.
- **Streamlit:** interfaz interactiva.
- **Joblib:** carga del modelo entrenado.

## Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/Alan-JC/Proyecto_Aztlan.git
cd Proyecto_Aztlan
pip install -r requirements.txt
```

## Ejecutar la aplicación

La interfaz requiere que exista un modelo entrenado en `models/model_xgb.pkl`.

Cuando el modelo esté disponible, ejecuta:

```bash
streamlit run src/app_streamlit.py
```

## Estado

Proyecto educativo en desarrollo. La preparación de datos, el entrenamiento del modelo y la validación de resultados forman parte del trabajo pendiente del proyecto.

---

<div align="center">
  <sub>SCIENCE · DATA · MACHINE LEARNING</sub>
</div>
