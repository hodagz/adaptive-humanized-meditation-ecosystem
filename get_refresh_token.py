import json
from google_auth_oauthlib.flow import InstalledAppFlow

# بارگذاری client_secret
with open("secrets/client_secret.json", "r") as f:
    client_config = json.load(f)

# ایجاد جریان احراز هویت
flow = InstalledAppFlow.from_client_config(
    client_config,
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

# اجرای جریان تأییدیه به صورت کنسولی
creds = flow.run_console()

# نمایش refresh_token برای ذخیره در secrets
print("\n✅ Your refresh token:")
print(creds.refresh_token)
