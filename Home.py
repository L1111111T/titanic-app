import streamlit as st

st.set_page_config(page_title="Home")

st.title("Welcome to the Titanic App")

st.write(
    """
    This Streamlit application analyzes the Titanic dataset
    and predicts passenger survival probability.
    """
)

st.info("Please open app.py to explore the analysis and prediction pages.")

if st.button("Go to Titanic App"):
    st.switch_page("app.py")
