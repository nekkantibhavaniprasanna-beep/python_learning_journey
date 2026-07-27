from datetime import datetime


class Payment:
    def __init__(self, payment_id, order_id, amount, method):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.method = method
        self.status = "Success"
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def receipt(self):
        print("\n" + "=" * 45)
        print("          PAYMENT RECEIPT")
        print("=" * 45)
        print(f"Payment ID : {self.payment_id}")
        print(f"Order ID   : {self.order_id}")
        print(f"Amount     : ${self.amount}")
        print(f"Method     : {self.method}")
        print(f"Status     : {self.status}")
        print(f"Date       : {self.date}")
        print("=" * 45)


class PaymentManager:
    def __init__(self):
        self.payments = []
        self.payment_count = 5000

    def make_payment(self, order_manager):

        if len(order_manager.orders) == 0:
            print("No Orders Available.")
            return

        order = order_manager.orders[-1]

        print("\nSelect Payment Method")
        print("1. Cash")
        print("2. UPI")
        print("3. Debit/Credit Card")

        choice = input("Enter Choice: ")

        if choice == "1":
            method = "Cash"

        elif choice == "2":
            method = "UPI"

        elif choice == "3":
            method = "Card"

        else:
            print("Invalid Payment Method")
            return

        self.payment_count += 1

        payment = Payment(
            self.payment_count,
            order.order_id,
            order.total_amount,
            method
        )

        self.payments.append(payment)

        print("\nPayment Successful.")
        payment.receipt()

    def payment_history(self):

        if len(self.payments) == 0:
            print("No Payment History.")
            return

        for payment in self.payments:
            payment.receipt()