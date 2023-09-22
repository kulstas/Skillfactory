import telebot

TOKEN =  '6317181784:AAFknXVQ8oCJPyhgy99yKzeDQA5B72EDrBA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.chat.first_name}')

@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У тебя красивый голос!')

@bot.message_handler(content_types=['photo'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


bot.polling(none_stop=True)  # бот должен стараться не прекращать работу при возникновении каких-либо ошибок.
