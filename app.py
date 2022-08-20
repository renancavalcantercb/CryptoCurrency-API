from flask import Flask
from api import *

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Welcome to the Bombcrypto Tokens API'


@app.route('/api/bcoin', methods=['GET'])
def getValueBcoin():
    listValuesBcoin = Crypto('bomber-coin', ['brl', 'usd'], True).crypto_price()
    return listValuesBcoin


@app.route('/api/bcoin-chart', methods=['GET'])
def getValueBcoinChart():
    listValuesBcoinChart = Crypto('bomber-coin', ['brl', 'usd'], True, True).crypto_price()
    return listValuesBcoinChart


@app.route('/api/sens', methods=['GET'])
def getValueSENS():
    listValuesSENS = Crypto('senspark', ['brl', 'usd'], True).crypto_price()
    return listValuesSENS


@app.route('/api/sens-chart', methods=['GET'])
def getValueSENSChart():
    listValuesSENSChart = Crypto('senspark', ['brl', 'usd'], True, True).crypto_price()
    return listValuesSENSChart


@app.route('/api/bomb', methods=['GET'])
def getValueBOMB():
    listValuesBOMB = Crypto('bombcrypto-coin', ['brl', 'usd'], True).crypto_price()
    return listValuesBOMB


@app.route('/api/bomb-chart', methods=['GET'])
def getValueBOMBChart():
    listValuesBOMBChart = Crypto('bombcrypto-coin', ['brl', 'usd'], True, True).crypto_price()
    return listValuesBOMBChart


if __name__ == '__main__':
    app.run()
