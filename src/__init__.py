from flask import Flask, request, render_template
import os
from . import decode
from . import colorPicker

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello Color Picker !!"
    return name

@app.route('/color', methods=['GET', 'POST'])
def colorPick():
    if request.method == 'POST':
        b64 = request.form['data']
        img = decode.dec(b64)
        data = colorPicker.mainFunction(img)
        return data
    else:
        return 'please base64 post'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')