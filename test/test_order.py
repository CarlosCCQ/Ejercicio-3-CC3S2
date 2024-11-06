import pytest
from  ecommerce_plataform.order import Order 
from  ecommerce_plataform.product import Product 
from  ecommerce_plataform.user import User 

@pytest.fixture
def sample_user():
    return User(user_id="1", username="testuser", email="testuser@example.com", password="Password1")

@pytest.fixture
def sample_products():
    return {
        "product1": Product(id="product1", name="Producto 1", description="Desc 1", price=10.0, stock=10),
        "product2": Product(id="product2", name="Producto 2", description="Desc 2", price=20.0, stock=5)
    }

@pytest.fixture
def sample_order(sample_user, sample_products):
    order_items = {"product1": 2, "product2": 1}
    return Order.create_order(sample_user, order_items, sample_products)

def test_create_order_success(sample_order, sample_user):
    # Comprobar que la orden se ha creado correctamente
    assert sample_order.order_id == 1
    assert sample_order.user == sample_user
    assert sample_order.order_items == {"product1": 2, "product2": 1}
    assert sample_order.total_amount == 40.0  # (10*2 + 20*1)

def test_create_order_insufficient_stock(sample_user, sample_products):
    # Intentar crear una orden con más cantidad de la disponible en el stock
    order_items = {"product1": 11}  # Stock insuficiente para product1
    with pytest.raises(ValueError, match="No hay suficiente stock para el producto 'Producto 1'."):
        Order.create_order(sample_user, order_items, sample_products)

def test_process_payment_success(sample_order):
    # Simular información de pago exitosa
    payment_info = {"payment_successful": True}
    result = sample_order.process_payment(payment_info)
    assert result is True
    assert sample_order.status == "Completed"

def test_process_payment_failure(sample_order):
    # Simular información de pago fallida
    payment_info = {"payment_successful": False}
    with pytest.raises(ValueError, match="El pago ha fallado."):
        sample_order.process_payment(payment_info)
    assert sample_order.status == "Pending"  # El estado debe permanecer sin cambios

def test_update_status(sample_order):
    # Probar la actualización del estado
    sample_order.update_status("Completed")
    assert sample_order.status == "Completed"
    
    sample_order.update_status("Canceled")
    assert sample_order.status == "Canceled"

    # Intentar actualizar a un estado no válido
    with pytest.raises(ValueError, match="Estado de la orden inválido."):
        sample_order.update_status("InvalidStatus")
