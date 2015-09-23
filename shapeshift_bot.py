#!/usr/bin/env python

import telegram
import sqlite3 as lite
import datetime
from pyshape import pyshape

tok = 'YOUR_TELEGRAM_BOT_TOKEN'

LAST_UPDATE_ID = None
s = pyshape()

con = lite.connect('/path/to/dir/db/logs.db')

def main():
    global LAST_UPDATE_ID
    bot = telegram.Bot(tok)
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None
    while True:
        shapeshift(bot)

def shapeshift(bot):
    global LAST_UPDATE_ID
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')

        if '/start' in message.lower() or '/help' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            risp = bot.sendMessage(chat_id=chat_id, text=s.help())
            writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1

        if '/coins' in message.lower() or '/coin' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            risp = bot.sendMessage(chat_id=chat_id, text=s.coins())
            writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1

        if '/alert' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            try:
                shape = message.split()
                risp = bot.sendMessage(chat_id=chat_id, text=s.alert(chat_id, shape[1], shape[2]))
                writedb(risp.to_dict())
            except:
                risp = bot.sendMessage(chat_id=chat_id, text='Error, the command is /alert <currency> <price>. Write /help if you need help.')
                writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1

        if '/market' in message.lower() or '/markets' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            try:
                shape = message.split()
                risp = bot.sendMessage(chat_id=chat_id, text=s.market(shape[1], shape[2]))
                writedb(risp.to_dict())
            except:
                risp = bot.sendMessage(chat_id=chat_id, text='Error, the command is /market <currency1> <currency2>. Write /help if you need help.')
                writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1

        if '/status' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            try:
                shape = message.split()
                risp = bot.sendMessage(chat_id=chat_id, text=s.status(shape[1]))
                writedb(risp.to_dict())
            except:
                risp = bot.sendMessage(chat_id=chat_id, text='Error, the command is /status <payment address>. Write /help if you need help.')
                writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1

        if '/price' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            try:
                shape = message.split()
                risp = bot.sendMessage(chat_id=chat_id, text=s.price(shape[1]))
                writedb(risp.to_dict())
            except:
                risp = bot.sendMessage(chat_id=chat_id, text='Error, the command is /price currency. Write /help if you need help or /coins for the list of supported currencies.')
                writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1        

        if '/shapeshift' in message.lower():
            writedb(update.message.to_dict())
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
            try:
                shape = message.split()
                address = s.shift(shape[1], shape[2], shape[3])
                if 'Error' in address:
                    risp = bot.sendMessage(chat_id=chat_id, text=address)
                    writedb(risp.to_dict())
                else:
                    risp = bot.sendMessage(chat_id=chat_id, text=address)
                    writedb(risp.to_dict())
                    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
                    bot.sendPhoto(chat_id=chat_id, photo='http://api.qrserver.com/v1/create-qr-code/?size=150x150&data='+address)
            except: 
                risp = bot.sendMessage(chat_id=chat_id, text='Error, the command is /shapeshift <currency1>, <currency2>, <address>. Write /help if you need help.')
                writedb(risp.to_dict())
            LAST_UPDATE_ID = update.update_id + 1

def writedb(mdict):
    a, b, c, d, e, f, g, h = [0,0,0,0,0,0,0,0]

    try:
        a = mdict['message_id']
    except:
        pass

    try: 
        b = mdict['from']['id']
    except:
        pass

    try:
        c = mdict['from']['username']
    except:
        pass

    try:
        d = mdict['from']['first_name']
    except:
        pass

    try:
        e = mdict['from']['last_name']
    except:
        pass

    try:
        f = mdict['text']
    except:
        pass

    try:
        g = mdict['chat']['id']
    except:
        pass
    try:
        h = datetime.datetime.fromtimestamp(int(mdict['date'])).strftime('%Y-%m-%d %H:%M:%S')
    except:
        pass

    with con: 
        cur = con.cursor()
        cur.execute("INSERT INTO log VALUES (?,?,?,?,?,?,?,?)", (a, b, c, d, e, f, g, h))

while True:
    if __name__ == '__main__':
        main()

