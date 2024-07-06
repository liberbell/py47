from google.oauth2.service_account import Credentials
import gspread

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'service_account.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

SP_SHEET_KEY = '1C-278Mp-exInLJ1jpkaienNeAjXUNRGmEI_-T5jSH10'

sh = gc.open_by_key(SP_SHEET_KEY)