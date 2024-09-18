# Настройки
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
app = ApplicationBuilder().token("7046258175:AAHPOkvHOMlW0wu6UVrJYHjRE1jHltP9uhs").build() # Токен API к Telegram
# Обработка команд
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name} пообщаемся?')
# Добавляем хендлеры в диспетчер
app.add_handler(CommandHandler("start", hello))
# Начинаем поиск обновлений
app.run_polling()(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
app.idle()