import csv
from datetime import date
from datetime import datetime
from typing import List

from modelos import Persona, Cuenta, CuentaJoven


def str_to_date(date_as_str: str) -> date:
    return datetime.strptime(date_as_str, "%Y-%m-%d").date()


def procesar_archivo(nombre_archivo: str) -> List[Persona]:
    personas = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    next(archivo_csv)
    numero_cuenta = 1
    for nombre, dni, fecha_nacimiento in archivo_csv:
        fecha_nacimiento = str_to_date(fecha_nacimiento)
        persona = Persona(nombre, dni, fecha_nacimiento)
        if not persona.es_mayor_de_edad():
            print("Error la persona es menor de 18 años")
        elif 18 <= persona.edad <= 30:
            cuenta = CuentaJoven(10, numero_de_cuenta=numero_cuenta)
        else:
            cuenta = Cuenta(numero_de_cuenta=numero_cuenta)
        persona.agregar_cuenta(cuenta)
        numero_cuenta += 1
        personas.append(persona)
    archivo.close()
    return personas
