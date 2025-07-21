# combine_audio.py

from pydub import AudioSegment
import os
from datetime import datetime

def combine_audio(voice_path, music_path, output_path):
    # لود کردن فایل‌ها
    print(f"🎵 Loading voice: {voice_path}")
    print(f"🎶 Loading music: {music_path}")
    voice = AudioSegment.from_file(voice_path)
    music = AudioSegment.from_file(music_path)

    # کوتاه‌سازی یا طولانی کردن موسیقی مطابق طول صدا
    if len(music) < len(voice):
        repeat_count = int(len(voice) / len(music)) + 1
        music = music * repeat_count
    music = music[:len(voice)]

    # کاهش صدای موسیقی (برای اینکه صدای گفتار واضح‌تر باشه)
    background = music - 10  # کاهش 10dB

    # ترکیب موسیقی و گفتار
    combined = background.overlay(voice)

    # ذخیره خروجی
    os.makedirs(os.path.join("outputs", "final"), exist_ok=True)
    combined.export(output_path, format="mp3")
    print(f"✅ Combined audio saved at: {output_path}")

if __name__ == "__main__":
    # مسیر فایل‌ها (آخرین فایل تولیدی را پیدا کن)
    voice_dir = "outputs/voiceovers"
    music_dir = "outputs"

    voice_files = sorted(
        [f for f in os.listdir(voice_dir) if f.endswith(".mp3")],
        key=lambda x: os.path.getmtime(os.path.join(voice_dir, x))
    )
    music_files = sorted(
        [f for f in os.listdir(music_dir) if f.endswith(".wav")],
        key=lambda x: os.path.getmtime(os.path.join(music_dir, x))
    )

    if not voice_files or not music_files:
        print("❌ No voice or music file found to combine.")
        exit(1)

    latest_voice = os.path.join(voice_dir, voice_files[-1])
    latest_music = os.path.join(music_dir, music_files[-1])

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    final_output = f"outputs/final/meditation_mix_{timestamp}.mp3"

    combine_audio(latest_voice, latest_music, final_output)
