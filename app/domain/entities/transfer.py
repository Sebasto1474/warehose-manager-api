import datetime as d

class Transfer:
    def __init__(self, user, trf_type, location, destination, quantity):
        self.user = user
        self.trf_type =  trf_type
        self.location = location
        self.destination = destination
        self.quantity = quantity
        timestamp = d.now()
        

class TransferServices:
    def __init__(self):
        pass

    def transfer_in(self, location, material_id, quantity):
        if quantity <= 0:
            return "Quantity must be positive."
        if location.empty is False:
            return "Location must be empty."
        