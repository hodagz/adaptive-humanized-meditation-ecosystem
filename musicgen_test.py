# musicgen_test.py

import torch
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import soundfile as sf
import numpy as np
from datetime import datetime
import os
import sys
import traceback

def log(msg):
    print(f"[LOG] {msg}")

try:
    # تنظیمات
    model_id = "facebook/musicgen-small"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    log(f"🎵 Using device: {device}")

    processor = AutoProcessor.from_pretrained(model_id)
    model = MusicgenForConditionalGeneration.from_pretrained(model_id).to(device)

    # متن ورودی
    prompt = "A relaxing, soothing ambient melody with soft pads and calm rhythm, instrumental only."
    inputs = processor(text=[prompt], return_tensors="pt").to(device)

    # تولید موسیقی
    log("🎼 Generating music...")
    audio_values = model.generate(**inputs, max_new_tokens=1024)

    # بررسی خروجی
    if audio_values is None or len(audio_values) == 0:
        raise RuntimeError("No audio was generated.")

    audio = audio_values[0].detach().cpu().numpy()
    log(f"📏 Original shape: {audio.shape}")

    # تغییر شکل در صورت نیاز
    if audio.ndim == 2:
        audio = audio[0]
    elif audio.ndim != 1:
        raise ValueError("Unsupported audio shape. Expected 1D or 2D array.")

    # نرمال‌سازی و تبدیل نوع داده
    max_val = np.max(np.abs(audio))
    if max_val == 0:
        raise ValueError("Audio contains only zeros.")
    audio = (audio / max_val).astype(np.float32)

    # استخراج sample rate از کانفیگ مدل
    try:
        sample_rate = model.config.audio_encoder.sampling_rate
    except:
        sample_rate = 32000  # fallback
        log("⚠️ Warning: Could not read sample rate from model config. Using default 32000.")

    # مسیر ذخیره فایل
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = os.path.join(output_dir, f"relaxing_music_{now}.wav")

    # ذخیره فایل
    sf.write(output_path, audio, samplerate=sample_rate)
    log(f"✅ Music saved at: {output_path}")

except Exception as e:
    log("❌ Error occurred:")
    traceback.print_exc()
    sys.exit(1)
