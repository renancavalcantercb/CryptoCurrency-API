from pycoingecko import CoinGeckoAPI

from exceptions.CurrencyNotFound import CurrencyNotFound


class Crypto:

    def __init__(self):
        self.cg = CoinGeckoAPI()

    def crypto_price(self, id: str, currency: list) -> dict:
        """
            Create a request to get a Bcoin price in Brl and USD, and difference in the last 24 hours.

            :param str id: ID of the crypto you want to know the price.
            :param list currency: Currency to know the
            value of the chosen crypto.

            :return: dict with the price of the crypto in the chosen currency.
            :rtype: dict

            :raises CurrencyNotFound: If the currency is not found.

            :example
                >>> crypto_price('bomber-coin', ['brl', 'usd'])
                {'BRL': '0.01', 'USD': '0.00', 'DIF': '-0.01'}
        """

        values = {}
        for c in currency:
            try:
                values[c.upper()] = self.cg.get_price(ids=id, vs_currencies=c)[id][c]
            except KeyError:
                raise CurrencyNotFound()
        values['DIF'] = self.cg.get_coin_by_id(id=id)['market_data']['price_change_percentage_24h']
        return values

