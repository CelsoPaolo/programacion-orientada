# programacion-orientada

# PRACTICA N* 1

El objetivo de esta práctica fue aplicar los principios fundamentales de la programación orientada a objetos (POO): abstracción, encapsulamiento, herencia y polimorfismo.

Como ejercicio principal, se desarrolló una calculadora estándar capaz de realizar operaciones básicas como suma, resta, multiplicación y división. A partir de esa clase base, se creó una calculadora factorial que hereda su funcionalidad y añade el método para calcular el factorial de un número, sobrescribiendo también el método para mostrar el resultado.

Además, se implementaron versiones de estas operaciones de forma procedimental, con el fin de comparar ambos enfoques y entender mejor las ventajas que ofrece el uso de clases y objetos en el diseño de software.

# Preparacion del entorno

1. Clonar el repositorio
```python
git clone https://github.com/yefeza/pg2-practica1.git
cd pg2-practica1
```

2. Crear un entorno virtual

```python
python -m venv env
```

3. Activar el entorno virtual
* En windows:
```python
.\env\Scripts\activate
```
* En linux o mac:
```python
source env/bin/activate
```

4. Ejecutar el scrip
```python
python main.py
```

5. Desactivar el entorno virtual
```python
deactivate
```

 # DESCRIPCIÓN Y FORMA DE USO DE LA CLASE CALCULADORA ESTANDAR

 La clase Calculadora realiza operaciones matemáticas básicas: suma, resta, multiplicación y división. Cada operación tiene un método específico que devuelve el resultado junto con una descripción.

suma(a, b): Realiza la suma de a y b.

resta(a, b): Realiza la resta de a y b.

multiplicacion(a, b): Realiza la multiplicación de a y b.

division(a, b): Realiza la división de a y b.

Su uso :
```python
from calculadora_poo import Calculadora  
calculadora = Calculadora()

print(calculadora.suma(10, 5))           
print(calculadora.resta(10, 5))          
print(calculadora.multiplicacion(10, 5)) 
print(calculadora.division(10, 5)) 
```

# PRINCIPIOS DE POO QUE APLICA Y COMO, calculadora estandar

Abstracción
Permite usar métodos como suma(), resta(), multiplicacion() y division() sin necesidad de conocer los detalles internos de cómo se realizan las operaciones. El usuario solo interactúa con lo esencial: los métodos públicos.

Encapsulamiento
Agrupa los atributos y métodos dentro de la clase, protegiendo los datos internos. Por ejemplo, el resultado de cada operación se guarda en un atributo privado (_resultado), y el usuario no accede directamente a él, sino a través del método _mostrar().

Herencia
Aunque no se aplica directamente en la clase Calculadora, esta clase está pensada como clase base. La clase CalculadoraFactorial hereda de ella y reutiliza su funcionalidad, especialmente el método multiplicar().

Polimorfismo
Se demuestra al sobrescribir el método _mostrar() en la clase CalculadoraFactorial. Mientras Calculadora lo usa para mostrar operaciones básicas, CalculadoraFactorial lo modifica para mostrar el resultado del factorial, aunque ambos usan el mismo nombre de método.

# Descripcion y forma de uso de la clase calculadorafactorial

La clase CalculadoraFactorial hereda de la clase Calculadora y añade la funcionalidad de calcular el factorial de un número entero.

Características:
Usa el método multiplicar() heredado para hacer el cálculo.

Implementa el método calcular(), que devuelve el factorial del número recibido.

Sobrescribe el método para mostrar el resultado, adaptándolo a la operación factorial.

Ejemplo de uso:

```python
from calculadora_factoriall import CalculadoraFactorial

factorial = CalculadoraFactorial(5)
print(factorial.calcular())  # factorial: 5 = 120
```

El cálculo se hace con un bucle while multiplicando desde 1 hasta el número dado, y el resultado se muestra con un formato personalizado.

```python
while cont <= self.numero:
            factorial = self.multiplicar(factorial, cont)

            cont += 1

        self._resultado = factorial
        return self._mostrar_opecaiones()
    
    def _mostrar_opecaiones(self):
        return f"{self.operacion}: {self.numero} = {self._resultado}"
```
# PRINCIPIOS DE POO QUE APLICA Y COMO, calculadorafactorial

Abstracción
La clase CalculadoraFactorial abstrae el proceso del cálculo del factorial. El usuario solo interactúa con el método calcular(), sin tener que preocuparse de los detalles internos de cómo se realiza la multiplicación de los números. Esto permite al usuario centrarse únicamente en lo que necesita: el resultado del factorial.

Encapsulamiento
Dentro de la clase CalculadoraFactorial, los detalles del cálculo se mantienen encapsulados. El resultado de la operación se guarda en el atributo privado _resultado, y el usuario no tiene acceso directo a este atributo. En cambio, accede a través del método _mostrar_opecaiones(), lo que asegura que los detalles de implementación queden protegidos.

Herencia
La clase CalculadoraFactorial hereda de la clase base Calculadora. Esto permite reutilizar la funcionalidad de los métodos ya definidos en la clase base, como multiplicar(), que es utilizado para calcular el factorial. Así, se evita la duplicación de código y se mantiene la estructura de clases modular y reutilizable.

Polimorfismo
El principio de polimorfismo se aplica cuando la clase CalculadoraFactorial sobrescribe el método _mostrar_opecaiones() de la clase Calculadora. Mientras que en Calculadora este método se usa para mostrar los resultados de operaciones básicas como suma o resta, en CalculadoraFactorial el mismo método es utilizado para mostrar el resultado del cálculo del factorial. Aunque ambos métodos tienen el mismo nombre, su comportamiento cambia dependiendo de la clase que los invoque.


# DIFERENECIA ENTRE LA IMPLEMENTACION PROCEDIMENTAL Y ORIENTADA A OBJETOS 
# Programacion procedimental
Ampliando un poco más, la programación procedimental en Python se centra en una secuencia de pasos o procedimientos (funciones) para realizar una tarea. El flujo del programa se controla mediante llamadas a estas funciones, y los datos suelen ser entidades separadas que se pasan entre ellas. Aunque es intuitiva para tareas sencillas y scripts, sufre de limitaciones en la gestión de la complejidad en proyectos grandes. La modificación de datos puede tener efectos secundarios difíciles de rastrear a medida que el programa crece, y la reutilización del código se limita principalmente a la invocación de funciones aisladas.
```python
base = 5
altura = 10

def area(b, a):
  return b * a

print(f"Área: {area(base, altura)}")
```

# Programacion orientada a objetos
En contraste, la programación orientada a objetos (OOP) en Python aborda la complejidad organizando el código en torno a objetos. Estos objetos son instancias de clases, que actúan como plantillas definiendo tanto los datos (atributos) que caracterizan al objeto como las acciones (métodos) que puede realizar. La OOP se basa en cuatro pilares fundamentales:

Encapsulamiento: Agrupa los datos y los métodos que operan sobre esos datos dentro de un objeto, restringiendo el acceso directo a los datos y protegiéndolos de modificaciones externas no controladas.

Abstracción: Se enfoca en las características esenciales de un objeto, ocultando los detalles de implementación internos. Esto permite interactuar con los objetos a un nivel superior, sin necesidad de conocer su funcionamiento interno completo.

Herencia: Permite crear nuevas clases (subclases) que heredan las propiedades y comportamientos de clases existentes (superclases). Esto fomenta la reutilización del código y la creación de jerarquías de clases relacionadas.

Polimorfismo: Posibilita que objetos de diferentes clases respondan al mismo mensaje (llamada a un método) de manera específica para su tipo. Esto añade flexibilidad y extensibilidad al diseño del software.
```python
class Rectangulo:
  def __init__(self, b, a):
    self.base = b
    self.altura = a

  def area(self):
    return self.base * self.altura

rect = Rectangulo(5, 10)
print(f"Área: {rect.area()}")
```
