'''
Вынос функций которые дергаются CallBack, и выводят в телегу ссылки на чаты категорий
'''
def home_remodeling(bot, update):
    msg_txt = 'https://t.me/joinchat/F_WOpxElLB7VAGST8O8ZkA'

    bot.send_message(chat_id=update.callback_query.message.chat_id,
                     text=msg_txt)

def auto_repair(bot, update):
    msg_txt = 'https://t.me/joinchat/F_WOp09R685MczvUhQuYEw'
    bot.send_message(chat_id=update.callback_query.message.chat_id,
                     text=msg_txt)

def repair_appliances(bot, update):
    msg_txt = 'https://t.me/joinchat/F_WOp1EC7SEPhdddGcLxVA'
    bot.send_message(chat_id=update.callback_query.message.chat_id,
                     text=msg_txt)

def cargo_transportation(bot, update):
    msg_txt = 'https://t.me/joinchat/F_WOp0W_lN_8h-8oo5--Jw'
    bot.send_message(chat_id=update.callback_query.message.chat_id,
                     text=msg_txt)