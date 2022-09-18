#5624019560:AAEnzkIl-B0M9Nk6BcBXBFCdIY2HqAEItq4
#t.me/d18y22_bot
import telebot
import subprocess

bot = telebot.TeleBot('5624019560:AAEnzkIl-B0M9Nk6BcBXBFCdIY2HqAEItq4')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Жду команды')
    
@bot.message_handler(commands=["df"])
def df(m, res=False):
    bot.send_message(m.chat.id, get_info())
# Получение сообщений от юзера

def get_info():
    cmd = subprocess.run(["df", "-h"], text="TEXT", stdout=subprocess.PIPE)
    cmd = cmd.stdout.split("\n")
    cmd = "".join(str(each) for each in cmd)
    return cmd
"""обработка сообщений текста
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (message.text == "df"):
        bot.send_message(message.chat.id, get_info())
"""
# Запускаем бота
bot.polling(none_stop=True, interval=0)


