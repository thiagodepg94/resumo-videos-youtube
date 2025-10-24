from baixar_audio import url_and_download as baixar_audio


def main():
    url = baixar_audio.get_video_url()
    audio_file = baixar_audio.download_audio(url)
    if audio_file:
        print(f"Áudio baixado com sucesso: {audio_file}")
    else:
        print("Falha ao baixar o áudio.")
        

if __name__ == "__main__":
    main()
