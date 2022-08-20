import pandas as pd
from pycoingecko import CoinGeckoAPI
import plotly.express as px
from datetime import datetime
import base64


class CryptoChart():
    def __init__(self):
        pass
    
    def chart(self, id, currency):
        count = 0
        cg = CoinGeckoAPI()
        reqChart = cg.get_coin_market_chart_by_id(id=id, vs_currency=currency, days='1')
        json = reqChart['prices']
        json = json[len(json)-10:len(json)]
        for value in json:
            timeInt = int(value[0])
            time = datetime.utcfromtimestamp(timeInt/1000).strftime('%H:%M')
        value[0] = time
        json[count] = value
        data1 = pd.DataFrame(json, columns=['Hour', 'Price'])
        fig = px.line(data1, x='Hour', y='Price',
                      title=str(id.capitalize() + 'Graph: To the Hell'), markers=True)
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
        fig.write_image('crypto.png')
        with open("crypto.png", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            file = open('b64_crypto.txt', 'w')
            file.write(b64_string.decode('utf-8'))
            file_input = open('b64_crypto.txt')
            dataBcoin = file_input.read()
        count += 1
        return dataBcoin