from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_transcript(transcript):
    try:
        # 1 - Gerar resumo da transcrição usando o modelo GPT
        prompt = f"Faça um resumo claro e bem estruturado do texto abaixo, destacando os principais pontos e ideias apresentadas.\n\nTexto:\n{transcript}\n\nResumo:"
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        resumo = response.choices[0].message.content

        # 2 - Gerar o caminho do arquivo de resumo
        resumo_path = os.path.join("downloads", "resumo_transcricao.txt")

        # 3 - Salvar o resumo em um arquivo .txt
        with open(resumo_path, 'w', encoding='utf-8') as r_file:
            r_file.write(resumo)

        return resumo
    
    except Exception as e:
        print(f"Erro ao resumir a transcrição: {e}")
        return None