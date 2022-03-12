# インストールしたパッケージのインポート
from flask import Flask, request, jsonify
from database import init_db
from flask_cors import CORS, cross_origin
from datetime import datetime
from pytz import timezone
from weather import weather_get
from models import Chatbot
from database import db

def create_app():
    # appという名前でFlaskのインスタンスを作成。
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config["JSON_AS_ASCII"] = False
    CORS(app, support_credentials=True)

    init_db(app)

    return app

app = create_app()

# 応答したデータの履歴を保存する。
def chat_history_db_save(user_input, bot_response, response_timestamp):
    chatbot = Chatbot()
    chatbot.user_input = user_input
    chatbot.bot_response = bot_response
    chatbot.response_timestamp = response_timestamp
    db.session.add(chatbot)
    db.session.commit()

# Botとの会話（Botの応答文字列を生成し、返却する。）
@app.route('/chat', methods=["POST"])
@cross_origin(supports_credentials=True)
def chat():
    # 日本(JST)の日時を生成する。
    now_time_jst = datetime.now(timezone('Asia/Tokyo'))
    # request.get_json() => {'formData': {'user_input': 'inputValue'}}
    user_input_json = request.get_json()['formData']

    if user_input_json['user_input'] == 'こんにちは':
        bot_response = 'こんにちは。'
    elif user_input_json['user_input'] == '今何時？':
        bot_response = now_time_jst.strftime('%H時%M分') + 'です。'
    elif user_input_json['user_input'] == '今日の東京の天気は？':
        bot_response = weather_get() + 'です。'
    else:
        bot_response = '私にはわかりません。'

    response_json = {
        'user_input': user_input_json['user_input'],
        'bot_response': bot_response,
        'response_timestamp': now_time_jst.strftime('%H:%M:%S')
    }

    chat_history_db_save(user_input_json['user_input'], bot_response, now_time_jst.strftime('%Y-%m-%dT%H:%M:%S'))

    return jsonify(response_json), 200

# 履歴一覧の取得
@app.route('/history/list', methods=["GET"])
def index():
    return "histroy list"

if __name__ == '__main__':
    # 作成したappを起動してくれる。
    app.run()

    # FLASK_APP=main.py FLASK_ENV=development flask run でも起動できる。
    # 上記のコードの場合、テンプレートが変更されると自動的にサーバーを再起動してくれる。