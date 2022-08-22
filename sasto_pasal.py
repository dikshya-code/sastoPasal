from unicodedata import category
from db_helper import fetch_data
from order import Order
from product import Product

TAX = 10

class SastoPasal:
    def __init__(self):
        self.order_list = []
        self.product_list = []
        self.set_products_from_db()

    def take_order(self):
        print("=" * 180)
        print(f"{'WELCOME TO SASTO PASAL':>100}")
        print("=" * 180)
        self.available_products()
        while True:
            order_id = int(input("Please enter the product number: "))
            if order_id < 0 or order_id > len(self.product_list):
                print("Entered product number not found. Please try again")
                continue
            quantity = int(input("Please enter quantity: "))
            self.order_list.append(
                Order(quantity=quantity, product=self.product_list[order_id - 1])
            )
            print("\n")
            continue_buy = input("You want to continue shopping ? Please enter yes to continue: ")
            if continue_buy == "yes":
                continue
            break
        print("=" * 180)
        print(f"{'THANK YOU FOR SHOPPING WITH SASTO PASAL':>100}")
        print("=" * 180)
        self.generate_bill()

    def generate_bill(self):
        bill_file = open("bill.txt", "w")
        bill_file.write("=" * 180 + "\n")
        bill_file.write(f"{'SASTO PASAL':>83}\n")
        bill_file.write("=" * 180 + "\n")

        bill_file.write(f"{'Product':<110}{'Unit':<10}{'Price':<10}{'Total'}\n\n")
        grand_total = 0
        for order in self.order_list:
            product_total = order.quantity * order.product.price
            bill_file.write(
                f"{order.product.title:<110}{order.quantity:<10}{order.product.price:<10}{product_total}\n")
            grand_total += product_total
        bill_file.write("\nTOTAL: {}\n".format(grand_total))
        bill_file.write("TAX: {}%\n".format(TAX))
        bill_file.write("Grand Total: {}\n".format(grand_total + ((grand_total * TAX) / 100)))
        bill_file.write("=" * 180 + "\n")
        bill_file.write(f"{'THANK YOU FOR SHOPPING WITH SASTO PASAL':>100}\n")
        bill_file.write("=" * 180 + "\n")

    def available_products(self):
        print(f"{'Product:':<110}{'Price':<10}{'Category'}")
        for product in self.product_list:
            print(
                f"{str(product.id) + '. ' + product.title + ':':<110}{str(product.price) + '':<10}{product.category}")
        print("\n")

    def set_products_from_db(self):
        query = "SELECT *FROM products"
        rows = fetch_data(query=query)
        for row in rows:
            self.product_list.append(Product(
                id=row[0],
                title=row[1],
                price=row[2],
                description=row[3],
                category=row[4],
                image=row[5],
            )
            )