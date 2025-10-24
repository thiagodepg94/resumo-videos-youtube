from pytubefix import YouTube
import os

def get_video_url():
    url = input("URL do vídeo: ")
    while "youtube.com" not in url:
        print("Por favor, insira uma URL válida do YouTube.")
        url = input("URL do vídeo: ")
    return url


def download_audio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream is None:
        print("Nenhum stream de áudio disponível para este vídeo.")
        return None
    os.makedirs('downloads', exist_ok=True)
    output_path = audio_stream.download(output_path='downloads')
    print(f"Áudio baixado em: {output_path}")
    return output_path
