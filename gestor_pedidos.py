# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

class GestorPedidos:

    def calcular_total_pedidos(self, lista_pedidos):

        total = 0
#Polimorfismo
        for pedido in lista_pedidos:
            total += pedido.calcular_total()

        return total

    def mostrar_pedidos(self, lista_pedidos):

        for pedido in lista_pedidos:
            print(pedido.mostrar_info())