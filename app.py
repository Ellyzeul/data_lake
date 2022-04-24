import os
from dotenv import load_dotenv
from flask import Flask, render_template
from routes.index import index_route


load_dotenv()

app = Flask(__name__)

app.config.from_object('config')
app.register_blueprint(index_route)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
