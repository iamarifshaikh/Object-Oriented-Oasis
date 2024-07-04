class Product:
    def __init__(self,name,price,quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def getPrice(self):
        return self._price

    def setPrice(self,price):
        if price > 0:
            self._price = price
        else:
            raise ValueError("Price must be greater than 0")
        
    def getQuantity(self):
        return self._quantity
    
    def setQuantity(self,quantity):
        if quantity > 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be greater than 0")
    
    def __str__(self):
        return f"Product(name={self._name}, price={self._price}, quantity={self._quantity})"