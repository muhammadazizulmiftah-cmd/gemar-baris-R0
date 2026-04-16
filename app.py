import streamlit as st
import google.generativeai as genai
from PIL import Image

# GANTI INI dengan API Key yang kamu copy tadi
API_KEY = "AQ.Ab8RN6LT0YbSFtgdtl5tvnC0DM8hUYzzyPl0rQyfD20lr4GioA"

# Konfigurasi Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

st.set_page_config(page_title="AI Scan Gigi Gratis", layout="centered")

st.title("🦷 Dentist AI Scanner")
st.info("Ambil foto gigi kamu dengan pencahayaan yang terang untuk hasil maksimal.")

# Fitur Ambil Foto
foto_kamera = st.camera_input("Ambil Foto Gigi")
foto_upload = st.file_uploader("Atau upload foto dari galeri", type=['jpg', 'jpeg', 'png'])

# Pilih salah satu input
input_foto = foto_kamera if foto_kamera else foto_upload

if input_foto:
    img = Image.open(input_foto)
    st.image(img, caption="Foto berhasil diambil", use_container_width=True)
    
    if st.button("Mulai Analisa"):
        with st.spinner("Sedang menganalisa kondisi gigi..."):
            try:
                # Instruksi untuk Gemini (Prompt)
                instruksi = """
                Analisa gambar gigi ini dengan detail:
                1. Apakah ada tanda Karies (lubang gigi)?
                2. Apakah terlihat Karang Gigi (Tartar) atau Plak?
                3. Bagaimana kondisi kebersihan secara umum?
                
                Berikan jawaban dalam Bahasa Indonesia yang ramah.
                Wajib sertakan kalimat: 'Hasil ini hanyalah prediksi AI, silakan konsultasi ke dokter gigi untuk diagnosa akurat.'
                """
                
                response = model.generate_content([instruksi, img])
                
                st.success("Analisa Selesai!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

st.divider()
st.caption("Dibuat dengan Gemini AI Studio & Streamlit")
