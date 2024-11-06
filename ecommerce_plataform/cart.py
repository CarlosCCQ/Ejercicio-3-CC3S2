class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if product_id not in self.items:
            self.items[product_id] = quantity
        else:
            self.items[product_id] += quantity

    def remove_item(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if product_id in self.items:
            if self.items[product_id] <= quantity:
                del self.items[product_id]
            else:
                self.items[product_id] -= quantity
        else:
            raise KeyError("El producto no se encuentra en el carrito.")

    def calculate_total(self, products):
        total = 0
        for product_id, quantity in self.items.items():
            product = products.get(product_id)
            if not product:
                raise KeyError(f"El producto con ID {product_id} no existe.")
            if product.stock < quantity:
                raise ValueError(f"No hay suficiente stock para el producto '{product.name}'.")
            total += product.price * quantity
        return total

    def clear_cart(self):
        self.items.clear()
