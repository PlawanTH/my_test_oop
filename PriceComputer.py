from Product import DiscountProduct, FreeMoreProduct, NormalProduct

#
#	Price Computer
#
class PriceComputer( object ):
	'''	This class use to compute the price for each product type
	'''
	def getTotalPrice( self, product, amount ):
		'''	Get total price from the given product and amount
		'''
		raise NotImplementedError()

class NormalProductPriceComputer( PriceComputer ):
	'''	This class use to compute the price for normal product type
	'''
	def getTotalPrice( self, product, amount ):
		'''	Get total price from the given product and amount
		'''
		#	Downcast to NormalProduct
		return product.price * amount

class DiscountProductPriceComputer( PriceComputer ):
	'''	This class use to compute the price for discount product type
	'''
	def getTotalPrice( self, product, amount ):
		'''	Get total price from the given product and amount
		'''
		#	Downcast to DiscountProduct
		return product.getFinalPrice() * amount

class FreeMoreProductPriceComputer( PriceComputer ):
	'''	This class use to compute the price for get more free product type
	'''
	def getTotalPrice( self, product, amount ):
		'''	Get total price from the given product and amount
		'''
		#	Downcast to FreeMoreProduct
		finalAmount = int( amount / product.freeAmount )
		if( amount % product.freeAmount != 0 ):
			finalAmount += 1 
			
		return finalAmount * product.price

#
#	Price Computer Factory
#
class PriceComputerFactory( object ):
	'''	This class is a factory to get price computer
	'''
	@staticmethod
	def getPriceComputer( product ):
		'''	Returns price computer by the given product

			Parameters:
				product (Product) - a product to get price computer
			Returns:
				PriceComputer - a computer to compute a product for each type
		'''
		if( isinstance( product, NormalProduct ) ):
			return NormalProductPriceComputer()
		elif( isinstance( product, DiscountProduct ) ):
			return DiscountProductPriceComputer()
		elif( isinstance( product, FreeMoreProduct ) ):
			return FreeMoreProductPriceComputer()

		raise ValueError("Product promotion type is not supported for this system.")