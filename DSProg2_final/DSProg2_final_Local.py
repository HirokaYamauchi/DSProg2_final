import sqlite3

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

    # SQLiteデータベースとテーブルを作成
    create_database_table2()

    print("completed")