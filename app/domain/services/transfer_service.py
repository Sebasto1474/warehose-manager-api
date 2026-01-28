class TransferServices:
    def __init__(self):
        pass

    def transfer_in(self, location, material_id, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if not location.available():
            raise TypeError("Location must be available")
        if material_id