import requests  # импорт библиотеки для работы с запросами

link = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current=temperature_2m,weather_code,wind_speed_10m,wind_direction_10m&wind_speed_unit=ms"

weather_codes = {  # различные вариации типов погоды
        0: "Чистое небо",
        1: "В основном ясно",
        2: "Частично облачно",
        3: "Пасмурно",
        45: "Туман",
        48: "Осаждение известкового тумана",
        51: "Легкий дождик",
        53: "Умеренный дождик",
        55: "Интенсивный дождик",
        56: "Легкий дождик со снегом",
        57: "Сильный дождик со снегом",
        61: "Легкий дождь",
        63: "Умеренный дождь",
        65: "Интенсивный дождь",
        66: "Лёгкий замерзающий снег",
        67: "Интенсивный замерзающий снег",
        71: "Лёгкий снег",
        73: "Умеренный снег",
        75: "Интенсивный снег",
        77: "Ледяные крупинки",
        80: "Незначительный ливень",
        81: "Умеренный ливень",
        82: "Сильный ливень",
        85:  "Незначительный снегопад",
        86: "Сильный снегопад"
    }
wind_directions = ("С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ")  # нормализованный вид направления ветра


def current_weather(latitude, longitude):
    """
    Получение текущего прогноза погоды

    Аргументы:
    latitude - широта
    longitude - долгота

    Возвращает:
    Температура воздуха(float), скорость ветра(float), направление ветра(str), тип погоды(str)

    Оригинальная документация:
    https://open-meteo.com/en/docs

    """

    r = requests.get(link.format(latitude, longitude)).json()["current"]  # получаем ответ от API

    temperature = r["temperature_2m"]  # температура
    wind_speed = r["wind_speed_10m"]  # скорость ветра
    wind_direction = wind_directions[int((r["wind_direction_10m"] + 22.5) // 45 % 8)]   # направление ветра
    weather_code = weather_codes[r["weather_code"]]  # тип погоды

    return temperature, wind_speed, wind_direction, weather_code
