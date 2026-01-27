class Location:
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number
        self.location = letter + number
        self.is_available = False
        self.positions = 0

    def __str__(self):
        return f"Location: {self.location}"

    def empty(self):
        if self.availability:
            self.availability = False
        self.positions -= 1
        return f"Location set as empty."

    def fill(self):
        if not self.availability:
            self.availability = True
        self.positions += 1
        return f"Location set as occupied."