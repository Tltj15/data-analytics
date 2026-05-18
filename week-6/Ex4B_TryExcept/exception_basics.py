try: 
    #apple = 1
    x = apple + 3

except NameError:
    print('NameError: You have not assigned a value to variable')
else:
    print(x)
finally:
    print("Let's try another one")
print()# adds a line of space inbetween the codeblock

try:
    x = int('pizza')
    #int(3)
    # integer is a whole number
    #'pizza' is a string
except ValueError:
    print('ValueError: Invalid integer value')
else:
    print(x)
finally:
    print("Let's try another one.")
print()

try:
    x = 'apple' + 3
    # 'apple' is a string
    # 3 is a integer
    # x = 'apple' + '3'
except TypeError:
    print('TypeError: Cannot add a string and integer together')
else:
    print(x)
finally:
    print("Let's try another one")
print()


try:
# have issues with this one have to use a eval()
    eval("greeting = 'Hello")
    #greeting = 'Hello, causes a synatx error, extra ' in 'hello
except SyntaxError:
    print('SyntaxError: Incorrect string literal')
else:
    print("Hello")
finally:
    print("Let's try another one.")
