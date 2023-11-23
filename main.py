import telebot
from extensions import *
from Parcer import *
from bot_token import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Приветствую! ' + str(message.chat.first_name)) # send_message - отправка сообщения в чат
    bot.send_message(message.chat.id, 'Введите /help, что бы узнать чем я могу Вам помочь ')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Введите /cr (currencyexchange), для того что бы узнать как с помощью бота ввести запрос на стоимость обмена валюты.') # replay_to - ответ с цитатой
    bot.reply_to(message, 'Введите /all, что бы узнать курсы валют на сегодня\n' '/usd - для курса доллара США\n' 
                     '/eur - для курса Евро\n' '/byn - для курса Белорусского рубля\n' '/kzt - для курса Казахстанского тенге\n'
                     '/try - для курса Турецкой лиры\n')

@bot.message_handler(commands=['cr'])
def currencyexchange_help(message):
    bot.send_message(message.chat.id, 'Введите валюту которую Вы хотите поменять, валюту на которую Вы хотите поменять и количество, через пробел '
                                      'Например: usd eur 10 (запрос НЕ чувствителен к регистру)')


@bot.message_handler(commands=['all'])
def send_all(message):
    bot.send_message(message.chat.id, f'{pre_print}{all_cur}')

@bot.message_handler(commands=['usd'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{usd_cur}')

@bot.message_handler(commands=['eur'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{eur_cur}')

@bot.message_handler(commands=['byn'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{byn_cur}')

@bot.message_handler(commands=['kzt'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{kzt_cur}')

@bot.message_handler(commands=['try'])
def send_usd(message):
    bot.send_message(message.chat.id, f'{pre_print}{try_cur}')


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    parts = message.text.split(' ')
    try:
        if len(parts) == 3:  # Проверяем, что сообщение содержит 3 части
            base = parts[0]
            quote = parts[1]
            amount = parts[2]

            if not amount.isdigit():
                bot.send_message(message.chat.id, 'Количество должно быть числом! Пример: USD EUR 10')
                return

            amount = int(amount)

            rate = get_currency_exchange_rate(base.upper(), quote.upper())
            # Логика по обработке результата
            if isinstance(rate, float):
                count = round(float(amount) * rate, 2)
                text = f'Основываясь на курсе FXRates -  {amount} {base.upper()} в {quote.upper()} = {count} {quote.upper()}'
            else:
                text = f'Произошла ошибка: {rate}'
            bot.send_message(message.chat.id, text)
        else:
            bot.send_message(message.chat.id, 'Неправильный формат запроса! Пример: USD EUR 10')
    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

bot.polling(none_stop=True)
