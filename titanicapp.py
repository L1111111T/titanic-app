import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Titanic App", layout="wide")

# -------------------------
# Apply seaborn style
# -------------------------
sns.set_style("whitegrid")

# -------------------------
# Title
# -------------------------
st.title("Titanic App by Yitian Li")

# -------------------------
# Create Tabs
# -------------------------
tab1, tab2 = st.tabs(["Analysis", "Prediction"])

# ==================================================
# ANALYSIS PAGE
# ==================================================
with tab1:

    st.header("Titanic Data Analysis")

    # Read CSV
    df = pd.read_csv("train.csv")

    # Display dataframe
    st.subheader("Entire Titanic Dataset")
    st.dataframe(df)

    # Create boxplots
    st.subheader("Fare Distribution by Passenger Class")

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Pclass 1
    sns.boxplot(
        y=df[df["Pclass"] == 1]["Fare"],
        ax=axes[0]
    )
    axes[0].set_title("Pclass 1")
    axes[0].set_xlabel("First Class")
    axes[0].set_ylabel("Fare")

    # Pclass 2
    sns.boxplot(
        y=df[df["Pclass"] == 2]["Fare"],
        ax=axes[1]
    )
    axes[1].set_title("Pclass 2")
    axes[1].set_xlabel("Second Class")
    axes[1].set_ylabel("Fare")

    # Pclass 3
    sns.boxplot(
        y=df[df["Pclass"] == 3]["Fare"],
        ax=axes[2]
    )
    axes[2].set_title("Pclass 3")
    axes[2].set_xlabel("Third Class")
    axes[2].set_ylabel("Fare")

    st.pyplot(fig)

# ==================================================
# PREDICTION PAGE
# ==================================================
with tab2:

    st.header("Titanic Survival Prediction")

    # Load model
    model = joblib.load("titanic_model.pkl")

    # Input widgets
    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    sex = st.selectbox(
        "Sex",
        ["male", "female"]
    )

    age = st.slider(
        "Age",
        1,
        80,
        24
    )

    fare = st.number_input(
        "Fare",
        min_value=0.0,
        value=32.0
    )

    # Encode sex
    sex_encoded = 1 if sex == "male" else 0

    # Prediction button
    if st.button("Predict Survival Probability"):

        input_data = pd.DataFrame({
            "Pclass": [pclass],
            "Sex": [sex_encoded],
            "Age": [age],
            "Fare": [fare]
        })

        probability = model.predict_proba(input_data)[0][1]

        st.success(
            f"Predicted Survival Probability: {probability:.2%}"
        )
