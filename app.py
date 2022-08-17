from flask import Flask
from pycoingecko import CoinGeckoAPI
import plotly.express as px
import pandas as pd
from datetime import datetime
import base64

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Welcome to the Bombcrypto Tokens API'

@app.route('/api/bcoin/', methods=['GET'])
def getValueBcoin():
    listValuesBcoin = getAPIexternaBCOIN()
    values = {
        'BRL': listValuesBcoin[0],
        'USD': listValuesBcoin[1],
        'DIF': listValuesBcoin[2],
        'B64': listValuesBcoin[3],
    }
    return values


@app.route('/api/sens/', methods=['GET'])
def getValueSENS():
    listValuesSENS = getAPIexternaSENS()
    values = {
        'BRL': listValuesSENS[0],
        'USD': listValuesSENS[1],
        'DIF': listValuesSENS[2],
        'B64': listValuesSENS[3],
    }
    return values

@app.route('/api/bombcrypto-coin/', methods=['GET'])
def getValueBOMB():
    listValuesBOMB = getAPIexternaBOMB()
    values = {
        'BRL': listValuesBOMB[0],
        'USD': listValuesBOMB[1],
        'DIF': listValuesBOMB[2],
        'B64': listValuesBOMB[3],
    }
    return values


def getAPIexternaBCOIN():
    cg = CoinGeckoAPI()
    reqBcoin = cg.get_price(ids='bomber-coin', vs_currencies='brl, usd',
                            include_24hr_change=True)
    reqChart = cg.get_coin_market_chart_by_id(id='bomber-coin', vs_currency='brl',
                                              days='1')
    priceBcoinBrl = float(reqBcoin['bomber-coin']['brl'])
    priceBcoinUsd = float(reqBcoin['bomber-coin']['usd'])
    difBcoin = reqBcoin['bomber-coin']['brl_24h_change']
    priceFormatBcoinBrl = '{:.2f}'.format(priceBcoinBrl)
    priceFormatBcoinUsd = '{:.2f}'.format(priceBcoinUsd)
    difFormatBcoinBrl = '{:.2f}'.format(difBcoin)
    json = reqChart['prices']
    json = json[len(json)-10:len(json)]
    for value in json:
        timeInt = int(value[0])
        time = datetime.utcfromtimestamp(
            timeInt/1000).strftime('%H:%M')
        value[0] = time
        json[count] = value
        data1 = pd.DataFrame(json, columns=['Hour', 'Price'])
        fig = px.line(data1, x='Hour', y='Price',
                      title='BCOIN Graph: To the Hell', markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(48, 52, 52, 1)',
            'paper_bgcolor': 'rgba(48, 52, 52, 1)',
        })
        fig.update_xaxes({
            'color': 'white'
        })
        fig.update_yaxes({
            'color': 'white'
        })
        fig.update_layout({
            'title_font_color': 'white'})
        fig.update_traces({'line_color': 'red'})
        fig.write_image('bcoin.png')
        with open("bcoin.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            file = open('b64_bcoin.txt', 'w')
            file.write(b64_string.decode('utf-8'))
            file_input = open('b64_bcoin.txt')
            dataBcoin = file_input.read()
    return(priceFormatBcoinBrl, priceFormatBcoinUsd, difFormatBcoinBrl, dataBcoin)


def getAPIexternaSENS():
    cg = CoinGeckoAPI()
    reqSens = cg.get_price(
        ids='senspark', vs_currencies='brl, usd', include_24hr_change=True)
    reqChart = cg.get_coin_market_chart_by_id(id='senspark', vs_currency='brl',
                                              days='1')
    priceSensBrl = float(reqSens['senspark']['brl'])
    priceSensUsd = float(reqSens['senspark']['usd'])
    difSens = reqSens['senspark']['brl_24h_change']
    priceFormatSensBrl = '{:.2f}'.format(priceSensBrl)
    priceFormatSensUsd = '{:.2f}'.format(priceSensUsd)
    difFormatSensBrl = '{:.2f}'.format(difSens)
    json = reqChart['prices']
    json = json[len(json)-10:len(json)]
    for value in json:
        timeInt = int(value[0])
        time = datetime.utcfromtimestamp(
            timeInt/1000).strftime('%H:%M')
        value[0] = time
        json[count] = value
        data1 = pd.DataFrame(json, columns=['Hour', 'Price'])
        fig = px.line(data1, x='Hour', y='Price',
                      title='SENS Graph: To the Hell', markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(48, 52, 52, 1)',
            'paper_bgcolor': 'rgba(48, 52, 52, 1)',
        })
        fig.update_xaxes({
            'color': 'white'
        })
        fig.update_yaxes({
            'color': 'white'
        })
        fig.update_layout({
            'title_font_color': 'white'})
        fig.update_traces({'line_color': 'red'})
        fig.write_image('SENS.png')
        with open("SENS.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            file = open('b64_sens.txt', 'w')
            file.write(b64_string.decode('utf-8'))
            file_input = open('b64_sens.txt')
            dataSens = file_input.read()
    return(priceFormatSensBrl, priceFormatSensUsd, difFormatSensBrl, dataSens)

def getAPIexternaBOMB():
    cg = CoinGeckoAPI()
    reqBomb = cg.get_price(
        ids='bombcrypto-coin', vs_currencies='brl, usd', include_24hr_change=True)
    reqChart = cg.get_coin_market_chart_by_id(id='bombcrypto-coin', vs_currency='brl',
                                              days='1')
    priceBombBrl = float(reqBomb['bombcrypto-coin']['brl'])
    priceBombUsd = float(reqBomb['bombcrypto-coin']['usd'])
    difBomb = reqBomb['bombcrypto-coin']['brl_24h_change']
    priceFormatBombBrl = '{:.2f}'.format(priceBombBrl)
    priceFormatBombUsd = '{:.2f}'.format(priceBombUsd)
    difFormatBombBrl = '{:.2f}'.format(difBomb)
    json = reqChart['prices']
    json = json[len(json)-10:len(json)]
    for value in json:
        timeInt = int(value[0])
        time = datetime.utcfromtimestamp(
            timeInt/1000).strftime('%H:%M')
        value[0] = time
        json[count] = value
        data1 = pd.DataFrame(json, columns=['Hour', 'Price'])
        fig = px.line(data1, x='Hour', y='Price',
                      title='BOMB Graph: To the Hell', markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(48, 52, 52, 1)',
            'paper_bgcolor': 'rgba(48, 52, 52, 1)',
        })
        fig.update_xaxes({
            'color': 'white'
        })
        fig.update_yaxes({
            'color': 'white'
        })
        fig.update_layout({
            'title_font_color': 'white'})
        fig.update_traces({'line_color': 'red'})
        fig.write_image('BOMB.png')
        with open("BOMB.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            file = open('b64_sens.txt', 'w')
            file.write(b64_string.decode('utf-8'))
            file_input = open('b64_sens.txt')
            dataBomb = file_input.read()
    return(priceFormatBombBrl, priceFormatBombUsd, difFormatBombBrl, dataBomb)



if __name__ == '__main__':
    app.run()
