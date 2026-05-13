import streamlit as st

st.set_page_config(page_title="Home")

st.title("Welcome to the Home Page!")
st.write("This is the home page for the Titanic App.")

if st.button("Go to Titanic App"):
    st.switch_page("pages/app.py")
