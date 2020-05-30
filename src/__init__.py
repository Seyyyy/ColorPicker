from flask import Flask, request, render_template, make_response, jsonify
import os
from . import decode
from . import colorPicker
import ast

app = Flask(__name__)

@app.route('/')
def hello():
    text = {
        'body': 'Hello Color Picker !!'
    }
    resp = make_response(jsonify(text))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/color', methods=['GET', 'POST', 'OPTIONS'])
def colorPick():
    print(request.headers)
    if request.method == 'POST':
        # byteデータでbody要素を受け取ってdict型に変更しbodyの中のindexがbase64のデータを受け取る
        byteData = request.get_data()
        byteData = byteData.decode()
        dic = ast.literal_eval(byteData)
        dic = dic['base64']

        b64 = dic
        img = decode.dec(b64)
        data = colorPicker.mainFunction(img)
        resp = make_response(jsonify(data))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        resp.headers['Access-Control-Max-Age'] = 86400
        resp.headers['Content-Type'] = 'application/json'
        return resp
    elif request.method == 'OPTIONS':
        # make priflight request
        resp = make_response()
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        resp.headers['Origin'] = '*'
        return resp
    else:
        return 'please base64 post'

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')