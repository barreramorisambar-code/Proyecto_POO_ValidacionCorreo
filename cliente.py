# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

import re

# Expresión regular para validar el formato de un correo electrónico:
# usuario@dominio.tld (usuario sin espacios ni @, dominio con al menos un punto)
PATRON_CORREO = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


class Cliente:

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            print("El nombre no puede estar vacío")
            return
        self._nombre = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if len(valor) != 10:
            raise ValueError ("El teléfono debe tener 10 caracteres")
        self._telefono = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        valor = valor.strip()
        if not PATRON_CORREO.match(valor):
            raise ValueError("El correo electrónico no tiene un formato válido")
        self._correo = valor

    @staticmethod
    def es_correo_valido(valor):
        """Permite validar un correo sin crear/modificar un Cliente."""
        return bool(PATRON_CORREO.match(valor.strip()))

    def __str__(self):
        return f"{self._nombre} - {self._telefono} - {self._correo}"