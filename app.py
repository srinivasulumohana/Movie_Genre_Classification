# =====================================================
# MOVIE GENRE CLASSIFICATION DASHBOARD
# FINAL ERROR-FREE STREAMLIT APP
# =====================================================

# =========================
# IMPORT LIBRARIES
# =========================

import streamlit as st
import joblib
import os

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Movie Genre Classification",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title("🎬 Movie Genre Classification")

st.write(
    "Predict Movie Genres using NLP & Machine Learning"
)

# =========================
# MODEL PATH
# =========================

model_path = "models/genre_model.pkl"

# =========================
# CHECK MODEL EXISTS
# =========================

if not os.path.exists(model_path):

    st.error(
        "Model file not found! Run train_model.py first."
    )

    st.stop()

# =========================
# LOAD MODEL
# =========================

model = joblib.load(model_path)

# =========================
# USER INPUT
# =========================

movie_description = st.text_area(
    "Enter Movie Description",
    height=200
)

# =========================
# PREDICTION BUTTON
# =========================

if st.button("Predict Genre"):

    if movie_description.strip() == "":

        st.warning(
            "Please enter movie description"
        )

    else:

        prediction = model.predict(
            [movie_description]
        )

        st.success(
            f"Predicted Genre: {prediction[0]}"
        )

# =========================
# EXAMPLES
# =========================

st.header("Example Inputs")

st.write(
    "• Superheroes fight aliens and save the world"
)

st.write(
    "• Haunted house with ghosts and spirits"
)

st.write(
    "• Romantic love story between two people"
)

st.write(
    "• Detectives solving mysterious crimes"
)

# =========================
# FOOTER
# =========================

st.write("---")

st.write(
    "Developed using Python, NLP, Scikit-learn & Streamlit"
)

