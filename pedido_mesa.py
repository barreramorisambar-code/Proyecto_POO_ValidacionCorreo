# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

from dominio.servicio_restaurante import ServicioRestaurante


class PedidoMesa(ServicioRestaurante):

    def __init__(self, codigo, cliente, total_incluido_IVA, servicio):
        super().__init__(codigo, cliente, total_incluido_IVA)
        self.servicio = servicio

    @property
    def servicio(self):
        return self._servicio

    @servicio.setter
    def servicio(self, valor):
        if valor < 0:
            print("El servicio no puede ser negativo")
            return
        self._servicio = valor

    def calcular_total(self):
        return self._total_incluido_IVA + self._servicio

    def mostrar_info(self):
        return (
            f"Pedido en Mesa | "
            f"Cliente: {self._cliente} | "
            f"Total: ${self.calcular_total()}"
        )

    def __str__(self):
        return self.mostrar_info()
