import requests
import json
import sqlite3
import time

help = """
/help I'm here to help you!\n
/shapeshift <currency1> <currency2> <payment address> replies with a <deposit address>. send <currency1> there and you'll get <currency2> on <payment address>. You'll get also a QR code of the <deposit address>!\n
/status <deposit address> checks the status of your transaction.\n
/coins lists all available coins on ShapeShift.\n
/market <currency1> <currency2> shows the details of a currency pair.\n
/price <currency> you'll get the USD value of one unit of <currency> ~ through CoinCap API.\n
/alert <currency> <price> set an alert to be notified when <currency> reaches <price> [WIP]\n
Rate me on @StoreBot!\n 
GitHub: https://github.com/mikexine/shapeshift_bot\n
Contact @mikexine for help, bugs, feedback & co.\n
"""


class pyshape:

    def __init__(self):
        pass

    def help(self):
        return help

    def coins(self):
        url = 'https://shapeshift.io/getcoins'
        headers = {'User-Agent': '@shapeshift_bot Telegram Bot', 'content-type': 'application/json'}
        r = requests.get(url, headers = headers, timeout = 30)
        data = r.json()
        coins = []
        try:
            for key in data:
                coins.append('- %s: %s\n' % (key, data[key]['name']))
            coins.sort()
            coins_l = '\n'
            for coin in range(len(coins)):
                coins_l = coins_l+coins[coin]
        except:
            coins_l = 'Error, retry.'
        return coins_l

    def market(self, c1, c2):
        c1c2 = c1+'_'+c2
        url = 'https://shapeshift.io/marketinfo/'+c1c2
        headers = {'User-Agent': '@shapeshift_bot Telegram Bot', 'content-type': 'application/json'}
        r = requests.get(url, headers = headers, timeout = 30)
        data = r.json()
        try:
            ok = "\nRate: %s \nDeposit max limit: %s \nDeposit min limit: %s \nMiner's fee: %s." % (data['rate'], data['limit'], data['minimum'], data['minerFee'])
        except:
            ok = 'Error, check the currency codes with /coins.'
        return ok

    def shift(self, c1, c2, add):
        url = 'https://shapeshift.io/shift'
        headers = {'User-Agent': '@shapeshift_bot Telegram Bot', 'content-type': 'application/json'}
        c1c2 = c1+'_'+c2
        params = {
            'pair' : c1c2,
            'withdrawal' : add,
            'apiKey' : 'f1a5804b969476e49574851c96e7bae75e828918941f9f078bead975f675eeae6bc101867f2f78318e21152c40d067ae68fd6ddd613c33604756d84b5eb7aa4a'
        }
        r = requests.post(url, data = json.dumps(params), headers = headers, timeout = 30)
        data = r.json()
        try:
            ok = data['deposit']
        except:
            ok = 'Error, check the currency codes with /coins and the address that you sent.'
        return ok
        
    def status(self, add):
        url = 'https://shapeshift.io/txStat/'+add
        headers = {'User-Agent': '@shapeshift_bot Telegram Bot', 'content-type': 'application/json'}
        r = requests.get(url, headers = headers, timeout = 30)
        data = r.json()
        try:
            if data['status'] == "no_deposits":
                ok = "No deposits found, check your address."
            elif data['status'] == "received":
                ok = "Deposit received, transaction in progress. You might have to wait for 1 confirmation."
            elif data['status'] == "complete":
                ok = "\nDeposit received and processed.\nReceived %s %s to %s, sent %s %s to %s, txId: %s." % (data['incomingCoin'], data['incomingType'], data['address'], data['outgoingCoin'], data['outgoingType'], data['withdraw'], data['transaction'])
            else:
                ok = "You should not see this message. Error."
        except:
            ok = 'Error, check your address'
        return ok

    def price(self, coin):
        url = 'http://www.coincap.io/page/'+coin.upper()
        headers = {'User-Agent': '@shapeshift_bot Telegram Bot', 'content-type': 'application/json'}
        r = requests.get(url, headers = headers, timeout = 30)
        data = r.json()
        try:
            ok = data['usdPrice']+' USD'
        except:
            ok = 'Error, check the currency code.'
        return ok


    def alert(self, chat_id, curr, price):
        conn = sqlite3.connect('/path/to/dir/db/alert.db')
        c = conn.cursor()
        sent = 'no'
        updown = 'up'
        created_time = str(time.time())
        c.execute("INSERT INTO alert VALUES (?,?,?,?,?,?)", (chat_id,created_time,price,curr,sent,updown))
        conn.commit()
        c.close()
        text = 'Alert for %s at %s price is now set' % (curr, price)
        return text

