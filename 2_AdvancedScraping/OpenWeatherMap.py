import requests
import json

#   OpenWeatherMap Api key
apikey = "5c714d59a2b02d50ac21ea13b6e55004"

#   도시 설정
cities = ["Seoul, KR", "Daegu, KR"]

#   API 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

#   켈빈 온도 -> 섭씨온도
k2c = lambda k : k - 273.15

#   도시정보 추출
for name in cities :

    #   API 구성
    url = api.format(city=name, key = apikey)

    #   요청 및 추출
    response = requests.get(url)

    #   JSON 형식으로 전환
    data = json.loads(response.text)

    #   결과 출력
    print("-----------------------")
    print(" 도시 = ", data["name"])
    print(" 날씨 = ", data["weather"][0]["description"])
    print(" 최저 기온 = ", k2c(data["main"]["temp_min"]))
    print(" 최고 기온 = ", k2c(data["main"]["temp_max"]))
    print(" 습도 = ", data["main"]["humidity"])
    print(" 기압 = ", data["main"]["pressure"])
    print(" 풍향 = ", data["wind"]["deg"])
    print(" 풍속 = ", data["wind"]["speed"])
    print("")

