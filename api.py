from pycoingecko import CoinGeckoAPI
from exceptions.CurrencyNotFound import CurrencyNotFound
from api_chart import CryptoChart


class Crypto():
    """
    Create a request to get a Bcoin price in Brl and USD, and difference in the last 24 hours.

    Attributes:
    --------
        :param str id: Id of the crypto you want to know the price.
        :param list currency: Currency to know the value of the chosen crypto.
        :param str lastdaychange: Parameter to know what was the percentage variation in the last 24 hours of the currency.

    Example:
    --------
        >>> bcoin = Crypto('bomber-coin', ['brl', 'usd']).crypto_price()

    """

    def __init__(self, id, currency, lastdaychange = False, chart = False):
        self.id = id
        self.currency = currency
        self.lastdaychange = lastdaychange
        self.chart = chart
    
    def crypto_price(self):
        values = {}
        cg = CoinGeckoAPI()
        for i in range(len(self.currency)):
            try:
                req = cg.get_price(
                    ids=self.id, vs_currencies=self.currency[i].lower(), include_24hr_change=self.lastdaychange)
                price = '{:.2f}'.format(float(req[self.id][self.currency[i].lower()]))
                values[self.currency[i].upper()] = price
            except KeyError: 
                raise CurrencyNotFound()
        if self.lastdaychange == True:
            dif = '{:.2f}'.format(float(req[self.id][str(self.currency[-1].lower() + '_24h_change')]))
            values['DIF'] = dif
        if self.chart == True:
            values['B64'] = CryptoChart().chart(self.id, self.currency[-1].lower())
        return values 

