from product import Product
from inventory import Inventory

def main():
    inventory = Inventory()

    # Testing the Inventory and Product classes
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Phone", 500, 10)

    inventory.addProduct(product1)
    inventory.addProduct(product2)

    print(inventory)

    inventory.removeProduct("Laptop")
    print(inventory)

    total_value = Inventory.getTotalValue(inventory.products)
    print(f"Total value of inventory: ${total_value}")

    found_product = Inventory.findProduct(inventory.products, "Phone")
    if found_product:
        print(f"Found product: {found_product}")
    else:
        print("Product not found in inventory.")
        
if __name__ == "__main__":
    main()