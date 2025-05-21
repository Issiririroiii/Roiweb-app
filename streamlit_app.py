import streamlit as st

st.title("Roi777")
st.write(        
    "Wut Wut Wut"
)
st.image("IMG-20250519-WA0016.jpg", width=2000)
st.title("Roi pintar berhitung")
st.header("sini cobain aja kalo ga percaya")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"{angka} adalah Bilangan Genap")
else:
 st.write(f"{angka} adalah Bilangan Ganjil")
