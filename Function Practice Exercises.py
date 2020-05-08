#Problems are arranged in increasing difficulty:

#    Warmup - these can be solved using basic comparisons and methods
#    Level 1 - these may involve if/then conditional statements and simple methods
#    Level 2 - these may require iterating over sequences, usually with some kind of loop
#    Challenging - these will take some creativity to solve

#WARMUP SECTION:
#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if (a%2==0 and b%2==0):
        if (a>b):
            return b
        elif (a<b):
            return a
        else:
            return a
    elif (a%2!=0 or b%2!=0):
        if (a>b):
            return a
        elif (a<b):
            return b
        else:
            return a

# Check
print(lesser_of_two_evens(2,4))

# Check
print(lesser_of_two_evens(2,5))


print("-------------------------------------------------------------------------------------------------")


#ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with 
#the same letter

#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False


def animal_crackers(text):
    tw = [word[0] for word in text.split()]
    if (tw[0].lower() == tw[1].lower()):
        return True
    else:
        return False
        

# Check
print(animal_crackers('Levelheaded Llama'))


# Check
print(animal_crackers('Crazy Kangaroo'))


print("-------------------------------------------------------------------------------------------------")


#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False


def makes_twenty(n1,n2):
    if (n1+n2 == 20 or n1==20 or n2==20):
        return True
    else:
        return False


# Check
print(makes_twenty(20,10))


# Check
print(makes_twenty(2,3))


print("-------------------------------------------------------------------------------------------------")


#LEVEL 1 PROBLEMS
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

#old_macdonald('macdonald') --> MacDonald

#Note: 'macdonald'.capitalize() returns 'Macdonald'


def old_macdonald(name):
    return name[0:3].capitalize()+name[3:].capitalize()


# Check
print(old_macdonald('macdonald'))


print("-------------------------------------------------------------------------------------------------")


#MASTER YODA: Given a sentence, return a sentence with the words reversed

#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

#Note: The .join() method may be useful here. The .join() method allows you to join together strings 
# in a list with some connector string. For example, some uses of the .join() method:

#>>> "--".join(['a','b','c'])
#>>> 'a--b--c'

#This means if you had a list of words you wanted to turn back into a sentence, you could just join 
# them with a single space string:

#>>> " ".join(['Hello','world'])
#>>> "Hello world"


def master_yoda(text):
    sp = text.split()
    inv = " ".join(sp[::-1])
    return inv
    

# Check
print(master_yoda('I am home'))


# Check
print(master_yoda('We are ready'))


print("-------------------------------------------------------------------------------------------------")


#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

#NOTA: abs(num) returns the absolute value of a number


def almost_there(n):
    return ((abs(100-n)<=10) or (abs(200-n)<=10))


# Check
print(almost_there(90))


# Check
print(almost_there(104))


# Check
print(almost_there(150))


# Check
print(almost_there(209))


print("-------------------------------------------------------------------------------------------------")


#LEVEL 2 PROBLEMS
#FIND 33:

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False


def has_33(nums):
    for i in range(0, len(nums)-1):
        if (nums[i]==3 and nums[i+1]==3):
            return True
    return False

        
# Check
print(has_33([1, 3, 3]))


# Check
print(has_33([1, 3, 1, 3]))


# Check
print(has_33([3, 1, 3]))


print("-------------------------------------------------------------------------------------------------")


#PAPER DOLL: Given a string, return a string where for every character in the original there are 
# three characters

#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    sp = [word*3 for word in text]
    return "".join(sp)


# Check
print(paper_doll('Hello'))


# Check
print(paper_doll('Mississippi'))


print("-------------------------------------------------------------------------------------------------")


#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return 
# their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
# if the sum (even after adjustment) exceeds 21, return 'BUST'

#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19


def blackjack(a,b,c):
    if (a+b+c <= 21):  #otra forma colocar sum((a,b,c))
        return a+b+c
    elif (a+b+c>=21 and (a==11 or b==11 or c==11)): #otra forma 11 in (a,b,c)
        return a+b+c-10
    else:
        return "BUST"


# Check
print(blackjack(5,6,7))


# Check
print(blackjack(9,9,9))


# Check
print(blackjack(9,9,11))


print("-------------------------------------------------------------------------------------------------")


#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.

#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14

"""
NO ME SALIO, BUSQUE LA SOLUCION
def summer_69(arr):
    suma = 0
    for i in range(0, len(arr)):
        if (arr[i]!=6):
            suma = arr[i] + suma
        else:
            while arr[i]!=9:
                i +=1
    return suma
"""
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

# Check
print(summer_69([1, 3, 5]))


# Check
print(summer_69([4, 5, 6, 7, 8, 9]))


# Check
print(summer_69([2, 1, 6, 9, 11]))


print("-------------------------------------------------------------------------------------------------")


#CHALLENGING PROBLEMS
#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

"""
DE ESTA FORMA SALE
def spy_game(nums):
    spy = False
    for i in range(0, len(nums)-1):
        if (nums[i]==0 and nums[i+1]==0 and nums[i+2]==7):
            spy = True
    return spy
""" 

"""
DE ESTA FORMA NO SALE
def spy_game(nums):
    spy = True
    cont = 0
    for num in nums:
        while spy:
            if num==0 and cont==0:
                cont +=1
                if cont==2:
                    spy=False
                break
            else:
                break
        while not spy:
            if num==7:
                cont +=1
                spy=True
                break
    if cont==3:
        return True
    else:
        return False
"""
#SOLUCIÓN DE LA PÁGINA
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1

# Check
print(spy_game([1,2,4,0,0,7,5]))


# Check
print(spy_game([1,0,2,4,0,5,7]))


# Check
print(spy_game([1,7,2,0,4,5,0]))


print("-------------------------------------------------------------------------------------------------")


#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and 
# including a given number

#count_primes(100) --> 25

#By convention, 0 and 1 are not prime.

# SOLUCIÓN DE LA PÁGINA
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# Check
count_primes(100)


print("-------------------------------------------------------------------------------------------------")


#Just for fun:
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

#print_big('a')

#out:   *  
#      * *
#     *****
#     *   *
#     *   *

#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 
# 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".

#SOLUCIÓN DE LA PÁGINA
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print_big('a')



#Great Job!