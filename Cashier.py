from PriceComputer import PriceComputerFactory, \
							DiscountProductPriceComputer, \
							FreeMoreProductPriceComputer, \
							NormalProductPriceComputer

#
#	Cashier
#
class Cashier( object ):
	'''	This class use to compute total price of bought products
	'''
	def __init__( self, db ):
		#	Inject database
		self.db = db

	def checkBill( self, productId, amount ):
		'''	Compute final price of a product
			by print an information to the console

			Parameters:
				productId (int) - a product id that have to compute total price
				amount (int) - an amount to compute total price
		'''
		#	Find product in database
		product = self.db.findProduct( productId )

		#	Check product was not founded
		#		then return
		if( product == None ):
			print( "No product id '{}' exists.".format( productId ) )
			return

		#	If the product was founded, get price computer by product
		#		and get computed total price from computer
		priceComputer = PriceComputerFactory.getPriceComputer( product )
		totalPrice = priceComputer.getTotalPrice( product, amount )

		#	Print buy info to the console
		print( "Name: {}, Price: {}, Product Type: {}, Discount Price: {}, Amount: {}, Total Price: {}".format(
			product.getName(), product.getPrice(), product.getProductType(), product.getFinalPrice(), amount, totalPrice
		) )