# インストールしたパッケージのインポート
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app, support_credentials=True)

# Botの応答文字列を生成し返却する
@app.route('/chat', methods=["GET"])
@cross_origin(supports_credentials=True)
def chat():

    return jsonify({'success': 'おはよう'}), 200
    

@app.route('/new')
def new():
    return 'New'

if __name__ == '__main__':
    # 作成したappを起動
    # ここでflaskの起動が始まる
    app.run(host='0.0.0.0', port='5000', debug=True)

    # FLASK_APP=main.py FLASK_ENV=development flask run でも起動できる。
    # 上記のコードの場合、テンプレートが変更されると自動的にサーバーを再起動してくれる。