from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
import logic

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
flag = 0
U_DATA = range(1)


def start(update, context):
    global flag
    flag = 0
    update.message.reply_text(
        'Привет! Играем в игру "Быки и коровы". Я загадаю слово, ты должен его отгадать:'
        'пишешь слово если одна из букв есть и она стоит на верном месте, я отвечу 1 бык,'
        'если буква в слове есть, но она стоит в другом месте, я отвечу 1 корова.' 
        'Если согласен укажи число букв в слове от 3 до 5')


def message(update, context):
    global flag
    if flag != 1:
        num = update.message.text
        if not num.isdigit(): 
            context.bot.send_message(update.effective_chat.id, 'Это не число!')
        elif int(num) < 3 or int(num) > 5:
            context.bot.send_message(update.effective_chat.id, 'Я сказал от 3 до 5!')
        else:
            secret_word = logic.change_word(int(num))
            context.user_data[U_DATA] = secret_word
            print(context.user_data[U_DATA])
            context.bot.send_message(update.effective_chat.id, f'Отлично! Я загадал слово из {num} букв.'
            'Угадывай!')
            flag = 1
    else:
        word = update.message.text
        print(word)
        res = logic.solution(word, context.user_data[U_DATA])
        if res[0] == len(context.user_data[U_DATA]):
            context.bot.send_message(update.effective_chat.id, 'Молодец! Ты угадал слово!')
        else:
            context.bot.send_message(update.effective_chat.id, f'{res[0]} бык, {res[1]} коров')
            
            
        
start_handler = CommandHandler('start', start)#/start
message_handler = MessageHandler(Filters.text, message)#сама игра



dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()