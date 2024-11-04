import re

class User():
    def __init__(self, user_id: str, username: str, email: str, password: str):
        self.user_id = user_id
        self.username = username
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)
        self.cart = {}  
    
    def _validate_email(self, email: str) -> str:
        # Validación básica de email usando regex
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            raise ValueError("Email inválido")
        return email
    
    def _validate_password(self, password: str) -> str:
        # Requisitos mínimos: 8 caracteres, 1 mayúscula, 1 número
        if (len(password) < 8 or 
            not any(c.isupper() for c in password) or 
            not any(c.isdigit() for c in password)):
            raise ValueError("La contraseña debe tener al menos 8 caracteres, una mayúscula y un número")
        return password
    
    def register(self,username:str,email:str,password: str) -> str:
        self.username = username
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)
        return self
    
    def login(self,email:str,password:str) -> str:
        if self.email == email and self.password == password:
            return True
        return False

    def update_info(self, username: str = None, email: str = None) -> None:
        if username:
            self.username = username
        if email:
            self.email = self._validate_email(email)
    
    def add_to_cart(self, product_id: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva")
        # Aquí se debería verificar el stock disponible
        self.cart[product_id] = self.cart.get(product_id, 0) + quantity
    
    def remove_from_cart(self, product_id: str, quantity: int) -> None:
        if product_id not in self.cart:
            raise ValueError("Producto no encontrado en el carrito")
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva")
            
        current_quantity = self.cart[product_id]
        if quantity >= current_quantity:
            del self.cart[product_id]
        else:
            self.cart[product_id] = current_quantity - quantity
    
    def checkout(self) -> dict:
        if not self.cart:
            raise ValueError("El carrito está vacío")
        order = dict(self.cart)  # Crear copia del carrito
        self.cart.clear()  # Vaciar el carrito
        return order