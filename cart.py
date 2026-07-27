class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product_manager):
        product_id = input("Enter Product ID: ")

        for product in product_manager.products:
            if product.product_id == product_id:

                if product.stock <= 0:
                    print("Product Out of Stock.")
                    return

                quantity = int(input("Enter Quantity: "))

                if quantity > product.stock:
                    print("Not enough stock available.")
                    return

                self.items.append({
                    "product": product,
                    "quantity": quantity
                })

                product.stock -= quantity

                print("Product Added to Cart Successfully.")
                return

        print("Product Not Found.")

    def view_cart(self):
        if len(self.items) == 0:
            print("Cart is Empty.")
            return

        total = 0

        print("\n========== YOUR CART ==========")

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            total += subtotal

            print(f"{product.name}")
            print(f"Price    : ₹{product.price}")
            print(f"Quantity : {quantity}")
            print(f"Subtotal : ₹{subtotal}")
            print("------------------------------")

        print(f"Total Amount : ₹{total}")

    def remove_from_cart(self):
        product_id = input("Enter Product ID to Remove: ")

        for item in self.items:

            if item["product"].product_id == product_id:

                item["product"].stock += item["quantity"]

                self.items.remove(item)

                print("Product Removed Successfully.")
                return

        print("Product Not Found in Cart.")

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["product"].price * item["quantity"]

        return total

    def clear_cart(self):
        self.items.clear()