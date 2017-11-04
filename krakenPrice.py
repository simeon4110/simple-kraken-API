def update_kraken_price():
    """ Function called via zappa scheduler, updates prices for Kraken """
    currency = "USD" # update later to accept other currencies
    url = "https://api.kraken.com/0/public/Ticker?pair=XBT" + currency

    request = requests.get(url)
    request_data = json.loads(request.text)

    # parse API request into variables (the key "XXBTZUSD" needs to be updated
	# if you want to use another currency.
    last_trade, last_trade_volume = request_data['result']['XXBTZUSD']['c']
    volume, volume_24 = request_data['result']['XXBTZUSD']['v']
    low, low_24 = request_data['result']['XXBTZUSD']['l']
    high, high_24 = request_data['result']['XXBTZUSD']['h']
    open = request_data['result']['XXBTZUSD']['o']
    ask, ask_whole_volume, ask_lot_volume = request_data['result']['XXBTZUSD']['a']
    bid, bid_whole_volume, bid_lot_volume = request_data['result']['XXBTZUSD']['b']

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
        'open': float(open),
        'high': float(high),
        'high_24': float(high_24),
        'low': float(low),
        'low_24': float(low_24),
        'volume': float(volume),
        'volume_24': float(volume_24)
        }
	
	return(request_data)