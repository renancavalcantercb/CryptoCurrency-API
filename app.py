from flask import Flask
from pycoingecko import CoinGeckoAPI
import plotly.express as px
import pandas as pd
from datetime import datetime
import base64

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Bombcrpyto Tokens API'


@app.route('/api/bcoin/', methods=['GET'])
def getValueBcoin():
    listValuesBcoin = getAPIexternaBCOIN()
    values = {
        'BRL': listValuesBcoin[0],
        'DIF': listValuesBcoin[1],
        'B64': listValuesBcoin[2],
    }
    return values


@app.route('/api/sens/', methods=['GET'])
def getValueSENS():
    listValuesSENS = getAPIexternaSENS()
    values = {
        'BRL': listValuesSENS[0],
        'DIF': listValuesSENS[1],
        'B64': listValuesSENS[2],

    }
    return values


def getAPIexternaBCOIN():
    count = 0
    cg = CoinGeckoAPI()
    reqBcoin = cg.get_price(ids='bomber-coin', vs_currencies='brl',
                            include_24hr_change=True)
    reqChart = cg.get_coin_market_chart_by_id(id='bomber-coin', vs_currency='brl',
                                              days='1')
    priceBcoin = float(reqBcoin['bomber-coin']['brl'])
    difBcoin = reqBcoin['bomber-coin']['brl_24h_change']
    priceFormatBcoin = '{:.2f}'.format(priceBcoin)
    difFormatBcoin = '{:.2f}'.format(difBcoin)
    json = reqChart['prices']
    json = json[len(json)-10:len(json)]
    for value in json:
        timeInt = int(value[0])
        time = datetime.utcfromtimestamp(
            timeInt/1000).strftime('%H:%M:%S')
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
        fig.show()
        fig.write_image('bcoin.png')
        with open("bcoin.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            file = open('b64_bcoin.txt', 'w')
            file.write(b64_string.decode('utf-8'))
            file_input = open('b64_bcoin.txt')
            dataBcoin = file_input.read()
        count = count + 1
    return(priceFormatBcoin, difFormatBcoin, dataBcoin)


def getAPIexternaSENS():
    count = 0
    cg = CoinGeckoAPI()
    reqSens = cg.get_price(
        ids='senspark', vs_currencies='brl', include_24hr_change=True)
    reqChart = cg.get_coin_market_chart_by_id(id='senspark', vs_currency='brl',
                                              days='1')
    priceSens = float(reqSens['senspark']['brl'])
    difSens = reqSens['senspark']['brl_24h_change']
    priceFormatSens = '{:.2f}'.format(priceSens)
    difFormatSens = '{:.2f}'.format(difSens)
    json = reqChart['prices']
    json = json[len(json)-10:len(json)]
    for value in json:
        timeInt = int(value[0])
        time = datetime.utcfromtimestamp(
            timeInt/1000).strftime('%H:%M:%S')
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
        fig.show()
        fig.write_image('SENS.png')
        with open("SENS.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            file = open('b64_sens.txt', 'w')
            file.write(b64_string.decode('utf-8'))
            file_input = open('b64_sens.txt')
            dataSens = file_input.read()
        count = count + 1
    return(priceFormatSens, difFormatSens, dataSens)


if __name__ == '__main__':
    app.run()
