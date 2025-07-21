# musicgen_test.py

import torch
from transformers import MusicgenForConditionalGeneration, AutoProcessor
from datetime import datetime
import os
import numpy as np
from scipy.io.wavfile import write as write_wav

# تنظیمات
model_id = "facebook/musicgen-small"
device = "cuda" if torch.cuda.is_available() else "cpu"

# بارگذاری مدل و پردازشگر
processor = AutoProcessor.from_pretrained(model_id)
model = MusicgenForConditionalGeneration.from_pretrained(model_id).to(device)

# متن راهنمای تولید موسیقی
prompt = "A relaxing, soothing ambient melody with soft pads and calm rhythm, instrumental only."
inputs = processor(text=[prompt], return_tensors="pt").to(device)

# تولید موسیقی
audio_values = model.generate(**inputs, max_new_tokens=1024)

# آماده‌سازی برای ذخیره‌سازی
audio = audio_values[0].cpu().numpy()
audio = audio / np.max(np.abs(audio))  # نرمال‌سازی بین -1 و 1
audio = (audio * 32767).astype(np.int16)  # تبدیل به int16

# ساخت پوشه خروجی
os.makedirs("outputs", exist_ok=True)

# ذخیره فایل WAV
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_path = f"outputs/relaxing_music_{now}.wav"
write_wav(output_path, 32000, audio)

print(f"✅ فایل موسیقی با موفقیت ساخته شد: {output_path}")
