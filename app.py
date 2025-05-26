import streamlit as st
from moviepy import VideoFileClip
import os
import tempfile

st.title("Conversor de Vídeo (.mp4) para Áudio (.mp3)")

uploaded_file = st.file_uploader("Envie um arquivo .mp4", type=["mp4"])

if uploaded_file:
    st.video(uploaded_file)

    if st.button("Converter para MP3"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(uploaded_file.read())
            temp_video_path = temp_video.name

        # Caminho temporário de saída
        temp_audio_path = temp_video_path.replace(".mp4", ".mp3")

        # Extração do áudio
        video = VideoFileClip(temp_video_path)
        video.audio.write_audiofile(temp_audio_path)
        video.close()

        # Download do resultado
        with open(temp_audio_path, "rb") as f:
            st.success("Conversão concluída!")
            st.download_button("Baixar MP3", f, file_name="audio_convertido.mp3")

        # Limpeza dos arquivos temporários
        os.remove(temp_video_path)
        os.remove(temp_audio_path)
