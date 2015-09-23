#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('./db/alert.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS alert")
c.execute('''CREATE TABLE alert (chat_id text, created_time text, price text, currency text, sent text, updown text)''')
conn.commit()
c.close()