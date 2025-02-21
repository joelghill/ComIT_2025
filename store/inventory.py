from uuid import uuid4


class InventoryItem:
    total = 0

    def __init__(self, name: str, price: float, stock: int = 0):
        self.name = name
        self.price = price
        self.stock = stock

        # Generate unique ID from UUID4
        self.id = str(uuid4())

        # Increment inventory by 1
        InventoryItem.total += 1

    def __str__(self) -> str:
        return f"({self.id}){self.name} - {self.price}. Stock: {self.stock}"

    def is_available(self) -> bool:
        return self.stock > 0
    
    def add_stock(self, units: int):
        self.stock += units

    def remove_from_stock(self, number: int):
        remaining = self.stock - number
        if remaining >= 0:
            self.stock = remaining
        else:
            raise Exception("Not enough stock")

# Hard coded store of all items in inventory
_inventory = [
    InventoryItem("Nintendo Switch 2", 999.99),
    InventoryItem("BBQ Chips", 3.50),
    InventoryItem("Pokemon Booster: Flaming Tides", 7.00),
    InventoryItem("Gaterade", 5.00),
    InventoryItem("Milk", 4.99),
    InventoryItem("Advil", 9.99),
    InventoryItem("Cat Fud", 49.99),
]

# Helper function to return what other modules expect
def get_inventory() -> list[tuple[str, float]]:
    return [(item.name, item.price) for item in _inventory]
