from paquete.modulo1 import Cliente

class Comprar(Cliente): 
      def __init__(self, category, style, price, cantidad, nombre, apellido, edad, correo, genero):
        super().__init__(nombre, apellido, edad, correo, genero)
        self.category = category
        self.style = style
        self.price = price
        self.cantidad = cantidad
    
     
      def calcular_total(self):
        total = self.price * self.cantidad
        return total

    
      def __str__(self):
       total = self.calcular_total()
       return f"Compra de {self.nombre} {self.apellido}:\n" \
               f"Cantidad: {self.cantidad}\n" \
               f"Categoría: {self.category}\n" \
               f"Estilo: {self.style}\n" \
               f"Monto total: {total}"

    