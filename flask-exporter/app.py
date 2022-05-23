from flask import Flask
import json
import requests
import os

def create_app():
    app = Flask(__name__)

    @app.route('/metrics')
    def cgi_stock():
        url = "https://yfapi.net/v6/finance/quote"

        querystring = {"symbols":"GIB"}
        headers = {
            'x-api-key': os.environ['YF_APIKEY']
            }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=querystring
        )
        if response.status_code != 200:
            return '# Issue with request' + response.text
        r = json.loads(response.text)
        market_price = r['quoteResponse']['result'][0]['regularMarketPrice']
        return 'stock_price{company="CGI"} ' + str(market_price)
    
    return app


if __name__=='__main__':
    # This will run the app for testing purposes
    app = create_app()
    app.run(port=31000, debug=True)








