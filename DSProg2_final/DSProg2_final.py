import requests
from bs4 import BeautifulSoup
import time

def scrape_weather_data(url):
    # URLからページの内容を取得
    response = requests.get(url)
    time.sleep(3)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(response.content, 'html.parser')

    # データを格納するリストを初期化
    data_list = []

    # テーブルを探す
    table = soup.find('table', {'id': 'tablefix1'})

    if not table:
        print("Table not found")
        return

    # テーブルの各行をループ処理
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 5:  # 必要な列が存在するか確認
            date = columns[0].text.strip()  # 日付
            precipitation = columns[3].text.strip()  # 降水量の合計
            avg_temp = columns[6].text.strip()  # 気温の平均
            daylight_hours = columns[16].text.strip()  # 日照時間
            weather_condition = columns[19].text.strip()  # 天気概況（昼）

            # データを辞書に格納し、リストに追加
            data = {
                '日付': date,
                '降水量': precipitation,
                '平均気温': avg_temp,
                '日照時間': daylight_hours,
                '天気概況(昼）': weather_condition
            }
            data_list.append(data)

    return data_list

def create_database_table():
    # SQLiteデータベース接続
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # テーブルを作成するSQLクエリ
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY,
        日付 TEXT NOT NULL,
        降水量 TEXT,
        平均気温 TEXT,
        日照時間 TEXT,
        天気概況_昼 TEXT
    );
    '''

    # テーブルを作成
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def insert_into_database(data_list):
    # SQLiteデータベース接続
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # データリストからデータベースにデータを入力
    for data in data_list:
        cursor.execute('''
        INSERT INTO weather (日付, 降水量, 平均気温, 日照時間, 天気概況_昼)
        VALUES (?, ?, ?, ?, ?);
        ''', (data['日付'], data['降水量'], data['平均気温'], data['日照時間'], data['天気概況(昼）']))

    # 変更を保存して接続を閉じる
    conn.commit()
    conn.close()

if __name__ == "__main__":
    url = "https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=1&view="
    weather_data = scrape_weather_data(url)
    for data in weather_data:
        print(data)
