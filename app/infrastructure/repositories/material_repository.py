class MaterialRepository:
    def __init__(self):
        pass

    def get_by_id(self, material_id):
        pass

    def create(self, material_id, description):
        new_material = Material(material_id, description)
        return new_material

