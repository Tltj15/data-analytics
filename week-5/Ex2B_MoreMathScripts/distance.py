#4. How do you calculate the distance between coordinates (x1, y1) and (x2, y2)? Hint:
#You'll need to look up how to calculate a square root in Python, which may involve a
#function from the math module.

#d= sqrt((x₂ - x₁)² + (y₂ - y₁)²)
import math
# use math.sqrt for squareroot
#p is for point
p1 = (5, 9) #(x1,y1)
p2= (3,7) #(x2,y2)
distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print(f'Distance between coordinates: {format(distance, '.2f')}')
