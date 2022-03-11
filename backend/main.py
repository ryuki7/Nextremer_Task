# インストールしたパッケージのインポート
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime
from pytz import timezone
from weather import weather_get

# appという名前でFlaskのインスタンスを作成。
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app, support_credentials=True)

# 日本(東京)の日時を生成し、返却する。
def now_datetime_jst(format):
    # タイムゾーンを指定して、日時を作成。
    now_time_jst = datetime.now(timezone('Asia/Tokyo'))
    return now_time_jst.strftime(format)

# Botの応答文字列を生成し、返却する。
@app.route('/chat', methods=["POST"])
@cross_origin(supports_credentials=True)
def chat():
    # request.get_json() => {'formData': {'user_input': 'inputValue'}}
    user_input_json = request.get_json()['formData']

    if user_input_json['user_input'] == 'こんにちは':
        bot_response = 'こんにちは。'
    elif user_input_json['user_input'] == '今何時？':
        bot_response = now_datetime_jst('%H時%M分') + 'です。'
    elif user_input_json['user_input'] == '今日の東京の天気は？':
        bot_response = weather_get() + 'です。'
    else:
        bot_response = '私にはわかりません。'

    return jsonify({ 'user_input': user_input_json['user_input'], 'bot_response': bot_response, 'response_timestamp': now_datetime_jst('%H:%M:%S') }), 200


@app.route('/', methods=["GET"])
def index():
    return 'Hello World'

if __name__ == '__main__':
    # 作成したappを起動してくれる。
    app.run()

    # FLASK_APP=main.py FLASK_ENV=development flask run でも起動できる。
    # 上記のコードの場合、テンプレートが変更されると自動的にサーバーを再起動してくれる。