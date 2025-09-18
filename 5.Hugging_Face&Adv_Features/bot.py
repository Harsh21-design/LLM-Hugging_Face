import telebot

Token = "put you telegram api token here"

# bot object
bot = telebot.TeleBot(Token)

# start function
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to My Test Bot by Harsh Malviya")

# help function
@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,'''You can choose different commands:\n/start: Welcome message\n/help: List of all different commands \n You can a
                   lso use this bot as a Calculator - Basic Operations''')



# custom message func
# @task3.message_handler()
# def custom(message):
#     task3.reply_to(message,f"You said: {message.text}")

# calculator func
# @task3.message_handler()
# def calc(message):
#     try:
#         calculate = eval(message.text.strip())
#     except Exception as e:
#         calculate = "This can not be Evaluated!"
        
#     task3.reply_to(message,calculate)


# to run the bot
print("bot is running")
bot.polling()