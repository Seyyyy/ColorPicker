from flask import Flask, request, render_template, Response, make_response, jsonify
import os
from . import decode
from . import colorPicker

app = Flask(__name__)

@app.route('/')
def hello():
    text = {
        'body': 'Hello Color Picker !!'
    }
    resp = make_response(jsonify(text))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/color', methods=['GET', 'POST'])
def colorPick():
    if request.method == 'POST':
        b64 = request.form['data']
        img = decode.dec(b64)
        data = colorPicker.mainFunction(img)
        resp = Response(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    else:
        return 'please base64 post'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')