from core.download_audio import download_audio
from core.convert_audio_wav import convert_to_wav
from core.transcribe_audio import transcribe_audio
from core.summarize_transcript import summarize_transcript


def main():
    url = input("URL do vídeo do YouTube: ")

    while "youtube.com" not in url:
        print("Por favor, insira uma URL válida do YouTube.")
        url = input("URL do vídeo do YouTube: ")

    if not url:
        return None
    
    print('\n[1/5] Baixando o áudio do vídeo...')
    audio_file = download_audio(url)

    if audio_file:
        print(f"Áudio baixado com sucesso: {audio_file}")
    else:
        return None
    
    print('\n[2/5] Convertendo o áudio para WAV...')
    converted_file = convert_to_wav(audio_file)

    if converted_file:
        print(f"Áudio convertido para WAV com sucesso: {converted_file}")
    else:
        return None

    print('\n[3/5] Transcrevendo o áudio...')
    transcribed_text = transcribe_audio(converted_file)

    if transcribed_text:
        print(f"Transcrição do áudio realizada com sucesso:")
        print(transcribed_text)
    else:
        return None
    
    print('\n[4/5] Gerando resumo do conteúdo...')
    summary = summarize_transcript(transcribed_text)

    if summary:
        print(f"Resumo da transcrição:")
        print(summary)
    else:
        return None
    
    print('\nProcesso concluído com sucesso! Verifique a pasta "downloads" para os arquivos gerados.')

if __name__ == "__main__":
    main()
