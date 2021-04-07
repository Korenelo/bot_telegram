from watcher import*
import telebot;
bot = telebot.TeleBot('1521415054:AAFEtR53oTZik2hVAiTPVVJr5OtVmu_TNno');
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Додати":
        bot.send_message(message.from_user.id, "Вкажи назву")
        add_film(message.text)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)