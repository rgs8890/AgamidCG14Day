class Drink:
    def __init__(self, name):
        self.name = name
    
    def prepare(self):
        return f"Making the {self.name}"
    
    def serve(self):
        return f"Serving the {self.name}"
    
class Ramune(Drink):
    def prepare(self):
        return f"Preparing the Ramune: {self.name}"
    
    def serve(self):
        return f"A nice ramune, {self.name} has been served."
    
class AsahiBeer(Drink):
    def prepare(self):
        return f"Preparing the Asahi: {self.name}"
    
    def serve(self):
        return f"A nice asahi, {self.name} has been served."
    
ramune = Ramune("Ramune Soda")
beer = AsahiBeer("Asahi")

drink_menu = [ramune, beer]

for drink in drink_menu:
    print(drink.serve())