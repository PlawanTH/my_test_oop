from Database import Database
from Product import Product, DiscountProduct, FreeMoreProduct, NormalProduct
from Cashier import Cashier

def main():
	#	Create new database to add products
	db = Database()

	#	Create new products
	product1 = DiscountProduct(11, 40, 20, name = "Toothbrush")
	product2 = FreeMoreProduct(33, 30, 2, name = "Toothpaste")
	product3 = NormalProduct(44, 50, name = "Shampoo")

	#	Add product to database
	db.add( product1 )
	db.add( product2 )
	db.add( product3 )

	#	Let's buy
	cashier = Cashier(db)
	cashier.checkBill(11, 1)
	cashier.checkBill(33, 2)
	cashier.checkBill(44, 3)

if __name__ == '__main__':
	main()