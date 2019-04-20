from e import dictr
from flask import Flask
from bs4 import BeautifulSoup


app = Flask(__name__) 

@app.route('/')
def index():
    print (dictr)
if __name__ == '__main__':
    app.run()