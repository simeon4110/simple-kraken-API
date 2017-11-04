import json, requests


def update_kraken_price(currency):
    """ Updates prices for Kraken """
    url = "https://api.kraken.com/0/public/Ticker?pair=XBT" + currency

    request = requests.get(url)
    request_data = json.loads(request.text)

    # parse API request into variables
    last_trade, last_trade_volume = request_data['result']['XXBTZ' + currency]['c']
    volume, volume_24 = request_data['result']['XXBTZ' + currency]['v']
    low, low_24 = request_data['result']['XXBTZ' + currency]['l']
    high, high_24 = request_data['result']['XXBTZ' + currency]['h']
    open_price = request_data['result']['XXBTZ' + currency]['o']
    ask, ask_whole_volume, ask_lot_volume = request_data['result']['XXBTZ' + currency]['a']
    bid, bid_whole_volume, bid_lot_volume = request_data['result']['XXBTZ' + currency]['b']

    # parse variables into dict, convert all numbers to floats
    request_data = {
        'code': currency,
        'last_trade': float(last_trade),
        'last_trade_volume': float(last_trade_volume),
        'ask': float(ask),
        'ask_lot': float(ask_lot_volume),
        'ask_whole': float(ask_whole_volume),
        'bid': float(bid),
        'bid_lot': float(bid_lot_volume),
        'bid_whole': float(bid_whole_volume),
        'open': float(open_price),
        'high': float(high),
        'high_24': float(high_24),
        'low': float(low),
        'low_24': float(low_24),
        'volume': float(volume),
        'volume_24': float(volume_24)
        }
    
    return(request_data)

# change currency to get a different currency pair  
request_data = update_kraken_price("USD")

print(request_data)

