class Car:
    def __init__(self,model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self, model):
        print(f"You are driving {self.color} {self.model}")