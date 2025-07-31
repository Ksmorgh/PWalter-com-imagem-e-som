import streamlit as st
import matplotlib.pyplot as plt
import random
import requests
import base64
import os

st.set_page_config(page_title="Projeto Walter Thummel", page_icon="💅")

st.title("🌈 Projeto Walter Thummel — Versão Turbinada")

# Frases personalizadas
frases_walter = [
    "Walter foi visto ontem usando glitter como protetor solar.",
    "Quando Walter chega, até a Alexa fica sem palavras.",
    "O Wi-Fi melhora quando Walter entra na sala.",
    "Walter é o único que consegue fazer um espelho corar.",
]

# Função para piada via API
import random

def piada_walter():
    piadas = [
        "Walter foi no médico e saiu com receita de glitter e close certo!",
        "Estudos revelam: o DNA do Walter brilha sob luz negra.",
        "Walter não anda... ele desfila no calçadão de purpurina!",
        "Walter tentou entrar no armário, mas ele estava lotado de roupas da Lady Gaga.",
        "Se Walter fosse um aplicativo, ele seria o Grindr Premium com brilho ativado.",
        "Walter não sai do armário... ele faz um desfile de primavera verão.",
        "O horóscopo do Walter diz: hoje seu signo é peixes, sua vibe é Beyoncé.",
        "Walter foi no churrasco... levou tofu, glitter e Beyoncé no pendrive.",
        "Walter é tão gay que ao invés de Wi-Fi, ele conecta por arco-íris.",
        "A Alexa já entendeu que quando Walter diz 'tocar música', é show da Pabllo!",
    ]
    return random.choice(piadas)
# Função para tocar som em base64
def play_sound_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio autoplay>
                <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            </audio>
        """, unsafe_allow_html=True)
    else:
        st.error("Arquivo de som não encontrado. Walter provavelmente escondeu.")

# ========== Botões originais ==========
if st.button("Mostrar motivo científico"):
    st.info("Estudos comprovam que Walter emite 98,7% mais purpurina que o ser humano médio.")

if st.button("Teste de confirmação"):
    st.success("Walter tentou negar, mas o terminal não mente!")

if st.button("Confirmação Final"):
    st.success("Resultado do teste — Walter = Gay confirmado (100%)")

# ========== Novos Botões ==========
if st.button("Frase aleatória do Walter"):
    st.warning(random.choice(frases_walter))

if st.button("Piada aleatória sobre Walter🌈"):
    st.write(piada_walter())

if st.button("Ouvir risada do Walter"):
    play_sound_base64("sons/walter.mp3")

# ========== Botão para mostrar imagem engraçada ==========
if st.button("Ver imagem secreta do Walter 🕵️‍♀️"):
    imagem_path = "imagens/walter.jpg"
    if os.path.exists(imagem_path):
        st.image(imagem_path, caption="Walter capturado em modo gayzisse total 👀✨")
    else:
        st.warning("Imagem não encontrada. Walter provavelmente deletou do Instagram.")
# ========== Gráfico divertido ==========
st.subheader("Nível de Gayzisse por dia da semana 💖")

dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
nivel = [random.randint(50, 100) for _ in dias]

fig, ax = plt.subplots()
ax.bar(dias, nivel, color='hotpink')
ax.set_ylabel("Intensidade (%)")
ax.set_title("Gayzisse Semanal de Walter")

st.pyplot(fig)
