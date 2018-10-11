import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheet():
    '''スプレッドシートの読み書きについての処理が入ったクラス'''
    def __init__(self, scope, auth_json, sheet_id, sheet_name):
        self.scope = scope
        self.auth_json = auth_json
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name

    def auth_sheet_api(self):
        '''スプレッドシートAPIの認証を行う'''
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.auth_json,
            self.scope
        )
        gs_cred = gspread.authorize(credentials)
        return gs_cred

    def open_worksheet(self):
        '''指定したワークシートを開いて操作できるオブジェクトを返す'''
        gs_cred = self.auth_sheet_api()
        spreadsheet = gs_cred.open_by_key(self.sheet_id)
        worksheet = spreadsheet.worksheet(self.sheet_name)
        return worksheet

