class CurrencyNotFound(Exception):
    def __init__(self):
        super().__init__('Currency Not Found')
