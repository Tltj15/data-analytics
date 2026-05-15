import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#Use a combination of functions from all three modules to create calculations

#_Experimenting with a subset of integers 1-100:
#Sum of 75 sample values from 1 to 100: ____
#Average of 75 sample values: ____
#Median of 75 sample values: ____
def cal_stats():
    vals_1_100 = range(1,101) # 1-101 to inclcude the 100 othereise its 99
    vals_sample = random.sample(vals_1_100, k=75) #.sample k cannot be bigger then 100, 75sample numbers
    total_sum = math.fsum(vals_sample) #use math.fsum() for sum of all numbers
    average = statistics.mean(vals_sample) #use statistics.mean() for the mean
    median = statistics.median(vals_sample) #use statistics.median() for the median value

    print('_Experimenting with a subset of integers 1-100:')
    print(f'Sum of 75 sample values from 1 to 100: {total_sum}')
    print(f'Average of 75 sample values: {average:.2f}')
    print(f'Median of 75 sample values: {median}' '\n')
cal_stats()



#_Experimenting with a superset of 200 values, integers 1-100:
#Average of 200 values: ____
#Median of 200 values: ____
#Mode of 200 values: ____
#Standard deviation of 200 values: ____
#Variance of 200 values: ____
def cal_stats():
    vals_1_100 = range(1,101)
    vals_choices = random.choices(vals_1_100, k = 200) #.choice allows repeitition so k200 will not be affected
    average = statistics.mean(vals_choices)
    median = statistics.median(vals_choices)
    mode = statistics.mode(vals_choices) #use statistics.mode() for mode of data set
    stan_dev = statistics.stdev(vals_choices) #use statistics.stdev() standard deviation of data
    variance = statistics.variance(vals_choices) #use statistics.variance() variance of data

    print('_Experimenting with a superset of 200 values, integers 1-100:')
    print(f'Avergae of 200 value: {average}')
    print(f'Median of 200 values: {median}')
    print(f'Mode of 200 values: {mode}')
    print(f'Standard deviation of 200 vlaues: {stan_dev:.2f}')
    print(f'Variance of 200 values: {variance:.2f}' '\n')
cal_stats()



#_Modeling a random circle:
#Radius = __, area = ____ (rounded up to the nearest integer)
#Radius = __, area = ____ (rounded down to the nearest integer)

def math_calc():
    radius = random.randint(3,10)
    pi = math.pi
    area = pi*(radius **2)
    up = math.ceil(area) #use math.ceil() to round up closest integer
    down = math.floor(area) #use math.floor() to round down closest integer

    print('_Modeling  random circle:')
    print(f'Radius= {radius}, area= {up} (rounded up to the nearest integer)')
    print(f'Radius= {radius}, area= {down} (rounded down to the nearest integer)')
math_calc()