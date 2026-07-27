class Customer:
    def __init__(self, customer_id, name, email, password):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password


class CustomerManager:
    def __init__(self):
        self.customers = []
        self.logged_in_customer = None

    def register_customer(self):
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Create Password: ")

        for customer in self.customers:
            if customer.email == email:
                print("Email already registered.")
                return

        new_customer = Customer(customer_id, name, email, password)
        self.customers.append(new_customer)

        print("Customer Registered Successfully.")

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        for customer in self.customers:
            if customer.email == email and customer.password == password:
                self.logged_in_customer = customer
                print(f"\nWelcome {customer.name}")
                return

        print("Invalid Email or Password.")

    def logout(self):
        if self.logged_in_customer:
            print(f"{self.logged_in_customer.name} Logged Out.")
            self.logged_in_customer = None
        else:
            print("No customer is currently logged in.")

    def view_customers(self):
        if not self.customers:
            print("No Customers Found.")
            return

        print("\n===== Customer List =====")

        for customer in self.customers:
            print("-" * 40)
            print(f"Customer ID : {customer.customer_id}")
            print(f"Name        : {customer.name}")
            print(f"Email       : {customer.email}")

    def search_customer(self):
        cid = input("Enter Customer ID: ")

        for customer in self.customers:
            if customer.customer_id == cid:
                print("\nCustomer Found")
                print(f"ID    : {customer.customer_id}")
                print(f"Name  : {customer.name}")
                print(f"Email : {customer.email}")
                return

        print("Customer Not Found.")

    def delete_customer(self):
        cid = input("Enter Customer ID: ")

        for customer in self.customers:
            if customer.customer_id == cid:
                self.customers.remove(customer)
                print("Customer Deleted Successfully.")
                return

        print("Customer Not Found.")