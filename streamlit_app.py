import streamlit as st

st.title("Roi777")
st.write(        
    "Bukan Web Judol"
)
st.image("IMG-20250519-WA0016.jpg", width=2000)
st.title("Roi pintar meramal")
st.header("Tulis tanggal lahir Lu")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"{angka} Kurang Hoki dalam asmara, Bad boy/Bad Girl, redflag, bjir")
else:
 st.write(f"{angka} Damn Hoki banget biasanya banyak yang suka, orangnya ganteng, cool, keren, kaya yg difoto 👆🏻")
