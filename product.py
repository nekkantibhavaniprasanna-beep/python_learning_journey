class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print("-" * 40)
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ₹{self.price}")
        print(f"Stock      : {self.stock}")
        print("-" * 40)


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))

        product = Product(product_id, name, price, stock)
        self.products.append(product)

        print("✅ Product Added Successfully!")

    def view_products(self):
        if len(self.products) == 0:
            print("No Products Available.")
            return

        print("\n===== Product List =====")

        for product in self.products:
            product.display()

    def search_product(self):
        pid = input("Enter Product ID: ")

        for product in self.products:
            if product.product_id == pid:
                print("\nProduct Found")
                product.display()
                return

        print("Product Not Found.")

    def update_stock(self):
        pid = input("Enter Product ID: ")

        for product in self.products:
            if product.product_id == pid:
                stock = int(input("Enter New Stock: "))
                product.stock = stock
                print("Stock Updated Successfully.")
                return

        print("Product Not Found.")

    def delete_product(self):
        pid = input("Enter Product ID: ")

        for product in self.products:
            if product.product_id == pid:
                self.products.remove(product)
                print("Product Deleted Successfully.")
                return

        print("Product Not Found.")