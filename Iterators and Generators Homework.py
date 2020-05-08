# Problem 1

# Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):
    for num in range(0, N): #Another way is range(N)
        yield num**2

for x in gensquares(10):
    print(x)


#Example
#for x in gensquares(10):
#    print(x)

#0
#1
#4
#9
#16
#25
#36
#49
#64
#81


print("----------------------------------------------------------------------------------------------")


#Problem 2

#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
#Note: Use the random library. For example:

import random

#random.randint(1,10)
#9


def rand_num(low,high,n):
    for i in range(0, n): #Same here range(n)
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)




#for num in rand_num(1,10,12):
#    print(num)

#6
#1
#10
#5
#8
#2
#8
#5
#4
#5
#1
#4


print("----------------------------------------------------------------------------------------------")


#Problem 3

#Use the iter() function to convert the string below into an iterator:

s = 'hello'

iter_s = iter(s)

def iter_str(iter_s):
    for x in iter_s:
        yield x

print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))


"""
s = iter(s)  Easy way to do the same

print(next(s))

"""


print("----------------------------------------------------------------------------------------------")


#Problem 4

#Explain a use case for a generator using a yield statement where you would not want to use a normal 
# function with a return statement.

"""If the output has the potential of taking up a large amount of memory and you only intend to 
iterate through it, you would want to use a generator"""


print("----------------------------------------------------------------------------------------------")


#Extra Credit!

#Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will 
# have to do some Googling/Stack Overflowing!)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3) #This is a generator, with this we don't need keep all in memory

for item in gencomp:
    print(item)

4
5

#Hint: Google generator comprehension!
#Great Job!"""