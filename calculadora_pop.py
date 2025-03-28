class calculadora:
    def __init__(self, a, b):
        self._resulatdo = 0 
        self.a = a
        self.b = b
        self.operacopnes = ""

    def suma(self):
        self.operacion = "suma"
        self._resultado = self.a + self.b
        return self._mostrar()

    def resta(self):
        self.operacion = "resta"
        self._resultado = self.a + self.b
        return self._mostrar()

    def multiplicacion(self):
        self.operacion = "multiplicacion"
        self._resultado = self.a + self.b
        return self._mostrar()

    def division(self):
        self.operacion = "division"
        self._resultado = self.a + self.b
        return self._mostrar()

    def _mostrar(self):
        return f"{self.operacion}: {self.a} y {self.b} = {self._resultado}"


calculadora_1 = calculadora(15, 5)

print(calculadora_1.suma())
print(calculadora_1.resta())
print(calculadora_1.multiplicacion())
print(calculadora_1.division())








