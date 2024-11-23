import streamlit as st
from utils import load_fontawesome

def show_about():
    """Halaman Tentang."""
    load_fontawesome()  

    st.markdown("""
    <div class="box">
        <h1 style="text-align: center;">🧑‍💻 Tentang Crawrify</h1>
        <p>
            <b>Crawrify</b> dirancang untuk mempermudah kamu mengenali berbagai jenis dinosaurus hanya dengan mengunggah gambar.
            Dengan teknologi kecerdasan buatan (AI), aplikasi ini mampu mengidentifikasi dinosaurus 
            dan memberikan informasi menarik tentang mereka.
        </p>
    </div>
                
    <div class="box">
         <h3>🌟 Fitur Utama Aplikasi</h3>
            <ul>
                <li>🔍 <strong>Klasifikasi Dinosaurus:</strong> Unggah gambar dinosaurus dan temukan nama serta jenisnya secara otomatis</li>
                <li>📚 <strong>Informasi Edukatif:</strong> Pelajari fakta menarik tentang dinosaurus, seperti habitat, masa hidup, dan ciri khas mereka</li>
                <li>💡 <strong>Tampilan User-Friendly:</strong> Dengan antarmuka yang sederhana, aplikasi ini mudah digunakan oleh semua kalangan</li>
            </ul>
    </div>
                
    <div class="box">
        <h3>🎯 Manfaat Aplikasi</h3>
            <ul>
                <li>📖 <strong>Edukasi:</strong> Membantu pelajar dan penggemar dinosaurus mempelajari lebih dalam tentang hewan purba</li>
                <li>🎮 <strong>Hiburan:</strong> Menjadi alat interaktif yang menyenangkan untuk mengeksplorasi dunia dinosaurus</li>
                <li>🤖 <strong>Teknologi Terapan:</strong> Memperkenalkan bagaimana AI dapat digunakan untuk mengenali objek dalam gambar</li>
            </ul>
        <p>
            Aplikasi ini cocok untuk pelajar, guru, peneliti, orang tua, atau siapa saja yang memiliki minat terhadap dinosaurus.  
        </p>
    </div>
    """,
    unsafe_allow_html=True,
    )

    st.markdown("""   
    <div class="box">
        <h3 style="text-align: center;">☎️ Kontak</h3>
    </div>
    """,
    unsafe_allow_html=True,
    )

    st.markdown("""    
    <div class="contact-box">
        <div class="contact-item">
            <i class="fa-regular fa-envelope"></i>
            <b>Email</b> 
            <a href="mailto:annisakhoiria10@gmail.com">annisakhoiria10@gmail.com</a>
        </div>
        <div class="contact-item">
            <i class="fa-brands fa-instagram"></i>
            <b>Instagram</b> 
            <a href="https://instagram.com/annisarhk">@annisarhk</a>
        </div>
        <div class="contact-item">
            <i class="fa-brands fa-github"></i>
            <b>GitHub</b> 
            <a href="https://github.com/aniskhra">github.com/aniskhra</a>
        </div>
    </div>
    
    <div class="footer">
        <p style="text-align: center; font-size: 12px;">Made with ❤️ by Annisa Alimatul Khoiria</p>
    </div>
    """,
    unsafe_allow_html=True,
)