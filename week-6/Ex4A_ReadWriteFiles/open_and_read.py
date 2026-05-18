f = open('about_me.txt', 'r', encoding='utf-8') # r measn open in read mode
#had issues running at first with unicodedecodeerror
# after asking ai why it couldnt run it had to add the encoding to the end of my open()
#print(f.read(50)) # will show in terminal
# added the 50 to the .read
#with the first 50 it only printed first 50 characters
#print(f.read(50))

#print(f.readline(100)) # 10 only gave  characters
#1 gave returned the whole line of a
#1 return from a-c with answer
# depending on the number it will return the amount a charhacters to print 
fifty = f.read(50) #.read(50) one variable
#print(f.readline())
return_line = []
for i in range (4): # output of a loop 
    #ran the loop 2times
    # changed to 4 time loop
    line = f.readline()
    if line:
        return_line.append(line) #append line to list
    
remain_lines = f.readlines(100)
f.close()
    #print(f.readline())
# when ran the name came out chopy, and only from a - c answer 

print(f'First 50 characters: {fifty}') #prints the 50characters

#print(f'Loop capture line: {return_line}')
#print(f'Readlines(100) remaining: {remain_lines}')

print(f'Next four lines as list by line: {return_line}')

print(f'Next 100 characters, rounded to complete line: {remain_lines}')
#print the all the questions and answers
#starts with first 50 characters a) name
# next four line starts with [general]
#next 100 characters adds the updated question [e]