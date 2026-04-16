import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. SETUP KEAMANAN (MENGAMBIL KUNCI DARI SECRETS)
try:
    api_kunci = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_kunci)
except:
    st.error("Error: Kunci API tidak ditemukan di Settings Streamlit!")

# 2. TAMPILAN APLIKASI
st.set_page_config(page_title="Scan Gigi AI", layout="centered")
st.title("🦷 Aplikasi Scan Gigi")
st.write("Ambil foto gigi kamu dengan jelas untuk dicek oleh AI.")

# 3. FITUR KAMERA
foto = st.camera_input("Klik tombol di bawah untuk ambil foto")

if foto:
    # Menampilkan gambar yang diambil
    img = Image.open(foto)
    st.image(img, caption="Foto berhasil diambil", use_container_width=True)
    
    if st.button("Analisa Sekarang"):
        with st.spinner("Tunggu sebentar, AI sedang melihat gigi kamu..."):
            try:
                # Menggunakan model Gemini terbaru
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                # Perintah untuk AI
                perintah = "Tolong analisa foto gigi ini. Jelaskan apakah ada karies (lubang), karang gigi, atau plak. Berikan saran dalam Bahasa Indonesia yang mudah dimengerti."
                
                # Proses analisa
                hasil = model.generate_content([perintah, img])
                
                st.success("Hasil Analisa:")
                st.write(hasil.text)
                st.warning("PENTING: Ini hanya prediksi AI. Harap konsultasi ke dokter gigi asli untuk diagnosa medis.")
            
            except Exception as e:
                st.error(f"Maaf, terjadi masalah teknis: {e}")
