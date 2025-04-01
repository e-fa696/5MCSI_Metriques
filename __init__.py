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
    url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    minute_counts = {}

    for commit in data:
        date_str = commit.get('commit', {}).get('author', {}).get('date')
        if date_str:
            dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
            minute = dt.minute
            minute_counts[minute] = minute_counts.get(minute, 0) + 1

    results = [{'minute': str(minute), 'count': count} for minute, count in sorted(minute_counts.items())]
 
    return jsonify(results=results)
@app.route("/test/")
def test():
    return "Flask fonctionne"

if __name__ == "__main__":
    app.run(debug=True)
