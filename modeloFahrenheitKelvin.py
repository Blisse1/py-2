class FahrenheitKelvin:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def calcularFahrenheitKelvin(self):
        return (self.fahrenheit + 459.67) / 1.8
