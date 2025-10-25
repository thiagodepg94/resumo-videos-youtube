from baixar_audio import url_and_download as baixar_audio
from converter_wav import convert_audio_wav as converter
from transcrever_audio import transcribe_audio as transcrever
from resumir_transcricao import summarize_transcript as resumir


def main():
    url = baixar_audio.get_video_url()
    audio_file = baixar_audio.download_audio(url)

    if audio_file:
        print(f"Áudio baixado com sucesso: {audio_file}")
    else:
        print("Falha ao baixar o áudio.")
        return None
    
    converted_file = converter.convert_to_wav(audio_file)

    if converted_file:
        print(f"Áudio convertido para WAV com sucesso: {converted_file}")
    else:
        print("Falha ao converter o áudio para WAV.")
        return None

    transcribed_text = transcrever.transcribe_audio(converted_file)

    if transcribed_text:
        print(f"Transcrição do áudio realizada com sucesso:")
        print(transcribed_text)
    else:
        print("Falha ao transcrever o áudio.")
        return None
    
    summary = resumir.summarize_transcript(transcribed_text)

    if summary:
        print(f"Resumo da transcrição:")
        print(summary)
    else:
        print("Falha ao resumir a transcrição.")

if __name__ == "__main__":
    main()
