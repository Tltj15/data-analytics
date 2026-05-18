class Restaurant:
    '''restaurant name and the food they sell'''  #docstring description
    def __init__(self, rest_name, food_type): # self is a specific resturant
        self.rest_name = rest_name
        self.food_type = food_type
# had issues with the __init__ , i didnt know it needed two underscore on eachside
    def describe_rest (self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

donkin = Restaurant('Donkin Dunnts', 'coffee')
sbu = Restaurant('SBUBBY', 'hot or old sandwitches')
baco = Restaurant('TACO BACO', 'mexican inspired food')

donkin.describe_rest()
donkin.rest_open()

sbu.describe_rest()
sbu.rest_open()

baco.describe_rest()
baco.rest_open()