from flask import Flask, render_template, jsonify
from datetime import datetime
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route('/rapport/')
def mongraphique():
    return render_template('graphique.html')

@app.route('/histogramme/')
def histogramme():
    return render_template('histogramme.html')

@app.route('/contact/')
def contact_form():
    return render_template('contact.html')

@app.route('/graph-commits/')
def graph_commits():
    return render_template('commits.html')

@app.route('/commits/')
def commits_chart():
    results = [
        {"minute": "12", "count": 2},
        {"minute": "15", "count": 1},
        {"minute": "23", "count": 3},
        {"minute": "30", "count": 2},
        {"minute": "42", "count": 1},
    ]
    return jsonify(results=results)
if __name__ == "__main__":
    app.run(debug=True)
