from flask import Flask
import ebay

app = Flask(__name__) 

@app.route('/')
def index():
    return items

if __name__ == '__main__':
    app.run()