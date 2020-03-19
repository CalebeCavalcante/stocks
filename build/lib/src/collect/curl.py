import requests

def extracao(ticket):
    
    try:
        
        response = get(ticket)
        obj = response.json()
        meta = obj['chart']['result'][0]['meta']
        
        return [ meta['symbol'], meta['regularMarketPrice'], meta['previousClose'] ]

    except Exception as e:
        raise e
    

def get(ticket):
    
    try:
        headers = {
        'authority': 'query1.finance.yahoo.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'sec-fetch-dest': 'empty',
        'accept': '*/*',
        'origin': 'https://finance.yahoo.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://finance.yahoo.com/quote/'+ticket.lower()+'.SA?p='+ticket.lower()+'.SA&.tsrc=fin-srch',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = (
            ('region', 'US'),
            ('lang', 'en-US'),
            ('includePrePost', 'false'),
            ('interval', '2m'),
            ('range', '1d'),
            ('corsDomain', 'finance.yahoo.com'),
            ('.tsrc', 'finance'),
        )

        response = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/'+ticket.upper()+'.SA', headers=headers, params=params)

        if response.status_code != 200: raise Exception("Falha ao buscar os dados de " + ticket)

        return response
        
    except Exception as e:
        raise e