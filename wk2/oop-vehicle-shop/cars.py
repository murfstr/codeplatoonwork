from car_management import CarManager

ford = CarManager('ford', 'focus', 2000, 100000, ['oil change'])
# print(ford)
# ford.add_service('change tires')
# print(ford)
chevy = CarManager('chevy', 'silverado', 2000, 120000, ['speaker replacement'])
# print(chevy)
# CarManager.prompt_user_to_add_car()
# print(CarManager.all_cars)
CarManager.welcome_customer()
# print(CarManager.all_cars)