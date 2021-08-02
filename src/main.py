from .settings import BOT_TOKEN, CHAT_ID, API_TOKEN
from .models import NotificationModel
from fastapi import FastAPI
from telegram.bot import Bot


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world!'}

@app.post('/notify/')
async def notify(notification: NotificationModel):
    if notification.token != API_TOKEN:
        return {'message': 'Auth error'}
    bot = Bot(BOT_TOKEN)
    message = f"Notification from {notification.sender}: \n"
    message += f"{notification.message}"
    bot.send_message(CHAT_ID, message)
    return {'message': 'Notification sent!'}
