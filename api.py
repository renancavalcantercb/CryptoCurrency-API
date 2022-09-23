from pycoingecko import CoinGeckoAPI

from exceptions.CurrencyNotFound import CurrencyNotFound


class Crypto:
    """
        Create a request to get a Bcoin price in Brl and USD, and difference in the last 24 hours.

        :param str id: ID of the crypto you want to know the price.
        :param list currency: Currency to know the
        value of the chosen crypto.


        Example:
            >>> bcoin = Crypto('bomber-coin', ['brl']).crypto_price()
            >>> bcoin = Crypto('bomber-coin', ['brl', 'usd']).crypto_price()
    """

    def __init__(self, id: str, currency: list):
        self.id = id
        self.currency = currency

    def crypto_price(self) -> dict:
        values = {}
        cg = CoinGeckoAPI()
        for i in range(len(self.currency)):
            try:
                req = cg.get_price(
                    ids=self.id, vs_currencies=self.currency[i].lower(), include_24hr_change=True)
                price = '{:.2f}'.format(
                    float(req[self.id][self.currency[i].lower()]))
                values[self.currency[i].upper()] = price
            except KeyError:
                raise CurrencyNotFound()
            dif = '{:.2f}'.format(
                float(req[self.id][str(self.currency[i].lower() + '_24h_change')]))
        values['DIF'] = dif
        return values
