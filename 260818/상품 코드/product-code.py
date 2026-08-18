product_name, product_code = input().split()
product_code = int(product_code)

class Product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

product1 = Product()
product2 = Product(product_name, product_code)

print("product", product1.code, "is", product1.name)
print("product", product2.code, "is", product2.name)