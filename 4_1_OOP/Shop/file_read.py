from models import Customer, Product


def load_products(file_path: str) -> list[Product]:
    """ Upload products from txt"""
    products = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            name, category, price, stock = line.strip().split(",")

            product = Product(
                name=name,
                category=category,
                price=float(price),
                stock=int(stock),
            )

            products.append(product)

    return products


def load_customers(file_path: str) -> list[Customer]:
    """ Upload customers from txt"""
    customers = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            name, email = line.strip().split(",")

            customer = Customer(
                name=name,
                email=email,
            )

            customers.append(customer)

    return customers