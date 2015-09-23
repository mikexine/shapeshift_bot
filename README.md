# @shapeshift_bot


Hello! This is the code used by [@shapeshift_bot](https://telegram.me/shapeshift_bot), through Telegram's Bot API. You can easily run your own @shapeshift_bot! Read this small tutorial.

----------

## Installing your own @shapeshift_bot

What you need:
 
 - Install Python and Git. 
 - Install [python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot), it is published here on GitHub by [leandrotoledo](https://github.com/leandrotoledo).
 - Type `git clone https://github.com/mikexine/shapeshift_bot.git` in your terminal and then `cd shapeshift_bot`.
 - Talk to [BotFather](https://telegram.me/BotFather) on Telegram, create a Bot API Token and save it. 
 - Edit the  `shapeshift_bot.py` file at line 8; instead of `YOUR_TELEGRAM_BOT_TOKEN` insert the Bot API Token obtained by BotFather.
 - Edit the `shapeshift_bot.py` file at line 13; you must insert the current working directory. If you want to check it, type `pwd` in your terminal. The whole path should be the output of `pwd` command followed by `/db/logs.db`.
 - Edit the `pyshape.py` file at line 104; you must insert the current working directory. If you want to check it, type `pwd` in your terminal. The whole path should be the output of `pwd` command followed by `/db/alert.db`.
 - Edit the `shape.sh` file, in lines 13-18. A clear explanation of what you should do is here: [scphillips.com blog post](http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/). You'll need to do also `sudo cp shape.sh /etc/init.d/` and (if you want to run the bot at startup)  `sudo update-rc.d shape.sh defaults` - but check the linked blog post, as it is explained more clearly.
 - Run `python db/createdb_logs.py`and `python db/createdb_alert.py`.

If everything went well, you're ready to run your bot! 

----------

## Running your own @shapeshift_bot

It's really simple! Just type `sudo service shape.sh start` to start the bot. 
Available commands: 

- `sudo service shape.sh start` - start the bot. 

- `sudo service shape.sh status` - check the bot's status.

- `sudo service shape.sh stop` - stop the bot.

You can customize your bot through BotFather: here you can add a profile picture, a description and an about text, you can insert the commands supported by your bot so they will be shown to users in a chat with your bot.. 

----------

## Troubles and contributing
The `/alert <currency> <price>` command is still under development. 

Feel free to contribute to this repository, if you want to help! 

If you need help, you can contact me through Telegram at [@mikexine](https://telegram.me/mikexine) (preferred way) or you can also write me an email at [mikexine@gmail.com](mailto:mikexine@gmail.com). 

----------

## Various
I would like to thank the authors of the resources that I linked (python-telegram-bot and the blog post on scphillips.com).

In the API calls to ShapeShift, I left my Public API Key - [you can't do much with it](https://shapeshift.io/affiliate.html). 

The CoinCap API doesn't work very well, and sometimes, randomly, the bot gets an error. I don't know why, yet.

Tips are always welcome at [3JqfcRSK49EuR9TitAz7YAgTrdifahun6D](bitcoin:3JqfcRSK49EuR9TitAz7YAgTrdifahun6D) but if you have some spare time, I'll be much much happier if you contact me on Telegram or if you send me an email with some feedback or some suggestion on how to improve the current code (which might be a bit messy and dirty). 

Oh, last thing, license. I don't care much, you can do whatever you want with this code, just don't hold me responsible for any problems that you might encounter. You should respect the python-telegram-bot license. 

Thanks for reading all the readme, bye!