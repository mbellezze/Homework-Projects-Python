#Problem 1

#Handle the exception thrown by the code below by using try and except blocks.

#for i in ['a','b','c']:
#    print(i**2)

"""
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
"""


try:
    for i in ["a", "b", "c"]:
        print(i**2)
    
except TypeError:
    print("No se pueden elevar al cuadrado los caracteres")


print("---------------------------------------------------------------------------------------------")


#Problem 2

#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block 
# to print 'All Done.'

#x = 5
#y = 0

#z = x/y

"""
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y

ZeroDivisionError: division by zero
"""


x = 5
y= 0

try:
    z = x/y

except ZeroDivisionError:
    print("No es posible dividir por cero")

finally:
    print("All done")


print("---------------------------------------------------------------------------------------------")


#Problem 3

#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, 
# except, else block to account for incorrect inputs.

#def ask():
#    pass

#ask()

#Input an integer: null
#An error occurred! Please try again!
#Input an integer: 2
#Thank you, your number squared is:  4

def ask():

    while True:

        try:
            num = int(input("Ingrese un entero: "))
            print(f"Entero ingresado: {num}")
            squ = num**2

        except:
            print("Ocurrio un error! Por favor intente de nuevo!")
            continue
        
        else:
            print(f"Muchas gracias, el cuadrado es: {squ}")
            break


ask()










#Great Job!
