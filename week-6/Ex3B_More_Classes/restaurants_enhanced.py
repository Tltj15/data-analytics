class Restaurant:
    '''restaurant name and the food they sell'''  #docstring description
    def __init__(self, rest_name, food_type): # self is a specific resturant
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = [] # store rating
#__init__ is a method
# had issues with the __init__ , i didnt know it needed two underscore on eachside
    def describe_rest (self): #methods inside class
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

    def add_num_served(self, amount): 
        self.number_served = self.number_served + amount
        
    def print_num_served(self): #prints the output
        print(f'{self.rest_name} has served {self.number_served} customers.')

    def customer_rating(self, rating): 
        if 1 <= rating <= 5:
            self.customer_ratings.append(rating)
            print(f'Your rating was {rating}.')
        else:
            print(f'Invalid rating. Please enter 1-5')

    def get_average_rating(self):
         if not self.customer_rating: #when there is no rating
              return 0
         return sum(self.customer_ratings) / len(self.customer_ratings)
            

baco = Restaurant('TACO BACO', 'mexican inspired food')
baco.describe_rest()
baco.rest_open()
#inputs for rating
served_today = int(input('How many customers served today?')) #accpts an input and adds that amount to self.num_served
baco.add_num_served(served_today) #input gets added here
baco.print_num_served()# print total
user_rating = float(input('How would you rate your experience (1-5) (5 being excellent): ')) #input rating accepts an input of num 1-5
#used int at first was giving issues when trying to add decimals
#used float to fix
baco.customer_rating(user_rating)

print(f'Average rating: {baco.get_average_rating():.1f}')



