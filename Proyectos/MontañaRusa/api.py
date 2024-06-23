from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def route():
    return "API"

@app.route("/datos1")
def get_datos1():
    diccionario = {'x_data':'[0, 1, 2, 3, 4, 5]','y_data':'[0.5, 0.8, 1.0, 0.9, 1.2, 0.7]'}
    return jsonify(diccionario)

@app.route("/datos2")
def get_datos2():
    diccionario = {'x_data':'[0, 1, 2, 3, 4]','y_data':'[1.1, 3.5, 2.8, 4.2, 5.0]'}
    return jsonify(diccionario)

@app.route("/datos4")
def get_datos4():
    diccionario = {'a':'[[1,2,1],[2,-1, 1],[3,1,-1]]','b':'[4,1,-2]'}
    return jsonify(diccionario)

if __name__ == "__main__":
    app.run(debug=True)

# URLs de la API
url_datos1 = 'http://127.0.0.1:5000/datos1'
url_datos2 = 'http://127.0.0.1:5000/datos2'
url_datos4 = 'http://127.0.0.1:5000/datos4'

# Obtener datos de /datos1
response1 = requests.get(url_datos1)
def datos1():
    if response1.status_code == 200:
        data1 = response1.json()
        x_data1 = data1.get('x_data', [])
        y_data1 = data1.get('y_data', [])
        return x_data1,y_data1

# Obtener datos de /datos2
response2 = requests.get(url_datos2)
def datos2():
    if response2.status_code == 200:
        data2 = response2.json()
        x_data2 = data2.get('x_data', [])
        y_data2 = data2.get('y_data', [])
        return x_data2,y_data2

# Obtener datos de /datos4
response4 = requests.get(url_datos4)
def datos4():
    if response4.status_code == 200:
        data4 = response4.json()
        a_data = data4.get('a', [])
        b_data = data4.get('b', [])
        return a_data,b_data
