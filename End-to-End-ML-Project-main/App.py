from flask import Flask
from House_price.logger import logging
from House_price.Exception import HousePriceException
import sys


app = Flask(__name__)

@app.route('/', methods=(['GET', 'POST']))
def index():
    try:
        1/2
    except Exception as e:
        raise HousePriceException(e, sys)
    logging.info("we are in index page")
    return "we can print a msg here python flask"


if __name__ == '__main__':
    app.run(debug=True)