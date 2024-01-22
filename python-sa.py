class Persona:
    nombre = None
    edad = None
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}"
    
class Cliente(Persona):
    telefono_de_contacto : None

    def __init__(self, nombre, edad, telefono):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono

    def mostrar(self):
        return super().mostrar(), f"Telefono: {self.telefono_de_contacto}"


class Empleado:
    sueldo_bruto = None
    def __init__(self, n, e, s):
        super().__init__(n, e)
        self.sueldo_bruto = s

    def calcular_salario_neto(self):
        self.sueldo_bruto * 0.9

    def mostrar(self):
        return super().mostrar() , f"Salario neto: {self.calcular_salario_neto}"
    
class Empresa:
    nombre = None
    empleado = None

    def __init__(self,):
        self.nombre = "MI EMPRESA" 
        self.empleado = []
        self.cliente = []

    def set_nombre(self,nombre):
        self.nombre = nombre

    def agregar_empleado(self, Empleado):
        self.empleado.append(Empleado)
        
    def agregar_cliente(self, Cliente):
        self.cliente.append(Cliente)


class Directivo:
    pass
        