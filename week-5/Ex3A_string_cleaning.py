# A colleague has shared the following contact records, but the data is a mess, with
#inconsistent capitalization and currency symbols that need to be cleaned up before it
#can be used:
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print(name_1.title())
print(name_2.title())
print(name_3.title())

print(salary_1.replace('$', ''))
salary_1 = salary_1.replace('$', '')
salary_1 = salary_1.replace(',', '')
#salary_1 = int(salary_1)
print(salary_1)
print(type(salary_1))
print(int(salary_1))

salary_1 = int(salary_1.replace('$', '').replace(',', ''))
print(salary_1)
# needs to be converted to interger to be able to perform math.