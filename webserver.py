'''
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
ZUMBY NSR CC [...]
'''

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm online"

def run():
  app.run(host='0.0.0.0',port=xxxx)

def keep_alive():  
    t = Thread(target=run)
    t.start()
