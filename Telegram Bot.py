import telebot
import requests
import json
# Создаем экземпляр бота
bot = telebot.TeleBot('api вашего бота')
def moex(ticker):
        ticker = str(ticker)
        r = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/' + ticker + '.json'
        response = requests.get(r)
        w = response.text
        data = json.loads(w)
        for i in data['marketdata']['data']:
            if i[1] == 'TQBR':
                q = i[12]
        return 'Стоимость бумаги составляет: '+ str(q) + ' рублей.'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Я бот финансовой поддержки, отправь мне идентификатор бумаги и скажу тебе ее цену.\nНапример 'GAZP' или 'QIWI'")
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, moex(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)