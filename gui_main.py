import tkinter as tk
from tkinter import ttk, messagebox
import os
from core.download_audio import download_audio
from core.convert_audio_wav import convert_to_wav
from core.transcribe_audio import transcribe_audio
from core.summarize_transcript import summarize_transcript

# ===========================
# Funções de controle
# ===========================

def iniciar_processo():
    url = entrada_url.get()
    if not url or "youtube.com" not in url:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida do YouTube.")
        return
    
    btn_gerar.config(state="disabled")
    status_label.config(text="Processando... isso pode levar alguns minutos.")
    janela.update_idletasks()

    try:
        audio_file = download_audio(url)
        converted_file = convert_to_wav(audio_file)
        transcript = transcribe_audio(converted_file)
        resumo = summarize_transcript(transcript)
        status_label.config(text="Resumo gerado com sucesso!")
        messagebox.showinfo("Sucesso", "Resumo gerado com sucesso!")
    except Exception as e:
        status_label.config(text="Erro ao gerar resumo.")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    finally:
        btn_gerar.config(state="normal")


def abrir_pasta():
    pasta = os.path.abspath('downloads')
    os.startfile(pasta) # Abre a pasta no Explorador de Arquivos do Windows


# ===========================
# Interface Gráfica
# ===========================

janela = tk.Tk()
janela.title("Resumo de Vídeos do YouTube")
janela.geometry("550x320")
janela.resizable(False, False)

# Tema moderno do ttk
style = ttk.Style(janela)
style.theme_use('clam')
style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=6)
style.configure('TLabel', font=('Segoe UI', 10))
style.configure('Title.TLabel', font=('Segoe UI', 14, 'bold'))

# ===========================
# Layout
# ===========================

frame = ttk.Frame(janela, padding=20)
frame.pack(expand=True, fill='both')

ttk.Label(frame, text='Resumo de Vídeos do YouTube', style='Title.TLabel').pack(pady=(0, 10))
ttk.Label(frame, text='Insira a URL do vídeo do YouTube:').pack(anchor='w')

entrada_url = ttk.Entry(frame, width=60)
entrada_url.pack(pady=5)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=15)

btn_gerar = ttk.Button(btn_frame, text='Gerar Resumo', command=iniciar_processo)
btn_gerar.grid(row=0, column=0, padx=5)

btn_abrir = ttk.Button(btn_frame, text='Abrir Pasta de Downloads', command=abrir_pasta)
btn_abrir.grid(row=0, column=1, padx=5)

status_label = ttk.Label(frame, text='Aguardando URL...', foreground='#555')
status_label.pack(pady=20)

# ===========================
# Rodapé
# ===========================

ttk.Separator(frame, orient='horizontal').pack(fill='x', pady=(10, 5))
ttk.Label(frame, text='Desenvolvido por Thiago Gonçalves © 2025', font=('Segoe UI', 8), foreground='#777').pack()

# ===========================
# Execução da aplicação
# ===========================

janela.mainloop()
