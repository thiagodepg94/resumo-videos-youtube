from pytubefix import YouTube
import os


def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream is None:
            print("Nenhum stream de áudio disponível para este vídeo.")
            return None
        
        os.makedirs('downloads', exist_ok=True)
        output_path = audio_stream.download(output_path='downloads')

        return output_path
    
    except Exception as e:
        print(f"Erro ao baixar o áudio: {e}")
        return None