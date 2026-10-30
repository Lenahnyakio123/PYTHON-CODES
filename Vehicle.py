class Vehicle:

    def __init__(self, reg_number, model):
        self.reg_number = reg_number
        self.model = model


    def displayVehicle(self):
        print(f"Registration Number: {self.reg_number}")
        print(f"Model: {self.model}")

class Bus(Vehicle):

    def __init__(self, reg_number, model, passenger_capacity):
        super().__init__(reg_number, model)
        # iv. Passenger capacity attribute
        self.passenger_capacity = passenger_capacity


    def displayBus(self):
        print(f"Registration Number: {self.reg_number}")
        print(f"Model: {self.model}")
        print(f"Passenger Capacity: {self.passenger_capacity} passengers")

if __name__ == "__main__":
    bus1 = Bus("KDJ 851M", "SUZUKI KDJ", 40)
    

    bus1.displayBus()
    
    print("\n--- Using parent method + child attribute ---")
    bus1.displayVehicle()
    print(f"Passenger Capacity: {bus1.passenger_capacity}")
