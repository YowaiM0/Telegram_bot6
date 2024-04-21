from bote import TOKEN  # импорт токена
from weather import current_weather  # импорт погодного файла
import telebot  # импорт библотеки для работы с Telegram API
bot = telebot.TeleBot(TOKEN)  


@bot.message_handler(commands=["weather"])  # обработка команды /weather
def weather_command(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание Reply клавиатуры
    button = telebot.types.KeyboardButton("Поделиться местоположением", request_location=True)  
    keyboard.add(button)  # добавление кнопки к клавиатуре
    bot.send_message(message.chat.id, "Поделитесь своим местоположением", reply_markup=keyboard) 


@bot.message_handler(content_types=['location'])  # если получено местоположение
def location_handler(message):
    weather = current_weather(message.location.latitude, message.location.longitude)  
    keyboard = telebot.types.ReplyKeyboardRemove()  # убрать кнопку
    bot.send_message(message.chat.id,
                     f"""Температура: {weather[0]}°C
Скорость ветра: {weather[1]} м/с
Направление ветра: {weather[2]}
Тип погоды: {weather[3]}""",
                     reply_markup=keyboard)  # отправить погоду


if __name__ == '__main__':
    bot.infinity_polling()  
