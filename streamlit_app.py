import streamlit as st
from streamlit_webrtc import webrtc_streamer
import deepface as DeepFace

# Função para realizar o reconhecimento facial e detectar emoções
def detect_emotion(image):
    try:
        analysis = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
        return analysis['dominant_emotion']
    except Exception as e:
        return "Erro no reconhecimento facial"

# Título
st.title("Qual é o seu sentimento atual?")

# Inicializa a câmera (ativa, mas não exibida para o usuário)
webrtc_ctx = webrtc_streamer(key="key", video_processor_factory=None, media_stream_constraints={"video": True, "audio": False}, mode="recvonly", async_processing=True)

# Exibição dos botões de sentimentos com emojis
col1, col2, col3, col4, col5 = st.columns(5)
sentimento = None

if col1.button("😀"):
    sentimento = "feliz"
if col2.button("😄"):
    sentimento = "alegre"
if col3.button("😐"):
    sentimento = "normal"
if col4.button("😕"):
    sentimento = "triste"
if col5.button("😡"):
    sentimento = "raivoso"

# Se o sentimento for escolhido, captura a foto e faz a análise
if sentimento:
    
    # Verifica se a câmera está ativa e captura o frame
    if webrtc_ctx and webrtc_ctx.video_receiver:
        frame = webrtc_ctx.video_receiver.get_frame()
        image = frame.to_ndarray(format="bgr24")

        # Processa a imagem e detecta o sentimento sem exibir a foto
        emotion = detect_emotion(image)
        st.write(f"O sentimento detectado pela análise facial é: *{emotion}*")
    else:
        st.warning("Nenhuma câmera detectada.")

