import streamlit as st

st.title("Roi77")
st.write(        
    "Wut Wut Wut"
)
st.image("IMG-20250519-WA0016.jpg", width=200)
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"(angka) adalah Bilangan Genap")
else:
st.write(f"{angka) adalah Bilangan Ganjil")
