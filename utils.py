import streamlit as st

# Menambahkan style dari font awesome
def load_fontawesome():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">
    """, unsafe_allow_html=True)