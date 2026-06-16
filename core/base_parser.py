class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Categoty: {self.category} | {self.name} - ${self.price:.1f}"  

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented  
        return self.price < other.price
    

if __name__ == "__main__":
    products_list = [
        Product("Laptop", 100.0, "Electronics"),
        Product("Smartphone", 500.0, "Electronics"),
        Product("Headphones", 300.0, "Audio"),]
    
    for product in products_list:
        print(product)
    
    products_list.sort()
    print("\nSorted products:")
    for product in products_list:        
        print(product)