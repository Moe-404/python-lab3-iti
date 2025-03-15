class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __repr__(self):
        return f"Engine(fuel_type={self.fuel_type}, horsepower={self.horsepower})"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, engine={self.engine})"

engine = Engine(fuel_type="petrol", horsepower=150)

car = Car(make="Toyota", model="Corolla", engine=engine)

print(car)
# Output: Car(make=Toyota, model=Corolla, engine=Engine(fuel_type=petrol, horsepower=150))