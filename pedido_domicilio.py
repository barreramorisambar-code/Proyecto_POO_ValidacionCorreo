# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

from dominio.servicio_restaurante import ServicioRestaurante


class PedidoDomicilio(ServicioRestaurante):

    def __init__(self, codigo, cliente, total_incluido_IVA, recargo_entrega):
        super().__init__(codigo, cliente, total_incluido_IVA)
        self.recargo_entrega = recargo_entrega

    @property
    def recargo_entrega(self):
        return self._recargo_entrega

    @recargo_entrega.setter
    def recargo_entrega(self, valor):
        if valor < 0:
            print("El recargo no puede ser negativo")
            return
        self._recargo_entrega = valor

    def calcular_total(self):
        return self._total_incluido_IVA + self._recargo_entrega

    def mostrar_info(self):
        return (
            f"Pedido a Domicilio | "
            f"Cliente: {self._cliente} | "
            f"Total: ${self.calcular_total()}"
        )

    def __str__(self):
        return self.mostrar_info()