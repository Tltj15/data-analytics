#Create a list with the titles of your favorite movies (or movies you’d like to watch) –
#include at least 2, but no more than 10.
movies = ['The Drama', 'Lalaland', 'Harry Poter', 'Twilight', 'Birdbox']
print('The list movies includes my top', len(movies), 'favorite movies.')
print(movies)

#a) Use the sorted() function to print a sorted list, then print the list again without
#using sorted()
print(sorted(movies))
print(movies)
# the sort fucntion alphabetized the movies

#b)sorted() differnt way
movies.sort()
print(movies)

# .append one more movie and fixing the description statement
movies.append('Straw')
print(movies)
print('The list movies includes my top', len(movies), 'favorite movies.')
