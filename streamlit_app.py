import streamlit as st

st.title("Roi777")
st.write(        
    "Web ini dibuat untuk Tugas dan candaan saja"
)
st.image("IMG-20250519-WA0016.jpg", width=700)
st.title("Roi pintar meramal")
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
    
import random
st.title("🥷 Stickman Fight")

# Inisialisasi state
if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.log = []
    st.session_state.round = 1

# Fungsi log
def add_log(text):
    st.session_state.log.insert(0, text)

# UI & aksi
st.markdown(f"**Ronde {st.session_state.round}**")
st.progress(st.session_state.player_hp, text="HP Kamu")
st.progress(st.session_state.enemy_hp, text="HP Musuh")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⚔️ Serang"):
        damage = random.randint(10, 20)
        st.session_state.enemy_hp -= damage
        add_log(f"Kamu menyerang musuh dan memberi {damage} damage!")
with col2:
    if st.button("🛡️ Bertahan"):
        heal = random.randint(5, 10)
        st.session_state.player_hp += heal
        if st.session_state.player_hp > 100:
            st.session_state.player_hp = 100
        add_log(f"Kamu bertahan dan memulihkan {heal} HP!")
with col3:
    if st.button("🔥 Serangan Khusus"):
        damage = random.randint(15, 30)
        recoil = random.randint(5, 10)
        st.session_state.enemy_hp -= damage
        st.session_state.player_hp -= recoil
        add_log(f"Kamu menyerang dengan kekuatan besar ({damage} damage), tapi kehilangan {recoil} HP!")

# Musuh menyerang setiap aksi
if st.session_state.enemy_hp > 0 and st.session_state.player_hp > 0:
    enemy_attack = random.randint(5, 15)
    st.session_state.player_hp -= enemy_attack
    add_log(f"Musuh menyerang dan memberi {enemy_attack} damage!")

st.session_state.round += 1

# Game over
if st.session_state.player_hp <= 0:
    st.error("Innalillahi Kamu mati! Game over.")
elif st.session_state.enemy_hp <= 0:
    st.success("Alhamdulillah Kamu menang! Stickman musuh tumbang.")

if st.button("🔁 Mulai Ulang"):
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.log = []
    st.session_state.round = 1
    st.rerun()

# Log Pertarungan
st.markdown("### Log Pertarungan")
for entry in st.session_state.log[:10]:
    st.markdown(f"- {entry}")
    
