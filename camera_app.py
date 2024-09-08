import streamlit as st
import streamlit.components.v1 as components

# Função para capturar imagem da câmera via JavaScript
camera_component = """
<script>
    let video = document.createElement('video');
    let canvas = document.createElement('canvas');
    let stream;

    function startCamera() {
        navigator.mediaDevices.getUserMedia({ video: true }).then(s => {
            stream = s;
            video.srcObject = stream;
            video.play();
        });
    }

    function capturePhoto() {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0);
        let imageData = canvas.toDataURL('image/png');
        return imageData;
    }

    function stopCamera() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
        }
    }

    function sendCaptureToStreamlit() {
        let photo = capturePhoto();
        streamlit.setComponentValue(photo);
    }

    // Start the camera when the script loads
    startCamera();
</script>
"""

# Criando o componente de câmera
photo_data = components.declare_component("camera_input", camera_component, default="")

# Exibir a câmera na interface do usuário
st.write("Clique no botão abaixo para capturar a imagem da câmera.")

# Botão para capturar a imagem
if st.button("Tirar Foto"):
    components.html(
        """
        <script>
            sendCaptureToStreamlit();
        </script>
        """,
        height=0,
    )

# Exibir a imagem capturada, se disponível
if photo_data:
    st.image(photo_data, caption="Foto Capturada", use_column_width=True)
