import requests

# 楽天商品検索API (BooksGenre/Search/)のURL
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

# URLのパラメータ
param = {
    # 取得したアプリIDを設定する
    "applicationId" : "1072722666659103303",
    "keyword" : "Pythonではじめる機械学習　scikit-learnで学ぶ特徴量エンジニアリングと機械学習の基礎",
    "format" : "json"
}

# APIを実行して結果を取得する
result = requests.get(url, param)

# jsonにデコードする
json_result = result.json()


for i in json_result["Items"]:
    item = i['Item']
    print("【商品名】",item["itemName"])
    print("【値段】",item["itemPrice"],"円")
    print("【URL】",item["itemUrl"])
    print()