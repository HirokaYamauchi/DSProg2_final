import sqlite3

def create_data_list2():
    # サンプルデータリストの作成（仮）
    data_list2 = [
        {'日付': '2023-12-03', '曜日': '日', 'screen_time': '3hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-04', '曜日': '月', 'screen_time': '3 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-05', '曜日': '火', 'screen_time': '4 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-06', '曜日': '水', 'screen_time': '4 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-07', '曜日': '木', 'screen_time': '2 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-08', '曜日': '金', 'screen_time': '2.5 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-09', '曜日': '土', 'screen_time': '5 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-10', '曜日': '日', 'screen_time': '3 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-11', '曜日': '月', 'screen_time': '1 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-12', '曜日': '火', 'screen_time': '3 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-13', '曜日': '水', 'screen_time': '1 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-14', '曜日': '木', 'screen_time': '3.5 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-15', '曜日': '金', 'screen_time': '3 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-16', '曜日': '土', 'screen_time': '1 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-17', '曜日': '日', 'screen_time': '4 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-18', '曜日': '月', 'screen_time': '2 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-19', '曜日': '火', 'screen_time': '4 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-20', '曜日': '水', 'screen_time': '2 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-21', '曜日': '木', 'screen_time': '3 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-22', '曜日': '金', 'screen_time': '5 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-23', '曜日': '土', 'screen_time': '2 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-24', '曜日': '日', 'screen_time': '1.5 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-25', '曜日': '月', 'screen_time': '2 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-26', '曜日': '火', 'screen_time': '4 hours', 'よく使うアプリ': 'Chrome'},
        {'日付': '2023-12-27', '曜日': '水', 'screen_time': '2 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-28', '曜日': '木', 'screen_time': '3 hours', 'よく使うアプリ': 'LINE'},
        {'日付': '2023-12-29', '曜日': '金', 'screen_time': '2 hours', 'よく使うアプリ': 'LINE'},
        {'日付': '2023-12-30', '曜日': '土', 'screen_time': '6 hours', 'よく使うアプリ': 'YouTube'},
        {'日付': '2023-12-31', '曜日': '日', 'screen_time': '6 hours', 'よく使うアプリ': 'YouTube'},
    ]

    return data_list2

def create_database_table2():
    # SQLiteデータベース接続
    conn2 = sqlite3.connect('weather_data.db')
    cursor2 = conn2.cursor()

    # テーブルを作成するSQLクエリ
    create_table_query2 = '''
    CREATE TABLE IF NOT EXISTS screentime (
        id INTEGER PRIMARY KEY,
        日付 TEXT NOT NULL,
        曜日 TEXT,
        screen_time TEXT,
        よく使うアプリ TEXT
    );
    '''

    # テーブルを作成
    cursor2.execute(create_table_query2)
    conn2.commit()
    conn2.close()

def insert_into_database(data_list2):
    # SQLiteデータベース接続
    conn2 = sqlite3.connect('weather_data.db')
    cursor2 = conn2.cursor()

    # データリストからデータベースにデータを入力
    for data in data_list2:
        cursor2.execute('''
        INSERT INTO screentime (日付, 曜日, screen_time, よく使うアプリ)
        VALUES (?, ?, ?, ?);
        ''', (data['日付'], data['曜日'], data['screen_time'], data['よく使うアプリ']))

    # 変更を保存して接続を閉じる
    conn2.commit()
    conn2.close()


if __name__ == "__main__":

    # データベースに挿入するデータのリストを作成
    data_list2 = create_data_list2()

    # SQLiteデータベースとテーブルを作成
    create_database_table2()

    # データをSQLiteデータベースに挿入
    insert_into_database(data_list2)

    print("completed")