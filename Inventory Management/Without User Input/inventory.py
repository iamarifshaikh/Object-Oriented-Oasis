from product import Product

class Inventory:
    def __init__(self):
        self.products = []
               
    def addProduct(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            return f"Product '{product._name}' added successfully"
        else:
            raise TypeError("Product must be of type Product")
    
    def removeProduct(self,productName):
        self.products = [product for product in self.products if isinstance(product,Product) and product._name != productName]
        
    def __repr__(self):
        return f"Inventory(products: {self.products})"
    
    @classmethod
    def getTotalValue(cls,products):
        totalValue = sum(product.getPrice() * product.getQuantity() for product in products)
        return totalValue
    
    @staticmethod
    def findProduct(products,productName):
        product = next((product for product in products if product._name == productName), None)
        return product