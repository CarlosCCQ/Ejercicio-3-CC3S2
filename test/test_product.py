import pytest 
from ecommerce_plataform.product import Product  

def test_product_creation():
    #Arrange
    id = 1
    name = "Arroz"
    description = "Saco de arroz altomayo"
    price = 10.99
    stock = 15
    #Act
    product = Product(id , name , description , price , stock)
    #Assert
    assert product.id == id
    assert product.name == name
    assert product.description == description
    assert product.price == price 
    assert product.stock == stock 

def test_fail_product_creation():
    #Arrange
    id = 1
    name = " "
    description = "Saco de arroz altomayo"
    price = -10.99
    stock = 15
    #Act
    product = Product(id , name , description , price , stock)
    #Assert
    assert product.id == id
    assert product.name == name
    assert product.description == description
    assert product.price == price 
    assert product.stock == stock 

def test_update_stock():
    #Arrange
    new_stock = 12
    #Act
    product = Product(1, "Arroz", "Saco de arroz altomayo", 10.99, 15)
    product.update_stock(new_stock)
    #Assert
    assert product.stock == new_stock

def test_fail_update_stock():
    #Act
    new_stock = -12
    #Arrange
    product = Product(1, "Arroz", "Saco de arroz altomayo", 10.99, 15)
    product.update_stock(new_stock)
    #Assert
    assert product.stock == new_stock

def test_apply_discount():
    #Arrange
    discount_percentage = 20
    original_price = 10.99
    expected_price = 8.792  # 10.99 - (10.99 * 0.20)
    #Act
    product = Product(1, "Arroz", "Saco de arroz altomayo", original_price, 15)
    product.apply_discount(discount_percentage)
    #Assert
    assert product.price == expected_price
