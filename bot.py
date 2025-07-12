import os
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import filters
import schedule
import time

# Получаем токен и chat_id из переменных окружения
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Создаем объект бота
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Сообщение, которое бот будет отправлять
message = "Привет, это твой Crunk-бот, который будет присылать тебе обновления!"

# Функция для отправки сообщения
def send_message():
    bot.send_message(chat_id=CHAT_ID, text=message)

# Планируем отправку сообщения каждый день в 5:00 утра
schedule.every().day.at("05:00").do(send_message)

# Бесконечный цикл для выполнения задачи по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)
