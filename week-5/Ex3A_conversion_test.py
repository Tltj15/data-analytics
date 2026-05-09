#Description: This script tests various numeric conversion techniques
# Author: Sam Q. Newprogrammer
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

#a) Cast as integer using int()
# print(int(a)) doenst work its a decimal
print(int(b))
#print(int(c)) has text value error
#print(int(d)) has text value error

#b) Cast as float using float()
print(float(a))
print(float(b))
#print(float(c)) value error 
#print(float(d)) value error

#c) For variable a, try casting into a float then integer, like this: int(float(a))
print(int(float(a))) #removes the decimal leaves whole number
print(int(float(b))) #stays the same
#print(int(float(c))) value error
#print(int(float(d))) value error
 
#d) Use slicing to add just the numeric portion of the string to a new variable
#(remember, indexing always starts with 0!), and cast the number as an integer or
# string, whichever is appropriate
print(c[0:3])
#num_part = c[0:3]
num_part = int(c[0:3])
print(num_part)

print(d[7])
num = d[7:8]
print(num)


#e) For variables a and d, use the .strip() method to remove the leading/trailing
#spaces, within a print statement to display each result.

print(a.strip())
print(d.strip())