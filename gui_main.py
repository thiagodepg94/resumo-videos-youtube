import tkinter as tk
from tkinter import filedialog, messagebox
from core.download_audio import download_audio
from core.convert_audio_wav import convert_to_wav
from core.transcribe_audio import transcribe_audio
from core.summarize_transcript import summarize_transcript

def iniciar_processo():
    url = entrada_url.get()
    if not url or "youtube.com" not in url:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida do YouTube.")
        return
    messagebox.showinfo("Processando", "O resumo do vídeo está sendo gerado. Isso pode levar alguns minutos...")
    audio_file = download_audio(url)
    if not audio_file:
        messagebox.showerror("Erro", "Falha ao baixar o áudio do vídeo.")
        return
    converted_file = convert_to_wav(audio_file)
    if not converted_file:
        messagebox.showerror("Erro", "Falha ao converter o áudio para WAV.")
        return
    transcript = transcribe_audio(converted_file)
    if not transcript:
        messagebox.showerror("Erro", "Falha ao transcrever o áudio.")
        return
    resumo = summarize_transcript(transcript)
    if not resumo:
        messagebox.showerror("Erro", "Falha ao resumir a transcrição.")
        return
    messagebox.showinfo("Sucesso", "Resumo gerado com sucesso!")

janela = tk.Tk()
janela.title("Resumo de Vídeos do YouTube")

tk.Label(janela, text="Insira a URL do vídeo do YouTube:").pack(pady=5)
entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(padx=10, pady=5)

tk.Button(janela, text="Gerar Resumo", command=iniciar_processo).pack(pady=10)

janela.mainloop()
