from moviepy import VideoFileClip
import os

# Caminhos das pastas
pasta_entrada = r'C:\Users\Distrito\Videos\Captures\mp4'
pasta_saida = r'C:\Users\Distrito\Videos\Captures\mp3'

# Garantir que a pasta de saída exista
os.makedirs(pasta_saida, exist_ok=True)

# Processar todos os arquivos MP4 na pasta de entrada
for nome_arquivo in os.listdir(pasta_entrada):
    if nome_arquivo.endswith(".mp4"):
        caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
        caminho_saida = os.path.join(pasta_saida, os.path.splitext(nome_arquivo)[0] + ".mp3")

        print(f"Convertendo: {nome_arquivo}")
        video = VideoFileClip(caminho_entrada)
        video.audio.write_audiofile(caminho_saida)
        video.close()

print("Conversão concluída!")
