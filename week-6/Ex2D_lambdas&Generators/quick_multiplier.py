doubler = lambda n : n * 2  #lambda is a small anonymous fucntion used with on expression
print(doubler(8))
print(doubler(-4))
print(doubler('banana')) # the output just doubles

tripler = lambda n : n * 3
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def discount_calc1(price, pct_off):
    return price * (1 - pct_off)
print(discount_calc1(10, .3))

def discount_calc2(pct_off):
    return lambda price: price * (1 - pct_off)
pct_off20 = discount_calc2(.2)
pct_off30 = discount_calc2(.3)
print(f'20% off: {pct_off20(10)}, 30% off:{pct_off30(10)}')

#If you want to create a similar multiplier variable for numbers 4 through 10, how can
#you save yourself some code by putting this lambda within a function?
def multiplier(n):
    return lambda x : x * n
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(multiplier(4)(15))
print(multiplier(5)(15))
print(multiplier(6)(15))
print(multiplier(7)(15))
print(multiplier(8)(15))
print(multiplier(9)(15))
print(multiplier(10)(15))


