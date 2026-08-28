class Product:
    """ Shop products"""

    def __init__(
        self,
        name: str,
        category: str,
        price: float,
        stock: int,
    ) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def change_price(self, new_price: float) -> None:
        """ Change product price"""
        self.price = new_price

    def change_stock(self, new_stock: int) -> None:
        """ Change product stock"""
        self.stock = new_stock


class Order:
    """ customer orders"""

    def __init__(self) -> None:
        self.order_list: list[Product] = []
        self.order_price: float = 0

    def add_product(self, product: Product) -> None:
        """ adding product to the order list"""
        self.order_list.append(product)

    def calculate_total_price(self) -> float:
        """ calculate the price"""
        self.order_price = sum(
            product.price
            for product in self.order_list
        )
        return self.order_price


class Customer:
    """ Shop customer """

    def __init__(
        self,
        name: str,
        email: str,
    ) -> None:
        self.name = name
        self.email = email
        self.orders: list[Order] = []

    def add_order(self, order: Order) -> None:
        """ Adding order to the customer list"""
        self.orders.append(order)