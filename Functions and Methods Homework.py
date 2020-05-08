#Write a function that computes the volume of a sphere given its radius.

#The volume of a sphere is given as $$\frac{4}{3} πr^3$$

def vol(rad):
    return (4/3)*(3.1416)*(rad**3)


# Check
print(vol(2))

#33.49333333333333

print("-----------------------------------------------------------------------------------------------")


#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low, high):
        return f"{num} is in the range between {low} and {high}"
    else:
        return f"{num} is not in the range between {low} and {high}"


# Check
print(ran_check(5,2,7))

#5 is in the range between 2 and 7


#If you only wanted to return a boolean:

def ran_bool(num,low,high):
    return ((low<=num) and (num<=high))


#Check
print(ran_bool(3,1,10))


print("-----------------------------------------------------------------------------------------------")


#Write a Python function that accepts a string and calculates the number of upper case letters 
#and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33

#HINT: Two string methods that might prove useful: .isupper() and .islower()

#If you feel ambitious, explore the Collections module to solve this problem!

def up_low(s):
    #cont1=0
    #cont2=0
    d={"upper":0, "lower":0}
    for word in s:
        if word.isupper():
            #cont1 +=1
            d["upper"] +=1
        elif word.islower():
            d["lower"] +=1
            #cont2 +=1
    print(f"No. of Upper case characters: {cont1}")
    print(f"No. of Lower case characters: {cont2}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


print("-----------------------------------------------------------------------------------------------")


#Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    return list(set(lst))


print(f"Unique List: {unique_list([1,1,1,1,2,2,3,3,3,3,4,5])}")

#Out
#[1, 2, 3, 4, 5]


print("-----------------------------------------------------------------------------------------------")


#Write a Python function to multiply all the numbers in a list.

#Sample List : [1, 2, 3, -4]
#Expected Output : -24


def multiply(numbers):
    mult=1
    for num in numbers:
        mult *= num
    return mult


print(multiply([1,2,3,-4]))

#Out
#-24


print("-----------------------------------------------------------------------------------------------")


#Write a Python function that checks whether a passed in string is palindrome or not.

#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or 
#nurses run.

def palindrome(s):
    return (s[::]==s[::-1])


print(palindrome('helleh'))

#Out
#True


print("-----------------------------------------------------------------------------------------------")


#Hard:

#Write a Python function to check whether a string is pangram or not.

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

#Hint: Look at the string module

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str2=set(alphabet)
    return str2<=set(str1.lower())       


print(ispangram("The quick brown fox jumps over the lazy dog"))

#Out
#True

print(string.ascii_lowercase)

#Out
#'abcdefghijklmnopqrstuvwxyz'


#Great Job!