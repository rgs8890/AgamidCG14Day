class Tea:
    def __init__(self, name, steep_time, base_ingredient = "tea leaves"):
        self.name = name
        self.steep_time = steep_time
        self.base_ingredient = base_ingredient
    
    def prepare(self):
        return f"Boiling water and steeping {self.name} for {self.steep_time} minutes."
    
class GreenTea(Tea):
    def __init__(self, name, steep_time):
        super().__init__(name, steep_time, base_ingredient = "green tea leaves")
    
    def prepare(self):
        base_prepare = super().prepare()
        return base_prepare + f"Adding {self.base_ingredient}"

class ChaiTea(Tea):
    def __init__(self, name, steep_time):
        super().__init__(name, steep_time, base_ingredient = "tea leaves and spices")
    
    def prepare(self):
        base_prepare = super().prepare()
        return base_prepare + " Make chai tea before serving."

class HerbalTea(Tea):
    def __init__(self, name, steep_time):
        super().__init__(name, steep_time, base_ingredient = "herbal tea leaves")
    
    def prepare(self):
        base_prepare = super().prepare()
        return base_prepare + " Make herbal tea before serving."

class MatchaTea(Tea):
    def __init__(self, name, steep_time):
        super().__init__(name, steep_time, base_ingredient = "matcha powder")
    
    def prepare(self):
        base_prepare = super().prepare()
        return base_prepare + f" Make matcha tea before serving with {self.base_ingredient}"

herbal = HerbalTea("Herbal Tea", "10")
chai = ChaiTea("Chai Tea", "15")
green = GreenTea("Green Leaves", "12")
matcha = MatchaTea("Matcha Leaves", "18")

teas = [herbal, chai, green, matcha]

for tea in teas:
    print(tea.prepare())
    print(tea.base_ingredient)

