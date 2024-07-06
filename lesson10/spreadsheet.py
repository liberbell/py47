from google.oauth2.service_account import Credentials
import gspread

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'path/to/the/downloaded/file.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)