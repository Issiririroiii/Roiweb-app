import streamlit as st

st.title("Roi777")
st.write(        
    "Bukan Web Judol"
)
st.image("IMG-20250519-WA0016.jpg", width=1000)
st.title("Roi pintar meramal")
st.header("Tulis tanggal lahir Lu")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"{angka} Kurang Hoki dalam asmara, Bad boy/Bad Girl, redflag, bjir")
else:
 st.write(f"{angka} Damn Hoki banget biasanya banyak yang suka, orangnya ganteng, cool, keren, kaya yg difoto 👆🏻")

st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #f0f0f0; /* Ubah warna latar belakang di sini */
        }
        </style>
        """,
        unsafe_allow_html=True
)
backgroundColor = "#f0f0f0"
