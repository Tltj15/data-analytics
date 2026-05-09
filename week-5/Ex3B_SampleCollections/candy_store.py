#Start by creating two tuples: one that lists at least 3 types of candy that can come in
#fruit flavors, and another that lists at least 3 fruity flavors. (Feel free to get creative with
#your flavor ideas...)

candy = ('Sour patch kids','Starburst', 'Skittles', 'Jolly rancher')
flavors = ('Watermelon', 'Lemon', 'Orange', 'Cherry')

#Now create a new variable to store candy combinations as a set. Using the index of
#each tuple, add at least one combination of each candy and flavor to the new set 
new_candy = set()
new_candy.add(candy[0] + ' ' + flavors[0])
new_candy.add(candy[1] + ' ' + flavors[2])
new_candy.add(candy[3] + ' ' + flavors[1])
new_candy.add(candy[2] + ' ' + flavors[3])
print(new_candy)
# in tuple sets its output is not in the order you placed them but the combination is corrrect.
print('Today candy options include:', new_candy)
# the more i run the output it rearranges the order of candy



