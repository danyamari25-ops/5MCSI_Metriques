from flask import Flask, render_template, jsonify
from flask import json
from urllib.request import urlopen

app = Flask(__name__)

# Route principale
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route contact
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

# Route pour le graphique en ligne
@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

# Route pour l'histogramme
@app.route("/histogramme/")
def mon_histogramme():
    return render_template("histogramme.html")

# Route pour récupérer les données météo
@app.route('/tawarano/')
def meteo():
    # Appel de l'API OpenWeatherMap
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()

    # Chargement du JSON
    json_content = json.loads(raw_content.decode('utf-8'))

    results = []

    # Parcours des éléments de la liste
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')  # timestamp
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Kelvin → °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})

    # Renvoi des résultats en JSON
    return jsonify(results=results)

# Lancer l'application
if __name__ == "__main__":
    app.run(debug=True)
