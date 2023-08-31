
class Comprar:
    def __init__(self, category, style, price, cantidad):
        self.category = category
        self.style = style
        self.price = price
        self.cantidad = cantidad
    
    def comprar(self):
        total = self.price * self.cantidad
        return f"Su compra es de (cantidad={self.cantidad}), (category={self.category}), (style={self.style}), y su monto a pagar es de (total={total})"