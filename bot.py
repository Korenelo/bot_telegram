from watcher import *
import telebot
film_name = ''

bot = telebot.TeleBot('1521415054:AAFEtR53oTZik2hVAiTPVVJr5OtVmu_TNno');
@bot.message_handler(content_types=['text', 'document', 'audio'])
def start(message):
    if message.text == 'Додати':
        bot.send_message(message.from_user.id, "Назва фільму")
        bot.register_next_step_handler(message, input_name)
def input_name(message):
    global film_name
    film_name = message.text
    bot.send_message(message.from_user.id, "Вкажи жанр")
    bot.register_next_step_handler(message, set_film_type)
def set_film_type(message):
    categories = message.text
    add_film(film_name, categories)
bot.polling(none_stop=True, interval=0)