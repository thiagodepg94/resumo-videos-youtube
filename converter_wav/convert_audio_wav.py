import ffmpeg
import os

def convert_to_wav(input_path):
    if not os.path.exists(input_path):
        print(f"O arquivo {input_path} não existe.")
        return None
    
    output_path = input_path.rsplit('.', 1)[0] + '.wav'
    (
        ffmpeg
        .input(input_path)
        .output(output_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000')
        .run(overwrite_output=True)
    )
    return output_path