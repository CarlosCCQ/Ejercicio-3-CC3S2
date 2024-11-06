import pytest
from ecommerce_plataform.user import User


# Pruebas para el método _validate_email
def test_validate_email_valid():
    # Cobertura de sentencias y condiciones: verifica una dirección de email válida
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "Password1"
    
    # Act
    user = User(user_id, username, email, password)
    
    # Assert
    assert user.email == "valid@example.com"

def test_validate_email_invalid():
    # Cobertura de ramas y condición/decisión modificada (MC/DC): verifica el manejo de un email inválido
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "invalid-email"
    password = "Password1"
    
    # Act & Assert
    with pytest.raises(ValueError):
        User(user_id, username, email, password)

# Pruebas para el método _validate_password
def test_validate_password_valid():
    # Cobertura de sentencias: verifica que una contraseña válida pase todas las condiciones
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "Password1"
    
    # Act
    user = User(user_id, username, email, password)
    
    # Assert
    assert user.password == "Password1"

def test_validate_password_short():
    # Cobertura de ramas: verifica el caso de una contraseña demasiado corta
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "Pwd1"
    
    # Act & Assert
    with pytest.raises(ValueError):
        User(user_id, username, email, password)

def test_validate_password_no_uppercase():
    # Cobertura de condiciones: verifica que falle si falta una letra mayúscula
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "password1"
    
    # Act & Assert
    with pytest.raises(ValueError):
        User(user_id, username, email, password)

def test_validate_password_short():
    # Cobertura de condiciones y sentencias: 
    # Este test verifica que falle cuando la contraseña tiene menos de 8 caracteres.
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "Pwd1"  # Contraseña de solo 4 caracteres
    
    # Act & Assert
    with pytest.raises(ValueError, match="La contraseña debe tener al menos 8 caracteres"):
        User(user_id, username, email, password)

def test_validate_password_no_uppercase():
    # Cobertura de condiciones y sentencias:
    # Este test verifica que falle cuando la contraseña no contiene una letra mayúscula.
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "password1"  # Contraseña sin mayúsculas
    
    # Act & Assert
    with pytest.raises(ValueError, match="La contraseña debe tener al menos una letra mayúscula"):
        User(user_id, username, email, password)

def test_validate_password_no_digit():
    # Cobertura de condiciones y sentencias:
    # Este test verifica que falle cuando la contraseña no contiene un número.
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "Password"  # Contraseña sin números
    
    # Act & Assert
    with pytest.raises(ValueError, match="La contraseña debe tener al menos un número"):
        User(user_id, username, email, password)

def test_validate_password_valid():
    # Cobertura de camino y sentencias:
    # Este test verifica que una contraseña válida pase todas las condiciones sin levantar excepciones.
    # Arrange
    user_id = "1"
    username = "testuser"
    email = "valid@example.com"
    password = "Password1"  # Contraseña válida que cumple todos los requisitos
    
    # Act
    user = User(user_id, username, email, password)
    
    # Assert
    assert user.password == "Password1"

# Pruebas para el método register
def test_register_user():
    # Cobertura de sentencias y condiciones: registra un nuevo usuario correctamente
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act
    user.register("newuser", "new@example.com", "Password2")
    
    # Assert
    assert user.username == "newuser"
    assert user.email == "new@example.com"
    assert user.password == "Password2"

# Pruebas para el método login
def test_login_successful():
    # Cobertura de caminos: verifica el camino de autenticación exitosa
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act
    result = user.login("user@example.com", "Password1")
    
    # Assert
    assert result == True

def test_login_unsuccessful():
    # Cobertura de caminos y condición/decisión modificada (MC/DC): verifica autenticación fallida
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act
    result = user.login("user@example.com", "wrongpassword")
    
    # Assert
    assert result == False

# Pruebas para el método update_info
def test_update_info_username():
    # Cobertura de sentencias: verifica la actualización del nombre de usuario
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act
    user.update_info(username="updateduser")
    
    # Assert
    assert user.username == "updateduser"

def test_update_info_email():
    # Cobertura de condición/decisión modificada (MC/DC): verifica la actualización de email
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act
    user.update_info(email="updated@example.com")
    
    # Assert
    assert user.email == "updated@example.com"

# Pruebas para el método add_to_cart
def test_add_to_cart():
    # Cobertura de sentencias y ramas: verifica que el producto se añada al carrito correctamente
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act
    user.add_to_cart("product1", 2)
    
    # Assert
    assert user.cart["product1"] == 2

def test_add_to_cart_invalid_quantity():
    # Cobertura de condiciones: verifica que falle si la cantidad es negativa
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act & Assert
    with pytest.raises(ValueError):
        user.add_to_cart("product1", -1)

# Pruebas para el método remove_from_cart
def test_remove_from_cart():
    # Cobertura de caminos y condiciones: verifica eliminación de producto con cantidad válida
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    user.add_to_cart("product1", 5)
    
    # Act
    user.remove_from_cart("product1", 3)
    
    # Assert
    assert user.cart["product1"] == 2

def test_remove_from_cart_invalid_quantity():
    # Cobertura de condiciones: verifica que falle si la cantidad es negativa
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act & Assert
    with pytest.raises(ValueError):
        user.remove_from_cart("product1", -1)

def test_remove_from_cart_not_in_cart():
    # Cobertura de ramas: verifica que falle si el producto no está en el carrito
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act & Assert
    with pytest.raises(ValueError):
        user.remove_from_cart("product2", 1)

# Pruebas para el método checkout
def test_checkout():
    # Cobertura de caminos: verifica el proceso de checkout exitoso
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    user.add_to_cart("product1", 1)
    user.add_to_cart("product2", 2)
    
    # Act
    order = user.checkout()
    
    # Assert
    assert order == {"product1": 1, "product2": 2}
    assert user.cart == {}

def test_checkout_empty_cart():
    # Cobertura de condiciones: verifica que falle si el carrito está vacío
    # Arrange
    user = User("1", "user", "user@example.com", "Password1")
    
    # Act & Assert
    with pytest.raises(ValueError):
        user.checkout()