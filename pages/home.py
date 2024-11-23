import streamlit as st 
import os

def show_home():
    """Halaman Beranda."""
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(parent_dir, "../src/image")

    dinosaurus = [
        {"nama": "Triceratops", "file": "triceratops.png"},
        {"nama": "Spinosaurus", "file": "spinosaurus.png"},
        {"nama": "Brachiosaurus", "file": "brachiosaurus.png"},
        {"nama": "Stegosaurus", "file": "stegosaurus.png"},
        {"nama": "Tyrannosaurus Rex", "file": "trex.png"},
        {"nama": "Velociraptor", "file": "velociraptor.png"},
    ]

    # Intro
    st.markdown("""
    <div class="box">
        <h1 style="text-align: center;">Crawrify🦖</h1>
        <p>
            Selamat Datang di <b>Crawrify</b>! <b>Crawrify</b> merupakan model AI yang bisa mendeteksi gambar dinosaurus dan membantu kamu mengenal lebih banyak tentang mereka. 
            Kamu bisa mengunggah gambar dinosaurus di menu <b>Klasifikasi</b> dan <b>Crawrify</b> akan memberikan informasi menarik tentang dinosaurus tersebut.
            Namun, perlu diingat bahwa AI ini tidak 100% akurat dan tidak bisa mendeteksi semua jenis dinosaurus, tetapi hanya 6 jenis dinosaurus yang paling dikenal.
            Mari mengeksplorasi dunia dinosaurus bersama kami!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Menambahkan gambar dari URL
    st.image("https://wallpapercave.com/wp/wp8978740.jpg", use_column_width=True)

    # Sejarah Dinosaurus
    st.markdown("""
    <div class="box">
        <h3 style="text-align: center;">📜 Sejarah Dinosaurus</h3>
        <p>
            Sejarah dinosaurus mencakup lebih dari 160 juta tahun evolusi dan perubahan yang luar biasa. 
            Dari munculnya dinosaurus pertama kali hingga kepunahan massal yang mengakhiri era mereka, sejarah dinosaurus sangat menarik dan penuh dengan transformasi.
            Berikut adalah gambaran singkat mengenai sejarah dinosaurus yang terbagi dalam beberapa periode penting:
            <br><b>1. Periode Trias (Sekitar 230 – 201 juta tahun yang lalu)</b>
                <br>Dinosaurus pertama kali muncul di akhir periode Trias, awalnya kecil dan tidak dominan. Kelompok seperti Saurischia mulai berkembang, menggantikan spesies lain di akhir periode.
            <br><b>2. Periode Jurassic (Sekitar 201 – 145 juta tahun yang lalu)</b>
                <br>Pada periode ini, dinosaurus menjadi penguasa daratan. Sauropoda (pemakan tumbuhan berleher panjang) dan theropoda (predator seperti Allosaurus) berkembang pesat. Reptil terbang Pterosaurs juga muncul.
            <br><b>3. Periode Cretaceous (Sekitar 145 – 66 juta tahun yang lalu)</b>
                <br>Puncak keberagaman dinosaurus seperti T. rex, Triceratops, dan Velociraptor. Tumbuhan berbunga mulai muncul. Periode ini diakhiri oleh kepunahan massal akibat asteroid besar.
            <br><b>4. Kepunahan Dinosaurus dan Era Pasca-Dinosaurus</b>
                <br>Setelah dinosaurus punah, mamalia berkembang dan mendominasi bumi termasuk manusia. Meskipun dinosaurus besar telah punah, kelompok burung keturunan dinosaurus theropoda bertahan dan berkembang hingga sekarang.
        </p>
        <p>Sumber: <a href="https://www.gramedia.com/best-seller/kenapa-dinosaurus-punah/#Sejarah_Dinosaurus_dari_Abad_ke_Abad">Gramedia</a></p>
    </div>
    """, unsafe_allow_html=True)

    # Jenis-Jenis Dinosaurus
    st.markdown("""
    <div class="box">
        <h3 style="text-align: center;">🦕 Jenis-Jenis Dinosaurus</h3>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i, dino in enumerate(dinosaurus[:3]):
        with cols[i]:
            img_path = os.path.join(image_dir, dino["file"])
            st.image(img_path, caption=dino["nama"], use_column_width=True)

    cols = st.columns(3)
    for i, dino in enumerate(dinosaurus[3:]):
        with cols[i]:
            img_path = os.path.join(image_dir, dino["file"])
            st.image(img_path, caption=dino["nama"], use_column_width=True)