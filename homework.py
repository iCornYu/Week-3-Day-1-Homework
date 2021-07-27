#Exercise 1:
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
print(list(filter(None, places))) #removes empty strings but keep blank strings

print(list(filter(lambda x: True if x and x.strip() else False, places ))) #removes both

#Exercise 2:
author = ["Shoha Tsuchida", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda x: x.lower().split()[-1])
print(author)

#Exercise 3:
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
print(list(map(lambda x: x[1]*(9/5) +32, places)))
#I could not figure out a way to print out the original list w/ tuple along with the modified values in a single line of code.

#Exercise 4:
def fib(num):
    if num <= 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    
fib(7)
# 7 = 21
# 6 = 13
# 5 = 8
# 4 = 5
# 3 = 3
# 2 = 2
# 1 = 1
#  