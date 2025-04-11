from calculadora_poo  import calculadora


class calculadorafactorial(calculadora):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero

    def calcular(self):
        self.operacion = 'factorial'
        factorial = 1
        cont = 1


        while cont <= self.numero:
            factorial = self.multiplicar(factorial, cont)

            cont += 1

        self._resultado = factorial
        return self._mostrar_opecaiones()
    
    def _mostrar_opecaiones(self):
        return f"{self.operacion}: {self.numero} = {self._resultado}"
    



