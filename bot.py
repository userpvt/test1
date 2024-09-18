# Настройки
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
app = ApplicationBuilder().token("7046258175:AAHPOkvHOMlW0wu6UVrJYHjRE1jHltP9uhs").build() # Токен API к Telegram

# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
    # Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(filters.TEXT, textMessage)
# Добавляем хендлеры в диспетчер
app.add_handler("hello", start_command_handler)
app.add_handler("hello", text_message_handler)
# app.add_handler(start_command_handler)
# app.add_handler(text_message_handler)
# Начинаем поиск обновлений
app.run_polling()
# Останавливаем бота, если были нажаты Ctrl + C
app.idle()