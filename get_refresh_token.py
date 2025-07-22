import json
from google_auth_oauthlib.flow import InstalledAppFlow

with open("secrets/client_secret.json", "r") as f:
    client_secrets = json.load(f)

flow = InstalledAppFlow.from_client_config(client_secrets, scopes=["https://www.googleapis.com/auth/youtube.upload"])
creds = flow.run_console()

print("\n✅ Your refresh token:")
print(creds.refresh_token)
