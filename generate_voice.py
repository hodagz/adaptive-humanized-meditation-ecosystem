# generate_voice.py

import edge_tts
import asyncio
from datetime import datetime
import os
import random

# لیست جملات پیشنهادی (میتونه هفتگی متغیر بشه یا از فایل بیاد)
SCRIPTS = [
    "Take a deep breath in... and slowly exhale.",
    "Let your thoughts settle. Feel the calmness growing with each breath.",
    "In this moment, there is nothing to do, just be.",
    "Relax your shoulders. Unclench your jaw. Soften your gaze.",
    "With every breath, you feel lighter, calmer, more grounded.",
]

# فقط صدای طبیعی آمریکایی واقعی
VOICES = [
    "en-US-AriaNeural",  # زنانه آمریکایی
    "en-US-GuyNeural",   # مردانه آمریکایی
]

async def generate_voice(text, voice="en-US-AriaNeural", output_dir="outputs/voiceovers"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = os.path.join(output_dir, f"voice_{voice}_{timestamp}.mp3")

    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_path)

    print(f"✅ Voice generated and saved at: {output_path}")
    return output_path

if __name__ == "__main__":
    # تولید صدای حداکثر برای ۳ ویدئو در هفته
    generate_this_week = 3

    selected_scripts = random.sample(SCRIPTS, generate_this_week)

    for script in selected_scripts:
        selected_voice = random.choice(VOICES)
        print(f"🎙️ Generating voice with {selected_voice}")
        asyncio.run(generate_voice(script, voice=selected_voice))
