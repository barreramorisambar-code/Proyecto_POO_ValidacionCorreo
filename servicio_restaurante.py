# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

class ServicioRestaurante:

    def __init__(self, codigo, cliente, total_incluido_IVA):
        self.codigo = codigo
        self.cliente = cliente
        self.total_incluido_IVA = total_incluido_IVA

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor == "":
            print("El código no puede estar vacío")
            return
        self._codigo = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if valor == "":
            print("El cliente no puede estar vacío")
            return
        self._cliente = valor

    @property
    def total_incluido_IVA(self):
        return self._total_incluido_IVA

    @total_incluido_IVA.setter
    def total_incluido_IVA(self, valor):
        if valor < 0:
            print("El total no puede ser negativo")
            return
        self._total_incluido_IVA = valor

    def calcular_total(self):
        return self._total_incluido_IVA

    def mostrar_info(self):
        return f"Código: {self._codigo} | Cliente: {self._cliente}"

    def __str__(self):
        return self.mostrar_info()