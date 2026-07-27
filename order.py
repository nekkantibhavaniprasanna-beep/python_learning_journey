from datetime import datetime


class order:
    def __init__(self, order_id, customer_name, items, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.status = "Placed"

    def display(self):
        print("\n" + "=" * 50)
        print(f"Order ID      : {self.order_id}")
        print(f"Customer      : {self.customer_name}")
        print(f"Order Date    : {self.date}")
        print(f"Order Status  : {self.status}")
        print("-" * 50)

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]

            print(f"{product.name}")
            print(f"Price    : ${product.price}")
            print(f"Quantity : {quantity}")
            print("-" * 30)

        print(f"Total Amount : ${self.total_amount}")
        print("=" * 50)


class OrderManager:
    def __init__(self):
        self.orders = []
        self.order_count = 1000

    def place_order(self, customer_manager, cart):
        if customer_manager.logged_in_customer is None:
            print("Please Login First.")
            return

        if len(cart.items) == 0:
            print("Cart is Empty.")
            return

        self.order_count += 1

        order = Order(
            self.order_count,
            customer_manager.logged_in_customer.name,
            cart.items.copy(),
            cart.calculate_total()
        )

        self.orders.append(order)

        print("\nOrder Placed Successfully.")
        print(f"Order ID : {order.order_id}")

        cart.clear_cart()

    def view_orders(self):
        if len(self.orders) == 0:
            print("No Orders Found.")
            return

        for order in self.orders:
            order.display()

    def search_order(self):
        oid = int(input("Enter Order ID: "))

        for order in self.orders:
            if order.order_id == oid:
                order.display()
                return

        print("Order Not Found.")

    def cancel_order(self):
        oid = int(input("Enter Order ID: "))

        for order in self.orders:
            if order.order_id == oid:
                order.status = "Cancelled"
                print("Order Cancelled Successfully.")
                return

        print("Order Not Found.")