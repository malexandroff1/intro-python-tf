from datetime import date
from datetime import datetime


class Persona:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: date, cuentas=None):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.cuentas = cuentas or []

    @property
    def edad(self):
        diferencia_en_dias = (date.today() - self.fecha_nacimiento).days
        return int(diferencia_en_dias / 365)

    def mostrar(self):
        print(f"nombre : {self.nombre} edad :{self.edad} dni : {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)


class Cuenta(object):
    def __init__(self, monto_inicio=0, numero_de_cuenta=0):
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    def aplicar_gasto(self, monto: float, descripcion: str):
        self.cantidad = self.cantidad - monto
        self.crear_movimiento(descripcion, monto)

    def aplicar_deposito(self, monto: float, descripcion: str):
        self.cantidad = self.cantidad + monto
        self.crear_movimiento(descripcion, monto)

    def desactivar(self):
        self.activa = False

    def activar(self):
        self.activa = True

    def crear_movimiento(self, descripcion: str, monto: float):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)


class CuentaJoven(Cuenta):
    def __init__(self, bonificacion, monto_inicio=0, numero_de_cuenta=0):
        Cuenta.__init__(self, monto_inicio, numero_de_cuenta)
        self.bonificacion = bonificacion


class MovimientoCuenta(object):
    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento
