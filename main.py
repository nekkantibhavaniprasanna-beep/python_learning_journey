from product import ProductManager
from customer import CustomerManager
from cart import Cart
from order import OrderManager
from payment import PaymentManager

product_manager = ProductManager()
customer_manager = CustomerManager()
cart = Cart()
order_manager = OrderManager()
payment_manager = PaymentManager()


def pause():
    input("\nPress Enter to continue...")


# ---------------- Product Menu ----------------

def product_menu():
    while True:
        print("\n========== PRODUCT MENU ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            product_manager.add_product()
            pause()

        elif choice == "2":
            product_manager.view_products()
            pause()

        elif choice == "3":
            product_manager.search_product()
            pause()

        elif choice == "4":
            product_manager.update_stock()
            pause()

        elif choice == "5":
            product_manager.delete_product()
            pause()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


# ---------------- Customer Menu ----------------

def customer_menu():
    while True:

        print("\n========== CUSTOMER MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. View Customers")
        print("4. Search Customer")
        print("5. Delete Customer")
        print("6. Logout")
        print("7. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            customer_manager.register_customer()
            pause()

        elif choice == "2":
            customer_manager.login()
            pause()

        elif choice == "3":
            customer_manager.view_customers()
            pause()

        elif choice == "4":
            customer_manager.search_customer()
            pause()

        elif choice == "5":
            customer_manager.delete_customer()
            pause()

        elif choice == "6":
            customer_manager.logout()
            pause()

        elif choice == "7":
            break

        else:
            print("Invalid Choice")


# ---------------- Cart Menu ----------------

def cart_menu():

    while True:

        print("\n========== CART MENU ==========")
        print("1. Add To Cart")
        print("2. View Cart")
        print("3. Remove From Cart")
        print("4. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            cart.add_to_cart(product_manager)
            pause()

        elif choice == "2":
            cart.view_cart()
            pause()

        elif choice == "3":
            cart.remove_from_cart()
            pause()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")
    # ---------------- Order Menu ----------------

def order_menu():

    while True:

        print("\n========== ORDER MENU ==========")
        print("1. Place Order")
        print("2. View Orders")
        print("3. Search Order")
        print("4. Cancel Order")
        print("5. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            order_manager.place_order(customer_manager, cart)
            pause()

        elif choice == "2":
            order_manager.view_orders()
            pause()

        elif choice == "3":
            order_manager.search_order()
            pause()

        elif choice == "4":
            order_manager.cancel_order()
            pause()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")


# ---------------- Payment Menu ----------------

def payment_menu():

    while True:

        print("\n========== PAYMENT MENU ==========")
        print("1. Make Payment")
        print("2. Payment History")
        print("3. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            payment_manager.make_payment(order_manager)
            pause()

        elif choice == "2":
            payment_manager.payment_history()
            pause()

        elif choice == "3":
            break

        else:
            print("Invalid Choice")


# ---------------- Main Menu ----------------

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("      E-COMMERCE SHOPPING CART SYSTEM")
        print("=" * 55)

        print("1. Product Management")
        print("2. Customer Management")
        print("3. Shopping Cart")
        print("4. Orders")
        print("5. Payments")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            product_menu()

        elif choice == "2":
            customer_menu()

        elif choice == "3":
            cart_menu()

        elif choice == "4":
            order_menu()

        elif choice == "5":
            payment_menu()

        elif choice == "6":
            print("\nThank You For Using E-Commerce Shopping Cart System.")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()