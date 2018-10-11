import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

# 認証情報のJSONファイル
json_file = 'test-spredsheet-e2b733f1b31a.json'

# スプレッドシートID
sheet_id = '13Q54b4eabxim_kwH8GSTF06hNnkHp6PXpPjJoUdCw_o'

# スプレッドシートのシート名
sheet_name = 'シート1'

# 認証
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file, scope
    )
gc = gspread.authorize(credentials)

# シート情報を読み込む
sp = gc.open_by_key(sheet_id)
wks = sp.worksheet(sheet_name)

# wks.update_acell('A1', "A1セルに書き込みます。")
wks.append_row(['テスト', 'テストだよん', 'テストテスト'], value_input_option='RAW')
