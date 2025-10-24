from baixar_audio import url_and_download as baixar_audio
from converter_wav import convert_audio_wav as converter


def main():
    url = baixar_audio.get_video_url()
    audio_file = baixar_audio.download_audio(url)
    if audio_file:
        print(f"Áudio baixado com sucesso: {audio_file}")
    else:
        print("Falha ao baixar o áudio.")
    converted_file = converter.convert_to_wav(audio_file)
    if converted_file:
        print(f"Áudio convertido para WAV com sucesso: {converted_file}")
    else:
        print("Falha ao converter o áudio para WAV.")
        

if __name__ == "__main__":
    main()
