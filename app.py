from flask import Flask, json, render_template
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    #n_astros = r['number']
    #astros = r['people']

    #return f'Number o Astronauts in Space Now: {n_astros}\n\n{astros}'
    return render_template('index.html', response=r)

if __name__ == "__main__":
    app.run(debug=True)
