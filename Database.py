class Database( object ):
	'''	This class use to store products
	'''
	def __init__( self ):
		self.products = {}

	def add( self, product ):
		'''	Add new product to database

			Parameters:
				product (Product) - the product to add to database
		'''
		#	Add product by id
		self.products[ product.getId() ] = product

	def findProduct( self, productId ):
		'''	Find a product in database
		
			Parameters:
				productId (int) - id of the product to find in database
			Returns:
				Product - founded product
		'''
		#	Check have product that matched with the given productId in database
		#		if founded, then return matched product 
		if( productId in self.products ):
			return self.products[ productId ]

		#	If not founded, return None
		return None