# Crypto API

The Crypto API provides a Rest API that returns the price of the chosen token, in the currency of your choice and the difference in value based on the last 24 hours.

### Utilizando o código de acesso [GET]
Set URL to `/{id}/{currency}` where `id` is the id of the cryptocurrency you want to know the price, if you want to know in more than one currency, put those separated by a comma, and `currency` is the currency you want to know the price of that crypto .

| Parameter | Description |
|---|---|
| `BRL` | Latest value of the chosen crypto in Reais
| `USD` | Latest value of the chosen crypto in dollars |
| `DIF` | Variation of the value in percentage of the last 24 hours. |

### Example

+ /bomber-coin/brl, usd

+ Response 200 ()

    + Response body

          {
            "BRL": "0.07",
            "USD": "0.01",
            "DIF": "2.24"
          }


+ /bitcoin/brl

+ Response 200 ()

    + Response body

            {
              "BRL": "103614.00",
              "DIF": "2.30"
            }

+ /dogecoin/eur, cad

+ Response 200 ()

    + Response body

            {
              "EUR": "0.06",
              "CAD": "0.08",
              "DIF": "0.82"
            }

