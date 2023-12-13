'''pip3 install pytelegrambotapi'''

import telebot

from decouple import config

token = config('token')


bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)


# @bot.message_handler(commands=['start', 'hello', 'test'])
# def start_message(message):
#     print(message)
#     print(message.chat.id)
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=keyboard)
#     bot.register_next_step_handler(message, reply_to_button)

# def reply_to_button(message):
#     # print(message)
#     if message.text == 'Да':
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEK9HJleUNiLLPt1xkMA_t5kxPga8AwCQACPwADRA3PF9DSZQlnrX8SMwQ')
#     elif message.text == 'Нет':
#         bot.send_message(message.chat.id, 'Пока')
#     else:
#         bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=keyboard)
#         bot.register_next_step_handler(message, reply_to_button)


# keyboard = telebot.types.InlineKeyboardMarkup()
# button1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
# button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')

# keyboard.row(button1, button2)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call: True)
# def handler_callback(call):
#     print(call)
#     if call.data == 'yes':
#         bot.send_message(call.message.chat.id, 'Продолжим')
#     elif call.data == 'no':
#         pass

@bot.message_handler(content_types=['sticker', 'text'], func=lambda message: True)
def start_message(message):
    # print(message)
    bot.send_message(message.chat.id, 'Привет')
    if message.sticker:
        bot.send_sticker(message.chat.id, message.sticker.file_id)


bot.polling()
