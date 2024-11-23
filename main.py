import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from pages.home import show_home
from pages.classification import show_classification
from pages.about import show_about
from utils import load_fontawesome

# Konfigurasi Halaman
st.set_page_config(
    page_title="Crawrify - Dinosaurus AI",
    page_icon="🦖",
    initial_sidebar_state="collapsed",
)

# Muat CSS Eksternal
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Gaya Navbar
styles = {
    "nav": {
        "background-color": "#1F4529",
        "margin-bottom": "30px",
    },
    "a": {
        "color": "#ffffff",
        "font-size": "16px",
        "text-decoration": "none",
        "padding": "10px 30px",
        "text-align": "center",
        "transition": "all 0.3s ease",
        "border-radius": "8px",
    },
    "active": {
        "color": "#ffffff",
        "font-weight": "bold",
        "background-color": "#2c6e3d",
        "padding": "10px 20px",
        "border-radius": "8px",
        "box-shadow": "0px 2px 4px rgba(0, 0, 0, 0.2)",
    },
    "hover": {
        "color": "#cbffcd",
    },
}

# Tentukan Halaman yang Tersedia
pages = ["Beranda", "Klasifikasi", "Tentang"]

# Navbar
selected_page = st_navbar(
    pages=pages,
    styles=styles,
    options={"show_menu": False, "show_sidebar": False},
)

# Atur Navigasi Antar Halaman
def main():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "src/style/style.css")
    load_css(css_path)

    if selected_page == "Beranda":
        show_home()
    elif selected_page == "Klasifikasi":
        show_classification()
    elif selected_page == "Tentang":
        show_about()

if __name__ == "__main__":
    main()