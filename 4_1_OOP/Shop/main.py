from file_read import load_customers, load_products
from models import Order


def main() -> None:
    """ run the shop app """
    products = load_products("data/products.txt")
    customers = load_customers("data/customers.txt")

    order = Order()

    order.add_product(products[0])
    order.add_product(products[1])

    customers[0].add_order(order)

    print(f"Customer: {customers[0].name}")
    print(f"Email: {customers[0].email}")
    print(f"Order price: {order.calculate_total_price()}")
    print(f"Orders count: {len(customers[0].orders)}")


if __name__ == "__main__":
    main()