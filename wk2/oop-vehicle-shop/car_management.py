class CarManager:
    all_cars = {}
    total_cars = 0
    id_counter = 1

    def __init__(self, make='', model='', year=None, mileage=None, service=None):
        self._make = make.lower()
        self._model = model.lower()
        self._year = year
        self._mileage = mileage
        self._service = service if service else []
        self._id = CarManager.id_counter

        CarManager.all_cars[self.id] = self
        CarManager.total_cars += 1
        CarManager.id_counter += 1


    @classmethod
    def welcome_customer(cls):
        print (f"--- WELCOME ---")
        print (f"1. Add a car")
        print (f"2. View all cars")
        print (f"3. View total number of cars")
        print (f"4. See a car's details")
        print (f"5. Service a car")
        print (f"6. Update mileage")
        print (f"7. Quit")

        user_input = int(input("Enter a number: "))

        if user_input == 1:
            cls.prompt_user_to_add_car()
        elif user_input == 2:
            for car in cls.all_cars.values():
                print(car)
        elif user_input == 3:
            print(f"There are {CarManager.total_cars} total cars.")
        elif user_input == 4:
            cls.specific_car_id()
        elif user_input == 5:
            car_id = int(input("Enter the car ID for service: "))
            if car_id in cls.all_cars:
                service_type = input("What's the new service to add? ")
                cls.all_cars[car_id].add_service(service_type)
            else:
                print("Car not found.")
        elif user_input == 6:
            cls.update_mileage()
        elif user_input == 7:
            print("Have a wonderful day!")
            # exit()
        else:
            print("Invalid option. Please try again.")
            cls.welcome_customer()

    @classmethod
    def specific_car_id(cls):
        car_id = int(input("Sure! What's the car ID?"))
        if car_id in cls.all_cars:
            print(cls.all_cars[car_id])
        else:
            print("Car not found.")

    @classmethod
    def prompt_user_to_add_car(cls):
        print('Enter info for car to add below!')
        make = input('Make?')
        model = input('Model?')
        year = int(input('Year?'))
        mileage = int(input('Mileage?'))
        service_item = input("Most recent service?")

        cls(make=make, model=model, year=year, mileage=mileage, service=[service_item])

    @classmethod
    def update_mileage(cls):
        car_id = int(input("Enter car ID to update mileage: "))
        if car_id in cls.all_cars:
            new_mileage = int(input("Enter new mileage: "))
            cls.all_cars[car_id]._mileage = new_mileage
            print(f"Mileage updated for car ID {car_id}.")
        else:
            print("Car not found.")


    @property
    def id(self):
        return self._id

    @property
    def make(self):
        return self._make.capitalize()

    @property
    def model(self):
        return self._model.capitalize()

    @property
    def year(self):
        return self._year

    @property
    def mileage(self):
        return self._mileage

    @property
    def service(self):
        return self._service

    def add_service(self, service_type):
        self._service.append(service_type)
        print(f'Service "{service_type}" added. Current services: {service_type}')

    def __repr__(self):
        return f'ID: {self.id} | {self.make} | {self.model} | {self.year} | {self.mileage} | {self.service}'

