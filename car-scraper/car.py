class Car:
    def __init__(self, guid: str, brand: str, model: str, price: int, mileage: int, first_registration: int, vehicle_type: str, location: str, image: str, condition: str):
        self.guid = guid
        self.brand = brand
        self.model = model
        self.price = price
        self.mileage = mileage
        self.first_registration = first_registration
        self.vehicle_type = vehicle_type
        self.location = location
        self.image = image
        self.condition = condition

        #make sure brand starts with a capital letter
        self.brand = self.brand[0].upper() + self.brand[1:]
        #if model starts with a character, make sure it starts with a capital letter
        if self.model[0].isalpha():
            self.model = self.model[0].upper() + self.model[1:]
        

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Mileage: {self.mileage}, First Registration: {self.first_registration}, Vehicle Type: {self.vehicle_type}, Location: {self.location}"