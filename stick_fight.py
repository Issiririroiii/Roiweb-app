import streamlit as st
import random

st.set_page_config(page_title="Epic Two Players Stick Fight", layout="centered")

# Judul
st.title("Epic Two Players Stick Fight")
st.subheader("Turn-based Battle Game")

# Inisialisasi state
if 'player1_hp' not in st.session_state:
    st.session_state.player1_hp = 100
if 'player2_hp' not in st.session_state:
    st.session_state.player2_hp = 100
if 'turn' not in st.session_state:
    st.session_state.turn = "Player 1"
if 'log' not in st.session_state:
    st.session_state.log = []

# Fungsi serangan
def attack(attacker, defender):
    damage = random.randint(5, 20)
    if defender == "Player 1":
        st.session_state.player1_hp -= damage
    else:
        st.session_state.player2_hp -= damage
    st.session_state.log.insert(0, f"{attacker} hits {defender} for {damage} damage!")
    st.session_state.turn = "Player 2" if attacker == "Player 1" else "Player 1"

# Tampilkan HP
st.markdown(f"**Player 1 HP:** {st.session_state.player1_hp}")
st.markdown(f"**Player 2 HP:** {st.session_state.player2_hp}")
st.markdown(f"**Current Turn: {st.session_state.turn}**")

# Tombol serang
if st.session_state.turn == "Player 1":
    if st.button("Player 1 Attack"):
        attack("Player 1", "Player 2")
else:
    if st.button("Player 2 Attack"):
        attack("Player 2", "Player 1")

# Menampilkan log
st.markdown("### Battle Log")
for entry in st.session_state.log[:5]:
    st.markdown(f"- {entry}")

# Reset tombol
if st.button("Reset Game"):
    st.session_state.player1_hp = 100
    st.session_state.player2_hp = 100
    st.session_state.turn = "Player 1"
    st.session_state.log = []

# Cek kemenangan
if st.session_state.player1_hp <= 0:
    st.success("Player 2 Wins!")
elif st.session_state.player2_hp <= 0:
    st.success("Player 1 Wins!")
  
