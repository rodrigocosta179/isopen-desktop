# build a750860af9
# (auto) 3cce43
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
