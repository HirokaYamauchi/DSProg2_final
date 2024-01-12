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

if __name__ == "__main__":

    # SQLiteデータベースとテーブルを作成
    create_database_table2()

    print("completed")