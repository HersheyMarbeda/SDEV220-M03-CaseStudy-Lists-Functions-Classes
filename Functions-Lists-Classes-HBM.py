# Programming Assingment: Case Study-Functions, Lists, and Classes
# Progammer: Hershey Marbeda
# Last Date Updated: 11.11.2024

# Super Class of Vehicle
class Vehicle:
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        self.vehicle_type = vehicle_type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
    # Function to display the vehicle information
    def display_inputs(self):
        print("\nYour Vehicle Information:")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof} \n")
        
# Sub Class of Vehicle    
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # inherit the attributes from Vehicle
        super().__init__(vehicle_type, year, make, model, doors, roof)
        
print("\nEnter the following information for your Vehicle:")
allowed_vehicle_types = ["Car", "Truck", "Plane", "Boat", "Broomstick"]
vehicle_type = input("Vehicle Type (Car, Truck, Plane, Boat, Broomstick): ").capitalize()
while vehicle_type not in allowed_vehicle_types:
    print("\nInvalid vehicle type. Please enter car, truck, plane, boat, or broomstick.")
    vehicle_type = input("Vehicle Type (car, truck, plane, boat, broomstick): ").capitalize()

year = input("Year: ")
if year.isdigit() == False:
    print("\nInvalid year. Please enter a number.")
    year = input("Year: ")
     
make = input("Make: ").capitalize()
model = input("Model: ").capitalize()

doors = input("Number of doors (2 or 4): ")
while doors != "2" and doors != "4":
    print("\nInvalid number of doors. Please enter 2 or 4.")
    doors = input("Number of doors (2 or 4): ")
    
roof = input("Type of roof (solid or sun roof): ").capitalize()
while roof != "Solid" and roof != "Sun roof":
    print("\nInvalid type of roof. Please enter Solid or Sun roof.")
    roof = input("Type of roof (solid or sun roof): ").capitalize()

        
# To call functions        
vehicle = Automobile(vehicle_type, year, make, model, doors, roof)
vehicle.display_inputs()

