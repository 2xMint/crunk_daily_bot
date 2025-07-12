import os
import telegram
import schedule
import time
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Filters
from datetime import datetime
import requests

# Получаем переменные окружения
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Создаём экземпляр бота
bot = telegram.Bot(token=TOKEN)

# Тема, текст и описание (простой пример, нужно добавить больше логики для автоматизации)
def send_message():
    topic = "Crunk Music Today!"
    message = "Сегодня в нашем плане: рассказ о важности crunk-музыки в истории. Сегодня мы будем говорить о Lil Jon."
    description = "Crunk music — это стиль, который родился в Атланте и стал важным элементом южной рэп-культуры."

    # Отправляем сообщение в чат
    bot.send_message(chat_id=CHAT_ID, text=f"{topic}\n\n{message}\n\n{description}")

# Функция для отправки сообщений по расписанию
def job():
    send_message()

# Настройка расписания (ежедневно в 5 утра)
schedule.every().day.at("05:00").do(job)

# Запуск бота
def main():
    # Для тестов, чтобы бот работал в фоновом режиме
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
