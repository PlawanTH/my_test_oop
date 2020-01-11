#
#	Product
#
class Product( object ):
	'''	This class use to store an information of a product
	'''
	def __init__( self, prodId, price, name = "" ):
		self.prodId = prodId
		self.price = price
		self.name = name

	def getId( self ):
		'''	Returns product id
		'''
		return self.prodId

	def getPrice( self ):
		'''	Returns price of a product
		'''
		return self.price

	def getName( self ):
		'''	Returns name of a product
		'''
		return self.name

	def getFinalPrice( self ):
		'''	Returns final price of a product,
			include additional computation
		'''
		raise NotImplementedError()

	def getProductType( self ):
		'''	Get type of the product
		'''
		raise NotImplementedError()

#
#	Inherit product
#
class DiscountProduct( Product ):
	'''	This class use to store an information of a discount product
	'''
	def __init__( self, prodId, price, percent, name = "" ):
		super( DiscountProduct, self ).__init__( prodId, price, name = name )
		self.percent = percent

	def getFinalPrice( self ):
		'''	Returns final price of a product,
			include additional computation
		'''
		return self.price * ( 1.0 - ( self.percent / 100.0 ) )

	def getProductType( self ):
		'''	Get type of the product
		'''
		return "Discount {} %".format( self.percent )

class FreeMoreProduct( Product ):
	'''	This class use to store an information of a get free product
	'''
	def __init__( self, prodId, price, freeAmount, name = "" ):
		super( FreeMoreProduct, self ).__init__( prodId, price, name = name )
		self.freeAmount = freeAmount

	def getFinalPrice( self ):
		'''	Returns final price of a product,
			include additional computation
		'''
		return self.price

	def getProductType( self ):
		'''	Get type of the product
		'''
		return "Free {}".format( self.freeAmount )

class NormalProduct( Product ):
	def __init__( self, prodId, price, name = "" ):
		super( NormalProduct, self ).__init__( prodId, price, name = name )

	def getFinalPrice( self ):
		'''	Returns final price of a product,
			include additional computation
		'''
		return self.price

	def getProductType( self ):
		'''	Get type of the product
		'''
		return "Normal Product"