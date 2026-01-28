class Stock:
    def __init__(self, location, material_id, quantity):
        self.location = location
        self.material_id = material_id
        self.quantity = quantity

    def increase_stock(self, value):
        if value <= 0:
            raise ValueError("Value must be greter than 0.")
        self.quantity += value

    def decrease_stock(self, value):
        if value <= 0:
            raise ValueError("Decrease value must be greater than 0.")
        if value > self.quantity:
            raise ValueError("Decrease value cannot be greater than current stock.")