import os
import telebot
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]
telegramToken = os.environ["TELEGRAM_BOT_TOKEN"]

client = Groq(
    api_key = api_key
)

# bot object
task3 = telebot.TeleBot(telegramToken)

# start function
@task3.message_handler(['start'])
def start(message):
    task3.reply_to(message,"Welcome to My Test Bot by Harsh Malviya\n click /help command to use this bot!")

# help func
@task3.message_handler(['help'])
def help(message):
    task3.reply_to(message,'''Listing of different commands:\n/start: Welcome message\n/help: choose different commands \n You can a
                   lso use this bot as an AI Chat-Bot''')

# ai reply func
@task3.message_handler()
def ai_reply(message):
    prompt = message.text
    if prompt.lower() in ['bye','exit','quit']:
        task3.reply_to(message,"ok see you later!")
    else:
        response = client.chat.completions.create(
        messages = [
            {
                "role":"user",
                "content":prompt
            }
        ],
        model = "llama-3.3-70b-versatile"
        )
        ai_reply = response.choices[0].message.content.strip() 
        task3.reply_to(message,ai_reply)


# run the bot
print("Bot is running")
task3.polling()