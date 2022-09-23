import re

from flask import Flask
from flask_restx import Api, Resource, Namespace, abort

from api import Crypto

app = Flask(__name__)
api = Api(app, version='2.0', title='Crypto API', description='API to get crypto prices', default='Crypto',
          default_label='Crypto API')


@api.route('/<string:id>/<string:currency>', doc={
    'params': {'id': 'ID of the crypto you want to know the price (ex: bomber-coin or bitcoin)',
               'currency': 'Currency to know the value of the chosen crypto (ex: brl, you can use both separated by comma)'}})
class Request(Resource):
    ns = Namespace('Crypto',
                   description='Create a request to get a Bcoin price in Brl and USD, and difference in the last 24 hours.')

    def get(self, id, currency):

        currency = re.sub(r'\s+', '', currency).split(',')
        try:
            req = Crypto(id, currency).crypto_price()
            return req
        except Exception as e:
            abort(404, e)


if __name__ == '__main__':
    app.run()
