from random import randint, random
from time import time

# from requests import Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json
# from src.config import config


def data_api_load(interval='1h'):

    data = []
    date = int(time())
    progress_imitation = 8000
    for _ in range(randint(1200, 1500)):
        random_direction = 1 if random() > 0.5 or progress_imitation < 2000 else -1
        progress_imitation += random_direction * 1000

        value = randint(progress_imitation, progress_imitation + 1000)
        date += randint(901, 1800)
        piece = {'date': str(date), 'value': str(value)}
        data.append(piece)
    return data

    # if interval not in ["1d", "1h", "15m"]:
    #     raise ValueError('given interval is not "1d", "1h", "15m"')
    #
    # url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'
    # parameters = {
    #     'start': '1',
    #     'interval': interval,
    #     'count': '1200',
    #     'convert': 'USD',
    #     'symbol': 'BTC',
    #     'aux': 'price,quote_timestamp'
    # }
    # headers = {
    #     'Accepts': 'application/json',
    #     'X-CMC_PRO_API_KEY': config.DATA_API_KEY,
    # }
    #
    # session = Session()
    # session.headers.update(headers)
    #
    # data = None
    # try:
    #     response = session.get(url, params=parameters)
    #     data = json.loads(response.text)
    #     print(data)
    #     return data
    # except (ConnectionError, Timeout, TooManyRedirects) as e:
    #     print(e)
