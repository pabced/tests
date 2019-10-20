from flask import Flask, jsonify, render_template
import os
import json

app = Flask(__name__, template_folder='template',static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def loadFile(name):
    filename = os.path.join(app.static_folder, name)
    data = ''
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return data

@app.route('/get_data_serie01')
def data_serie01():
    data = loadFile('serie01.json')
    return jsonify(data)

@app.route('/get_data_serie02')
def data_serie02():
    data = loadFile('serie02.json')
    return jsonify(data)

@app.route('/get_data_serie03')
def data_serie03():
    data = loadFile('serie03.json')
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
