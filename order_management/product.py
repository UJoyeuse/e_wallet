class Product:
    """Class representing a medication / product in the project.

    Attributes:
        code: unique identifier of the product (string)
        name: name of the product (string)
        brand: the brand of the product (string)
        description: a textual description of the project (string)
        quantity: the quantity of products available in the stock (int)
        price: unit price of the project (float)
        dosage_instruction: instructions to take the medicine (string, optional)
        requires_prescription: whether the medication requires a prescription (bool)
        
    """
    def __init__(
            self, 
            code: int, 
            name: str, 
            brand: str,
            description: str,
            quantity: int, 
            price: float, 
            dosage_instruction: str,
            requires_prescription: bool,
            category: str) -> None:
        self.code = code
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.category = category
        self.description = description
        self.price = price
        self.dosage_instruction = dosage_instruction
        self.requires_prescription = (requires_prescription != 0)

    def to_json(self) -> str:
        """Returns a valid JSON representation of the object

        Arguments:

        Returns: A JSON string.
        """
        #TODO: Implement the function
        return NotImplemented

    def __str__(self) -> str:
        return self.name