import json
from typing import List
from .product import Product

class Stock:
    """Represents the catalog of products
    
    Attributes:
        products: the list of products
    """
    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def update(self, id: int, change: int):
        """Update the quantity of a product by adding or removing
        
        Args:
            id: identifier of the product
            change: the value by which the quantity should be update (+1 adds 1, -2 removes 2 for example)
        """
        #TODO: Make sure the product exists, and that by making the change, the value is still >= 0
        
        #TODO: Update the quantity

    def getProductByID(self, id: int) -> Product:

       with open('products.json', 'r') as file:
        products = json.load(file)
       for product in products:
        if product['id'] == id:
         return Product(product['code'], product['name'], product['brand'],product['quantity'],product['category'],
                        product['description'],product['price'])
        return None
 
        """Gets a product by its ID

        Args:
            id: identifier of the product
        
        Returns: the product's object
        """
        #TODO: Implement te function
        
    def dump(self, outfile: str):

        """Saves the stock to a JSON file"""
        #TODO: Implement the function
    
    @staticmethod
    def load(infile: str):

     with open(infile, 'r') as file:
        stock_data = json.load(file)
        print("stock from an existing file", stock_data)

        """Loads the stock from an existing file
        
        Args: 
            infile: input file to the function
        """
        #TODO: Implement the function
    
    def __str__(self) -> str:
        """Returns a string representation of the stock
        """
        #TODO: Return the description of the stock with a nice output showing the ID, Name, Brand, Description, Quantity, Price, and the requires_prescription field