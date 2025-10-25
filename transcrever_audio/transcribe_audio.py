from openai import OpenAI
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializar o cliente OpenAI com a chave da API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Função para transcrever áudio usando o modelo Whisper da OpenAI
def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        print(f'Arquivo não encontrado: {file_path}')
        return None
    
    try:
        # 1 - Transcrever com Whisper
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1"
            )
        
        text = transcription.text

        # 2 - Gerar caminho do arquivo de texto
        txt_path = file_path.rsplit('.', 1)[0] + '.txt'

        # 3 - Salvar o texto transcrito em um arquivo .txt
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
       
        return text
    
    except Exception as e:
        print(f'Erro ao transcrever áudio: {e}')
        return None
