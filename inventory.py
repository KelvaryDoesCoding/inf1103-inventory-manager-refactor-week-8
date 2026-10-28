# Manage a collection of Product objects

from product import Product


class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    @property
    def products(self) -> tuple[Product, ...]:
        return tuple(self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Inventory can only contain Product objects.")
        if self.search_product(product.product_id) is not None:
            raise ValueError("A product with this ID already exists.")
        self.__products.append(product)

    def generate_product_id(self) -> str:
        numbers = [int(p.product_id[1:]) for p in self.__products
                   if p.product_id.startswith("P") and p.product_id[1:].isdigit()]
        return f"P{max(numbers, default=0) + 1:03d}"

    def search_product(self, product_id: str) -> Product | None:
        product_id = product_id.strip().upper()
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self.search_product(product_id)
        if product is None:
            raise ValueError("Product not found.")
        product.update_stock(quantity)

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return
        print(f"{'ID':<12} {'Name':<25} {'Price':>11} {'Stock':>8}")
        print("-" * 59)
        for product in self.__products:
            product.display_information()
