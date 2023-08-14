import json
from .product import Product
from .stock import Stock

class Cart:
    """Represents a cart with a list of products and quantity

    Attributes:
        products: a dictionary with the key being the ID of the products, and the value being the quantity
        added
    """
    def __init__(self, stock: Stock) -> None:
        self.products = {}
        self.stock = stock

    def add(self, productCode: str, quantity: int):
        """Adds a product to the cart with the specified quantity
        
        Args:
            productCode: the identifier of the product
            quantity: quantity to add

        Returns: None
        """
        #TODO: Make sure the quantity is valid (> 0 and <= to the quantity in the stock)
        #TODO: If the product was already in the cart, increment the quantity
        
        #TODO: After the checks, add the product to the dictionary

    def __str__(self) -> str:
        """String representation of the cart
        """
        #TODO: Return a string representation of a cart that shows the products, their quantity, unit price, total price. And also the total price of the cart
        # Feel free to format it the way you want to
        return NotImplemented

    def remove(self, code, infile: str):

     with open(infile, 'r') as file:
      cart = json.load(file)
      for product in cart:
        if product['code'] == code:
          cart.remove(product)
          print("product removed successfully")
        else:
         print("product not found")
         
 
        """
        Removes a specific product from the cart """
        #TODO: Removes a product from the cart. safely fail if the product code is not found

    def clear(self):
        """Clears up the cart.
        """

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        #TODO: implement the function

    