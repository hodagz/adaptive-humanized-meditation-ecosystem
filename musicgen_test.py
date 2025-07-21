# musicgen_test.py

import torch
from transformers import MusicgenForConditionalGeneration, AutoProcessor
from datetime import datetime
import os
import numpy as np
from scipy.io.wavfile import write as write_wav

# مدل و دستگاه
model_id = "facebook/musicgen-small"
device = "cuda" if torch.cuda.is_available() else "cpu"

# بارگذاری
processor = AutoProcessor.from_pretrained(model_id)
model = MusicgenForConditionalGeneration.from_pretrained(model_id).to(device)

# متن راهنما
prompt = "A relaxing, soothing ambient melody with soft pads and calm rhythm, instrumental only."
inputs = processor(text=[prompt], return_tensors="pt").to(device)

# تولید
audio_values = model.generate(**inputs, max_new_tokens=1024)

# تبدیل به numpy array
audio = audio_values[0].cpu().numpy()  # shape: (1, samples) or (channels, samples)

# اگر خروجی چند بعدی بود، فقط یکی رو بردار
if audio.ndim == 2:
    audio = audio[0]

# نرمال‌سازی و تبدیل به int16
audio = audio / np.max(np.abs(audio))  # normalize to -1 ~ 1
audio = (audio * 32767).astype(np.int16)

# ساخت مسیر خروجی
os.makedirs("outputs", exist_ok=True)
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_path = f"outputs/relaxing_music_{now}.wav"

# ذخیره
write_wav(output_path, 32000, audio)

print(f"✅ موسیقی ذخیره شد: {output_path}")
