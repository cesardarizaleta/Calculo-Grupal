from flask import Flask, jsonify, request

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
    diccionario = {'x_data':'[0, 1, 2, 3, 4, 5]','y_data':'[0.5, 0.8, 1.0, 0.9, 1.2, 0.7]'}
    return jsonify(diccionario)

@app.route("/datos4")
def get_datos4():
    diccionario = {'a':'[[1,2,1],[2,-1, 1],[3,1,-1]]','b':'[4,1,-2]'}
    return jsonify(diccionario)

if __name__ == "__main__":
    app.run(debug=True)