from flask import Flask, render_template, request
from modeloCelsiusKelvin import CelsiusKelvin
from modeloKelvinFahrenheit import KelvinFahrenheit
from modeloFahrenheitCelsius import FahrenheitCelsius
from modeloFahrenheitKelvin import FahrenheitKelvin

app = Flask(__name__)

@app.route("/", methods=["GET"])
def renderTemplate():
    return render_template("index.html")

@app.route("/celsius", methods=["POST"])
def celsius():
    celsiusDato = float(request.form["celsius"])

    celsius = CelsiusKelvin(celsiusDato)

    calcular = celsius.celsiusKelvin()

    return render_template("index.html", celsiusKelvin=calcular)


@app.route("/kelvin", methods=["POST"])
def kelvin():
    kelvinDato = float(request.form["kelvin"])

    kelvin = KelvinFahrenheit(kelvinDato)

    calcular = kelvin.calcularKelvinFahrenheit()

    return render_template("index.html", kelvin=calcular)

@app.route("/fahrenheitCelsius", methods=["POST"])
def fahrenheitCelsius():
    fahrenheitDato = float(request.form["fahrenheitCelsius"])

    fahrenheit = FahrenheitCelsius(fahrenheitDato)

    calcular = fahrenheit.calcularFahrenheitCelsius()

    return render_template("index.html", fahrenheitCelsius=calcular)

@app.route("/fahrenheitKelvin", methods=["POST"])
def fahrenheitKelvin():
    fahrenheitDato = float(request.form["fahrenheitKelvin"])

    fahrenheit = FahrenheitKelvin(fahrenheitDato)

    calcular = fahrenheit.calcularFahrenheitKelvin()

    return render_template("index.html", fahrenheitKelvin=calcular)

if __name__ == "__main__":
    app.run(debug=True)
