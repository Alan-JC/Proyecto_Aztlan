"""
Proyecto Aztlán — Explorador y predictor educativo de exoplanetas.

Esta interfaz usa el modelo guardado en models/model_xgb.pkl para generar
una predicción exploratoria a partir de tres parámetros astronómicos.
"""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Configuración de la aplicación
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Proyecto Aztlán | Exoplanetas",
    page_icon="🪐",
    layout="wide",
)

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "model_xgb.pkl"

# ---------------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------------
@st.cache_resource
def load_model(model_path: Path):
    """Carga el modelo una sola vez durante la sesión de Streamlit."""
    if not model_path.exists():
        return None
    return joblib.load(model_path)


def build_input(radius: float, period: float, stellar_temp: float) -> pd.DataFrame:
    """Construye la tabla de entrada con los nombres de columnas esperados."""
    return pd.DataFrame(
        [[radius, period, stellar_temp]],
        columns=["planet_radius", "orbital_period", "stellar_temp"],
    )


def get_prediction_label(prediction) -> tuple[str, str]:
    """Convierte la etiqueta del modelo en texto para la interfaz."""
    if int(prediction) == 1:
        return "Candidato positivo", "El modelo clasificó estos parámetros como positivos."
    return "Candidato negativo", "El modelo no clasificó estos parámetros como positivos."


# ---------------------------------------------------------------------------
# Encabezado
# ---------------------------------------------------------------------------
st.title("🪐 Proyecto Aztlán")
st.caption("EXPLORACIÓN DE EXOPLANETAS · DATA SCIENCE · MACHINE LEARNING")
st.markdown(
    "Una experiencia educativa para explorar parámetros planetarios y observar "
    "cómo un modelo de clasificación interpreta datos astronómicos."
)

st.divider()

# ---------------------------------------------------------------------------
# Cargar modelo y verificar disponibilidad
# ---------------------------------------------------------------------------
model = load_model(MODEL_PATH)

if model is None:
    st.warning(
        "No se encontró el modelo entrenado. Coloca el archivo "
        "`model_xgb.pkl` dentro de la carpeta `models/` para habilitar "
        "las predicciones."
)

# ---------------------------------------------------------------------------
# Panel de exploración
# ---------------------------------------------------------------------------
tab_predict, tab_about, tab_data = st.tabs(
    ["🔭 Explorar parámetros", "ℹ️ Sobre el proyecto", "📊 Datos y modelo"]
)

with tab_predict:
    st.subheader("Configura un sistema planetario")
    st.write("Modifica los valores y ejecuta una clasificación exploratoria.")

    col_inputs, col_result = st.columns([1.15, 0.85], gap="large")

    with col_inputs:
        radius = st.slider(
            "Radio planetario (radios terrestres)",
            min_value=0.1,
            max_value=20.0,
            value=1.0,
            step=0.1,
        )
        period = st.slider(
            "Periodo orbital (días)",
            min_value=0.1,
            max_value=1000.0,
            value=365.0,
            step=0.1,
        )
        stellar_temp = st.slider(
            "Temperatura estelar (K)",
            min_value=2000,
            max_value=10000,
            value=5778,
            step=50,
        )

        # Valores de referencia aproximados del sistema Tierra-Sol.
        st.caption(
            "Referencia aproximada Tierra-Sol: 1 radio terrestre, 365 días "
            "de periodo orbital y 5,778 K de temperatura solar."
        )

        predict_button = st.button(
            "Analizar parámetros", type="primary", disabled=model is None
        )

    with col_result:
        st.markdown("### Resultado")
        st.metric("Radio", f"{radius:.1f} R⊕")
        st.metric("Periodo orbital", f"{period:.1f} días")
        st.metric("Temperatura estelar", f"{stellar_temp:,} K")

        if predict_button and model is not None:
            try:
                input_df = build_input(radius, period, stellar_temp)
                prediction = model.predict(input_df)[0]
                label, description = get_prediction_label(prediction)

                if int(prediction) == 1:
                    st.success(f"**{label}**\n\n{description}")
                else:
                    st.info(f"**{label}**\n\n{description}")

                # Si el estimador ofrece probabilidades, mostrar la confianza
                # estimada por el modelo sin interpretarla como certeza científica.
                if hasattr(model, "predict_proba"):
                    probabilities = model.predict_proba(input_df)[0]
                    st.caption("Probabilidades estimadas por el clasificador")
                    st.write(
                        {
                            str(class_label): f"{probability:.1%}"
                            for class_label, probability in zip(
                                model.classes_, probabilities
                            )
                        }
                    )
            except Exception as error:
                st.error(
                    "No fue posible generar la predicción. Verifica que el modelo "
                    "haya sido entrenado con las tres variables esperadas."
                )
                st.exception(error)

        st.caption(
            "Esta clasificación es experimental y educativa. No confirma ni descubre "
            "un exoplaneta; la confirmación requiere análisis científico adicional."
        )

with tab_about:
    st.subheader("¿Qué busca Aztlán?")
    st.write(
        "Proyecto Aztlán explora el uso de ciencia de datos y aprendizaje "
        "automático para analizar información relacionada con exoplanetas: "
        "planetas que orbitan estrellas fuera de nuestro sistema solar."
    )
    st.markdown(
        """
        **Objetivos**
        - Explorar conjuntos de datos de misiones astronómicas.
        - Comprender variables como radio y periodo orbital.
        - Experimentar con modelos de clasificación.
        - Comunicar resultados de manera visual y accesible.
        """
    )

with tab_data:
    st.subheader("Fuentes y alcance")
    st.write(
        "El repositorio contempla conjuntos de datos de Kepler, K2 y TESS. "
        "La aplicación de predicción utiliza actualmente tres variables de entrada "
        "y un modelo previamente entrenado."
    )
    st.markdown(
        """
        **Variables de entrada**
        - `planet_radius`: radio planetario.
        - `orbital_period`: periodo orbital.
        - `stellar_temp`: temperatura de la estrella.

        **Tecnologías**
        - Python y Pandas para manejo de datos.
        - XGBoost / Scikit-learn para machine learning.
        - Joblib para persistencia del modelo.
        - Streamlit para la interfaz.
        """
    )

st.divider()
st.caption(
    "Proyecto educativo · Las salidas del modelo son estimaciones de clasificación, "
    "no evidencia de confirmación astronómica."
)
