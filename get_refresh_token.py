import json
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

# تنظیم مسیر فایل
CLIENT_SECRET_PATH = Path("secrets/client_secret.json")

if not CLIENT_SECRET_PATH.exists():
    raise FileNotFoundError("❌ فایل client_secret.json پیدا نشد!")

# بارگذاری اطلاعات کلاینت
with open(CLIENT_SECRET_PATH, "r") as f:
    client_secrets = json.load(f)

# گرفتن دسترسی به API یوتیوب
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# اجرای جریان تایید هویت
flow = InstalledAppFlow.from_client_config(client_secrets, scopes=SCOPES)
creds = flow.run_console()

# نمایش توکن برای انتقال به GitHub Secrets
print("\n✅ Your refresh token:")
print(creds.refresh_token)

# پیشنهاد پاک‌سازی فایل بعد از گرفتن توکن
delete = input("\n🧹 آیا می‌خوای فایل client_secret.json پاک بشه؟ (yes/no): ").strip().lower()
if delete == "yes":
    CLIENT_SECRET_PATH.unlink()
    print("🗑️ فایل client_secret.json حذف شد.")
else:
    print("⚠️ فایل client_secret.json حذف نشد. حتماً بعداً دستی پاکش کن!")
