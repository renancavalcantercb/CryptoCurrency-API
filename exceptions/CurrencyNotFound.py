class CurrencyNotFound(Exception):
    def __init__(self):
        super().__init__('ID or Currency Not Found')
