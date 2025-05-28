import streamlit as st

st.title("Roi777")
st.write(        
    "Web ini dibuat untuk Tugas dan Hiburan saja"
)
st.image("IMG_20250428_130541.jpg", width=700)
st.title("orang di atas pintar meramal")
st.header("Tulis tanggal lahir Kamu")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
 st.write(f"{angka} Kurang Hoki dalam asmara, Bad boy/Bad Girl, redflag, jaskiding")
else:
 st.write(f"{angka} Damn Hoki banget biasanya banyak yang suka, orangnya ganteng, cool, keren, kaya yg difoto 👆🏻")

st.title("AYO MAIN SUIT JAWA ✊🏻✋🏻✌🏻")

import random
pilihan = ["Batu", "Kertas", "Gunting"]
emoji = {
    "Batu": "✊",
    "Kertas": "✋",
    "Gunting": "✌️"
}

st.markdown("Pilih salah satu dan lawan bot!")

player_choice = st.selectbox("Pilihan kamu:", pilihan)
if st.button("Main!"):
    computer_choice = random.choice(pilihan)

    st.write(f"Kamu memilih: {emoji[player_choice]} {player_choice}")
    st.write(f"Komputer memilih: {emoji[computer_choice]} {computer_choice}")

    if player_choice == computer_choice:
        st.info("Hasil: Seri!")
    elif (player_choice == "Batu" and computer_choice == "Gunting") or \
         (player_choice == "Kertas" and computer_choice == "Batu") or \
         (player_choice == "Gunting" and computer_choice == "Kertas"):
        st.success("Hasil: Kamu menang, selamat🎉!")
    else:
        st.error("Hasil: Maaf kamu Kalah!")

if st.button("Main Lagi yu"):
    st.rerun()
else:
    pass
st.title("Aplikasi Sederhana")

# Menggunakan layout kolom
col1, col2 = st.columns(2)

with col1:
    angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

    if (angka % 2) == 0:
        st.write(f"{angka} adalah Bilangan Genap")
    else:
        st.write(f"{angka} adalah Bilangan Ganjil")

with col2:
    st.header("Aplikasi menghitung Total Belanja")

    def hitung_total(harga, jumlah):
        return harga * jumlah

    harga_barang = st.number_input("Masukkan Harga Barang:", value=0, step=1000)
    jumlah_barang = st.number_input("Masukkan Jumlah Barang:", value=0, step=1)
    total_harga = hitung_total(harga_barang, jumlah_barang)

    if total_harga > 100000:
        total_harga_diskon = total_harga - 0.05 * total_harga
        st.write(f"Total Harga (dengan diskon): Rp. {total_harga_diskon:,.0f}")
    else:
        st.write(f"Total Harga: Rp. {total_harga:,.0f}")

    bayar = st.number_input("Masukkan Jumlah Uang:", value=0, step=10000)

    if bayar >= total_harga:
        kembalian_uang = bayar - total_harga
        st.write(f"Uang Kembalian: Rp. {kembalian_uang:,.0f}")
    else:
        st.write("Uang yang anda bayarkan kurang ")
    
