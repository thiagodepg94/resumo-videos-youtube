from pytubefix import YouTube
import os

def get_video_url():
    url = input("URL do vídeo: ")
    return url


def download_audio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream is None:
        print("Nenhum stream de áudio disponível para este vídeo.")
        return None
    output_path = audio_stream.download()
    base, ext = os.path.splitext(output_path)
    new_file = base + '.mp3'
    os.rename(output_path, new_file)
    return new_file


def main():
    url = get_video_url()
    audio_file = download_audio(url)
    if audio_file:
        print(f"Áudio baixado com sucesso: {audio_file}")
    else:
        print("Falha ao baixar o áudio.")
        

if __name__ == "__main__":
    main()
