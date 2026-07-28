from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, from Paas Lab Student: VARSHITHA SIRIPURAM, Roll NO: 24MID0288'
