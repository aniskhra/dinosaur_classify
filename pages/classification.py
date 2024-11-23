import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os

@st.cache_resource
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict_image(image, model, class_names):
    image = image.resize((150, 150))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    prediction = model.predict(image_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)
    return predicted_class, confidence

def get_dinosaur_info(dino_name):
    """Menampilkan informasi tentang dinosaurus."""
    info = {
        "Triceratops": """
            - 🦖 **Tipe**: Herbivora
            - 🌍 **Habitat**: Padang rumput dan hutan dataran rendah 
            - ⏳ **Periode**: Akhir periode Kapur (68–66 juta tahun yang lalu)
            - 🔍 **Ciri khas**: Tiga tanduk di kepala, frill besar di belakang kepala
            - 💡 **Fakta menarik**: Frill digunakan untuk menarik pasangan atau melindungi diri dari predator.
        """,
        "Spinosaurus": """
            - 🦖 **Tipe**: Karnivora semi-akuatik
            - 🌍 **Habitat**: Sungai, danau, dan lingkungan berair 
            - ⏳ **Periode**: Awal hingga pertengahan periode Kapur (112–93 juta tahun yang lalu)
            - 🔍 **Ciri khas**: Memiliki layar besar di punggungnya
            - 💡 **Fakta menarik**: Diduga menjadi salah satu dinosaurus terbesar yang hidup di air dan darat.
        """,
        "Brachiosaurus": """
            - 🦖 **Tipe**: Herbivora
            - 🌍 **Habitat**: Hutan tropis dengan pohon tinggi 
            - ⏳ **Periode**: Akhir periode Jurassic (154–153 juta tahun yang lalu)
            - 🔍 **Ciri khas**: Leher sangat panjang, kaki depan lebih panjang dari kaki belakang
            - 💡 **Fakta menarik**: Digunakan untuk meraih daun di pohon yang sangat tinggi.
        """,
        "Stegosaurus": """
            - 🦖 **Tipe**: Herbivora
            - 🌍 **Habitat**: Padang rumput semi-kering dan hutan
            - ⏳ **Periode**: Akhir periode Jurassic (155–150 juta tahun yang lalu)
            - 🔍 **Ciri khas**: Lempengan besar di punggung dan ekor berduri
            - 💡 **Fakta menarik**: Otaknya sangat kecil dibandingkan tubuhnya yang besar.
        """,
        "Tyrannosaurus Rex": """
            - 🦖 **Tipe**: Karnivora
            - 🌍 **Habitat**: Hutan subtropis dan daerah dataran tinggi
            - ⏳ **Periode**: Akhir periode Kapur (68–66 juta tahun yang lalu)
            - 🔍 **Ciri khas**: Gigi besar dan kuat yang dapat menghancurkan tulang
            - 💡 **Fakta menarik**: Salah satu predator terbesar di darat yang pernah ada.
        """,
        "Velociraptor": """
            - 🦖 **Tipe**: Karnivora
            - 🌍 **Habitat**: Padang pasir dan daerah semi-kering
            - ⏳ **Periode**: Akhir periode Kapur (75–71 juta tahun yang lalu)
            - 🔍 **Ciri khas**: Berukuran kecil dengan cakar tajam
            - 💡 **Fakta menarik**: Sangat cerdas dan berburu dalam kelompok.
        """
    }
    st.markdown(info.get(dino_name, "Informasi tidak ditemukan"))

def show_classification():
    """Halaman Klasifikasi."""
    st.markdown("""
    <div class="box">
        <h1>🕵️ Klasifikasi Dinosaurus</h1>
        <p>Di sini kamu bisa mengunggah gambar dinosaurus untuk mengetahui klasifikasinya.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Unggah gambar dinosaurus kamu:", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)
        st.write("Memproses gambar...")

        # Muat model
        model_path = os.path.join(os.path.dirname(__file__), "../model/my_model.h5")
        model = load_model(model_path)

        # Daftar kelas dinosaurus
        class_names = ["Triceratops", "Spinosaurus", "Brachiosaurus", "Stegosaurus", "Tyrannosaurus Rex", "Velociraptor"]
        
        # Prediksi
        predicted_class, confidence = predict_image(image, model, class_names)
        
        # Tampilkan prediksi dengan nama dinosaurus lebih besar
        st.markdown(f"<h2 style='text-align: center; font-size: 40px; font-weight: bold;'>Prediksi: {predicted_class}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 20px;'>(Confidence: {confidence * 100:.2f}%)</p>", unsafe_allow_html=True)

        # Tampilkan informasi dinosaurus sesuai dengan nama yang diprediksi
        get_dinosaur_info(predicted_class)