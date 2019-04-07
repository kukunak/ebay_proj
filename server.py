from flask import Flask
import ebay 

app = Flask(__name__) # создаем приложение в () имя текущего файла

@app.route('/')
def index():
    return f'{cat:\n} {title:\n}{price:\n} {url:\n}'

if __name__ == '__main__':
    app.run()