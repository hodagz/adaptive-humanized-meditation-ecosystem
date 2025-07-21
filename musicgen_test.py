# musicgen_test.py
import torch
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import scipy
from datetime import datetime
import os

# تنظیمات اولیه
model_id = "facebook/musicgen-small"
device = "cuda" if torch.cuda.is_available() else "cpu"

# بارگذاری مدل و پردازشگر
processor = AutoProcessor.from_pretrained(model_id)
model = MusicgenForConditionalGeneration.from_pretrained(model_id).to(device)

# متن راهنما برای تولید موسیقی
prompt = "A relaxing, soothing ambient melody with soft pads and calm rhythm, instrumental only."

# آماده‌سازی ورودی
inputs = processor(text=[prompt], return_tensors="pt").to(device)

# تولید موسیقی
audio_values = model.generate(**inputs, max_new_tokens=256)

# ذخیره فایل خروجی با تاریخ و ساعت
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
os.makedirs("outputs", exist_ok=True)
output_path = f"outputs/relaxing_music_{now}.wav"

# ذخیره‌سازی خروجی
import os
import soundfile as sf

os.makedirs("outputs", exist_ok=True)  # 🔧 مطمئن شو پوشه هست

sf.write(output_path, audio_values[0].cpu().numpy(), samplerate=32000)

print(f"✅ Music generated and saved at: {output_path}")
