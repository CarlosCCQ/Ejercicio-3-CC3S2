class Product:
    def __init__(self, id, name, description, price, stock):
        if not name or not description:
            raise ValueError("El nombre o descripcion incorrecto")
        if price <= 0 or stock < 0:
            raise ValueError("Precio o Stcock negativo")
            
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
    
    def update_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock negativo")
        self.stock = new_stock
    
    def apply_discount(self, discount_percentage):
        if not 0 <= discount_percentage <= 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        self.price = self.price * (1 - discount_percentage / 100)
    
    def summary(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock
        }