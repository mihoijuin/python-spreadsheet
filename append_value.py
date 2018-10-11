from spread_sheet import SpreadSheet

if __name__ == '__main__':
    #  スプレッドシートを扱うための情報を作成してく
    scope = [   # スコープを規定
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    auth_json = 'test-spredsheet-e2b733f1b31a.json'     # 認証情報の入ったJSONファイル
    sheet_id = '13Q54b4eabxim_kwH8GSTF06hNnkHp6PXpPjJoUdCw_o'   # スプレッドシートID
    sheet_name = 'シート1'      # スプレッドシートのシート名

    # SpreadSheetクラスを使用してインスタンスを生成し、シートの情報を読み込む
    sheet = SpreadSheet(scope, auth_json, sheet_id, sheet_name)

    # ワークシート情報を取得
    worksheet = sheet.open_worksheet()

    # wks.update_acell('A1', "A1セルに書き込みます。")
    worksheet.append_row(['テスト', 'テストだよん', 'テストテスト'], value_input_option='RAW')
