class Ramen:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        return f"Preparing a bowl of {self.name} ramen."

class TonkotsuRamen(Ramen):
    def prepare(self):
        return f"Simmering pork bones for hours to make {self.name}"
    
    def serve(self):
        return f"Serving the crazy Tonkotsu! Here it is: {self.name}"
    
class ShoyuRamen(Ramen):
    def prepare(self):
        return f"Mixing soy sauce base to prepare {self.name}"
    
    def serve(self):
        return f"Serving the shambolic Shoyu! Here it is: {self.name}"

class MisoRamen(Ramen):
    def prepare(self):
        return f"Blending miso paste for flavorful {self.name}"
    
    def serve(self):
        return f"Serving the mental Miso! Here it is: {self.name}"

class SpicyRamen(Ramen):
    def prepare(self):
        return f"Blending spicy sauces for flavorful {self.name}"
    
    def serve(self):
        return f"Serving the spicy Ramen! Here it is: {self.name}"
    
ramen_types = [TonkotsuRamen("Tonkotsu"), ShoyuRamen("Shoyu"), SpicyRamen("Spicy")]

for ramen_type in ramen_types:
    print(ramen_type.prepare())

for ramen_type in ramen_types:
    print(ramen_type.serve())