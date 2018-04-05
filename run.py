'''
Бот представляет из себе небольшой путеводитель.
'''

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import show_links
import logging
import os


TOKEN = os.environ['TOKEN_BOT']


updater = Updater(token=TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)



def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def get_general_menu():
    kb_master_customer = []
    kb_master_customer.append([InlineKeyboardButton('Мастер', callback_data='master')])
    kb_master_customer[0].append(InlineKeyboardButton('Заказчик', callback_data='customer'))
    return InlineKeyboardMarkup(kb_master_customer)

def get_master_menu():
    kb_master_menu = []
    kb_master_menu.append([InlineKeyboardButton('Авторемонт', callback_data='auto_repair')])
    kb_master_menu.append([InlineKeyboardButton('Ремонт бытовой техники', callback_data='repair_appliances')])
    kb_master_menu.append([InlineKeyboardButton('Грузоперевозки', callback_data='cargo_transportation')])
    kb_master_menu.append([InlineKeyboardButton('Ремонт по дому', callback_data='home_remodeling')])
    return InlineKeyboardMarkup(kb_master_menu)

def get_customer_menu():
    return get_master_menu()

def get_knowledge_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton('Познакомиться', callback_data='get_general_menu')]])

def start(bot, update):
    #bot.send_message(chat_id=update.message.chat_id,
    #                 text='Выберите категрию', reply_markup=get_kbd())
    
    msg_txt = (f'Привет, {update.message.chat.username}! Меня зовут Глория. '
               'Я помогу тебе разобраться в крупнейшем в Приморье сообществе Мастеров, '
               'оказывающих различные услуги Населению, от электрики до ремонта твоего авто.'
               'С моей помощью ты сможешь получить доступ к чатам сообщества, базе участников, '
               'а так же к дополнительным и уникальным функциям!')

    update.message.reply_text(msg_txt, reply_markup=get_knowledge_menu())
    #update.message.reply_text(msg_txt, reply_markup=get_general_menu())

def general_menu(bot, update):
    msg_txt = ('Ты можешь получить быстрый доступ к голосованию или познакомиться со мной, '
               'получить доступ к чатам и базе участников сообщества.'
               'Подскажи, ты Заказчик или Мастер?')

    bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                 message_id=update.callback_query.message.message_id,
                                 text=msg_txt, reply_markup=get_general_menu())

    
    #bot.send_message(chat_id=update.callback_query.message.chat_id,
    #                 text=msg_txt, reply_markup=get_general_menu())

def master(bot, update):
    msg_txt = ('Отлично, нам нужны хорошие специалисты своего дела! У меня для тебя есть много полезного и интересного :)'
              '\nКакая у тебя сфера деятельности?')
    
    bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                 message_id=update.callback_query.message.message_id,
                                 text=msg_txt, reply_markup=get_master_menu())

    #bot.send_message(chat_id=update.callback_query.message.chat_id,
    #                 text=msg_txt, reply_markup=get_master_menu())


def customer(bot, update):
    msg_txt = 'Надеюсь тебе понравятся наши Мастера, незабудь оставить отзыв об их работе, это важно для тех кто будет обращаться к ним в дальнейшем.'

    bot.edit_message_text(chat_id=update.callback_query.message.chat_id,
                                 message_id=update.callback_query.message.message_id,
                                 text=msg_txt, reply_markup=get_customer_menu())
    #bot.send_message(chat_id=update.callback_query.message.chat_id,
    #                 text=msg_txt, reply_markup=get_customer_menu())


#def stub(bot, update):
#    bot.send_message(chat_id=update.callback_query.message.chat_id,
 #                    text='stub is run...')
    #bot.send_message(chat_id=update.callback_query.message.chat_id,
    #                 text=update.callback_query.data)
    

def main():    
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)    
    dispatcher.add_handler(start_handler)    
    dispatcher.add_handler(CallbackQueryHandler(master, pattern='master'))
    dispatcher.add_handler(CallbackQueryHandler(customer, pattern='customer'))
    dispatcher.add_handler(CallbackQueryHandler(general_menu, pattern='get_general_menu'))    

    dispatcher.add_handler(CallbackQueryHandler(show_links.home_remodeling, pattern='home_remodeling'))
    dispatcher.add_handler(CallbackQueryHandler(show_links.auto_repair, pattern='auto_repair'))
    dispatcher.add_handler(CallbackQueryHandler(show_links.repair_appliances, pattern='repair_appliances'))
    dispatcher.add_handler(CallbackQueryHandler(show_links.cargo_transportation, pattern='cargo_transportation'))
    #dispatcher.add_handler(CallbackQueryHandler(stub,
    #                pattern='auto_repair|repair_appliances|cargo_transportation'))    

    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

