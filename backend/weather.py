import requests
import os

# OpenWeatherMapのAPIを利用する。(天気情報を取得できる。)
def open_weather_map_api():
    city_name = "Tokyo"
    API_KEY = os.environ.get("Open_Weather_Map_MyAPI_Key")
    # パラメーター
    params = { "q": city_name, "appid": API_KEY }

    url = "http://api.openweathermap.org/data/2.5/forecast"
    response = requests.get(url, params = params)

    data_json = response.json()
    ## JSONデータを見やすく字下げする。
    # data_json_indent = json.dumps(data_json['list'][0], indent=4)
    # print(data_json_indent)

    # 天気を英語で返す。（例 'Clouds' など）
    return data_json['list'][0]['weather'][0]['main']

def weather_get():
    today_weather_en = open_weather_map_api()
    weather_list = {
        'Clear': '晴れ',
        'Clouds': '曇り',
        'Rain': '雨',
        'Thunderstorm': '雷雨',
        'Drizzle': '霧雨',
        'Snow': '雪'
    }

    today_weather_ja = []
    # (APIから取得した)英語で記された天気情報を日本語に変換し、「today_weather_ja」変数に追加する。
    for (key, value) in weather_list.items():
        if key == today_weather_en:
            today_weather_ja.append(value)
            break

    # 上記のfor文でどれにも当てはまらなかった場合は、何らかの異常気象(Atmosphere)である。
    if len(today_weather_ja) == 0:
        today_weather_ja.append('何らかの異常気象')

    return today_weather_ja[0]