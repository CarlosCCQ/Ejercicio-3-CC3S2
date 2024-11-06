class Order:
    order_counter = 1

    def __init__(self, order_id, user, order_items, total_amount, status="Pending"):
        self.order_id = order_id
        self.user = user
        self.order_items = order_items  
        self.total_amount = total_amount
        self.status = status

    @classmethod
    def create_order(cls, user, order_items, products):
        total_amount = 0
        for product_id, quantity in order_items.items():
            product = products.get(product_id)
            if not product:
                raise KeyError(f"El producto con ID {product_id} no existe.")
            if product.stock < quantity:
                raise ValueError(f"No hay suficiente stock para el producto '{product.name}'.")
            total_amount += product.price * quantity
        
        for product_id, quantity in order_items.items():
            products[product_id].update_stock(products[product_id].stock - quantity)
        
        order_id = cls.order_counter
        cls.order_counter += 1  
        return cls(order_id, user, order_items, total_amount)

    def process_payment(self, payment_info):
        if not self._is_payment_successful(payment_info):
            raise ValueError("El pago ha fallado.")
        
        self.status = "Completed"
        return True

    def _is_payment_successful(self, payment_info):
        return payment_info.get("payment_successful", False)

    def update_status(self, new_status):
        if new_status not in ["Pending", "Completed", "Canceled"]:
            raise ValueError("Estado de la orden inválido.")
        self.status = new_status

    def summary(self):
        return {
            "order_id": self.order_id,
            "user": self.user.username,
            "order_items": self.order_items,
            "total_amount": self.total_amount,
            "status": self.status
        }
