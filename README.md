# Bombcrypto Coins API

O Bombcrypto Coins disponibiliza uma API REST que retorna o preço do token escolhido (BCOIN ou SENS), a diferença de valor baseado nas últimas 24 horas e uma imagem do gráfico de varição da última hora.

### Utilizando o código de acesso [GET]
Monte a URL como `/api/{moeda}` substituindo `moeda` pelo Token que você quer obter as informações, no momento existe somente duas moedas que é possivel obter sendo ela `bcoin` ou `sens`.
| Parâmetro | Descrição |
|---|---|
| `B64  ` | Imagem do gráfico de variação da última hora em BASE64. |
| `BRL` | Último valor do BCOIN em Reais. |
| `DIF` | Variação do valor em porcentagem das últimas 24 horas. |


+ /api/bcoin

+ Response 200 ()

    + Body

            {
                "B64": "iVBORw0KGgoAAAANSUhEUgAA…kzj4i8AAAAASUVORK5CYII=",
                "BRL": "0.79",
                "DIF": "16.87",
            }

+ /api/sens

+ Response 200 ()

    + Body

            {
                "B64": "iVBORw0KGgoAAAANSUhEUgAA…CqONe8AAAAASUVORK5CYII=",
                "BRL": "1.66",
                "DIF": "4.35",
            }



![Gif da Maga do Bombcrypto andando](https://media.giphy.com/media/EHxAswWZMz3d9UCKUB/giphy.gif)![Gif do Vampiro do Bombcrypto andando](https://media.giphy.com/media/oRh8wlREMMlD075qc3/giphy.gif)![Gif do Pistoleiro do Bombcrypto andando](https://media.giphy.com/media/JuJFJDVGnpfC9nYB9G/giphy.gif)![Gif do Guerreiro do Bombcrypto andando](https://media.giphy.com/media/BB5PKWbZJ4syzioAR9/giphy.gif)![Gif do Pepe do Bombcrypto andando](https://media.giphy.com/media/5aNxJf2gOIV2QfKPss/giphy.gif)![Gif do Doge do Bombcrypto andando](https://media.giphy.com/media/KyaiTSSlu4Qr6pXcyU/giphy.gif)


