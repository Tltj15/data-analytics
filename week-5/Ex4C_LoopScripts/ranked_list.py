#Create a list of at least 5 items using anything you like: favorite foods, pets, cities you'd
#like to visit, skills you want to develop, etc.
#Use enumerate() with a for loop to print each item as a numbered list, starting at 1.
#Example: 1. tacos
#Now add an if statement inside your loop: if the index is 1 (i.e., the first item), also
#print " <- top pick!" on the same line.
foods = ['tacos', 'ramen', 'jerk chicken', 'pizza', 'pasta']
for index, item in enumerate(foods, start=1):
    if index == 1:
        print(index, item,'<-top pick!' )
    else:
        print(index, item)

# had to add start=1 if i dont it will just index per noraml with 0
#enumerate list the numbers vertically vs horizontal



