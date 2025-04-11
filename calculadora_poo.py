class calculadora:
    def __init__(self):
        self._resulatdo = 0 
        self.operacopnes = ""

    def suma(self,a , b):
        self.operacion = "suma"
        self._resultado = a + b
        return self._mostrar(a, b)

    def resta(self, a, b):
        self.operacion = "resta"
        self._resultado = a - b
        return self._mostrar(a, b)
    
    def multiplicar(self, a, b):
        return a * b

    def multiplicacion(self, a, b):
        self.operacion = "multiplicacion"
        self._resultado = self.multiplicar(a, b)
        return self._mostrar(a, b)

    def division(self, a, b):
        self.operacion = "division"
        self._resultado = a / b
        return self._mostrar(a, b)

    def _mostrar(self,a ,b):
        return f"{self.operacion}: {a} y {b} = {self._resultado}"











