
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Твой токен бота
BOT_TOKEN = "7777551240:AAEQ3ziVflWlpiDONWy-Nzck5MNksbPF0GQ"

# Логика подбора меню (заглушка)
def get_menu():
    return {
        "утро": "какао + тост с джемом",
        "обед": "сырники (магазинные) + чай",
        "вечер": "творожок с бананом"
    }

# Клавиатура
reply_keyboard = [
    ["🍽 Меню", "🧃 Дай жрать"],
    ["⚙️ Настройки"]
]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Йо, это Ви. Готов к работе. Жми на кнопку или пиши команду 👇",
        reply_markup=markup
    )

# Ответ на кнопку "Меню"
async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = get_menu()
    text = "📒 Меню на сегодня:\n"
    for k, v in menu.items():
        text += f"🍽 {k.capitalize()}: {v}\n"
    await update.message.reply_text(text)

# Ответ на кнопку "Дай жрать"
async def handle_alt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = get_menu()
    text = "🧃 Держи меню, пока ты не сгрызла мышку:\n"
    for k, v in menu.items():
        text += f"{k.capitalize()}: {v}\n"
    await update.message.reply_text(text)

# Ответ на "Настройки"
async def handle_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚙️ Настройки пока в разработке. Но скоро можно будет сказать боту: я дома, я не готовлю, я голодный зверь.")

# Обработка всех сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🍽 Меню":
        await handle_menu(update, context)
    elif text == "🧃 Дай жрать":
        await handle_alt(update, context)
    elif text == "⚙️ Настройки":
        await handle_settings(update, context)
    else:
        await update.message.reply_text("Я тебя понял, но пока знаю только меню и пожрать 😎")

# Запуск бота
def main():
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Бот запущен. Ждёт команд...")
    app.run_polling()

if __name__ == "__main__":
    main()
