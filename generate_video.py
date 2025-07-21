# generate_video.py

from moviepy.editor import *
from datetime import datetime
import os

# تنظیم مسیرها
AUDIO_FILE = "outputs/final/combined_audio.wav"  # یا relaxing_music_xx.wav اگر گفتار نیست
IMAGE_FILE = "assets/backgrounds/forest.jpg"     # برای هر ویدئو می‌تونه متفاوت باشه

# ساخت پوشه خروجی
os.makedirs("outputs/videos", exist_ok=True)

# زمان‌بندی
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
OUTPUT_FILE = f"outputs/videos/meditation_{now}.mp4"

# بارگذاری صدا
audio = AudioFileClip(AUDIO_FILE)

# بارگذاری تصویر
image = ImageClip(IMAGE_FILE).set_duration(audio.duration)

# اندازه ویدئو (برای تطبیق با شبکه‌های اجتماعی)
video = image.set_audio(audio).resize(height=720).set_fps(24)

# ذخیره خروجی
video.write_videofile(OUTPUT_FILE, codec="libx264", audio_codec="aac")
print(f"✅ Video saved at: {OUTPUT_FILE}")
