from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive' ]

def auth():
   
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds
def upload_file(file_path:str):
    if not os.path.exists(file_path):
        print(f"file path {file_path} does not exist")
        return
    

    service = build('drive', 'v3', credentials=auth())
    mime_type = "application/vnd.google-apps.spreadsheet"
    try:
        file_metadata = { 
            "name": os.path.basename(file_path).replace(".csv", ""),
            "mimeType": mime_type
            }
        media = MediaFileUpload(file_path, mimetype="text/csv")

        service.files().create(
            body=file_metadata, 
            media_body=media,
            fields = 'id').execute()

        print(f"File {os.path.basename(file_path)} successfully uploaded to Google Drive")
        return

    except Exception as err:
        print(err)
        return

if __name__ == '__main__':
    upload_file('./wiki.csv')