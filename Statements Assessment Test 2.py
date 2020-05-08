# 1) Use for, .split(), and if to create a Statement that will print out words that start with 's'.

st = 'Print only the words that start with s in this sentence'

sp_st = st.split()

for x in sp_st:
    if x[0] == "s" or x[0] == "S":
        print (x)


print("------------------------------------------------------------------------------------------------")

# 2) Use range() to print all the even numbers from 0 to 10.

for x in range(0,11):
    if x%2 == 0:
        print (x)


print("------------------------------------------------------------------------------------------------")

# 3) Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

my_list = [x for x in range(1,51) if x%3==0]

print(my_list)


print("------------------------------------------------------------------------------------------------")

# 4) Go through the string below and if the length of a word is even print "even!".

st = 'Print every word in this sentence that has an even number of letters'

#x = [word for word in st.split() if len(word)%2==0]
#print (x)

for word in st.split():
    if len(word)%2 == 0:
        print(f"The word {word} is even!")


print("------------------------------------------------------------------------------------------------")

# 5) Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz".

for num in range(1,101):
    if (num%3 == 0 and num%5 == 0):
        print(f"FizzBuzz + {num}")
    elif (num%5 == 0):
        print(f"Buzz + {num}")
    elif (num%3 == 0):
        print(f"Fizz + {num}")


print("------------------------------------------------------------------------------------------------")

# 6) Use List Comprehension to create a list of the first letters of every word in the string below.

st = 'Create a list of the first letters of every word in this string'

my_list = [word[0] for word in st.split()]

print(my_list)