# get_refresh_token.py

from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Load client secret
with open("secrets/client_secret.json", "r") as f:
    client_config = json.load(f)

flow = InstalledAppFlow.from_client_config(
    client_config,
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

creds = flow.run_local_server(port=0)
print("\n✅ Your refresh token:")
print(creds.refresh_token)
