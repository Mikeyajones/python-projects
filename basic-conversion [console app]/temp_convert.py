# Temperature Conversion
# Author: Michael Jones
# Date: July 15, 2020

# Permissions:
# You are free to use and share this code for any purpose.

# Purpose:
# - Convert Fahrenheit to Celsius and Celsius to Fahrenheit.
# - Demonstrate how a While loop in Python functions.


#Convert Fahrenheit to Celsius
def f_to_c(num):
    return ((num - 32) * 5 / 9)

# Convert Celsius to Fahrenheit
def c_to_f(num):
    return ((num * 9/5) + 32)

# Declaring our variable run to make the while loop True
run = True

while run:
    # ------ MAIN MENU ------
    print('\n------ Temperature Conversion [Version 1.0] ------\n')
    print('Choose a conversion type: \n')
    print('1: Fahrenheit to Celsius')
    print('2: Celsius to Fahrenheit')
    print('3: Quit \n')

    # Ask the user to input an option
    choice = int(input('Select an option by inputting a number: '))

    # ------ Converting Fahrenheit to Celsius ------ 
    if choice == 1:
        print('\n------ Fahrenheit to Celsius Conversion ------ \n')
        fah = int(input('Enter the temperature in Fahrenheit you want to convert to Celsius: '))
        result = f_to_c(fah)
        print('\n------ Calculating the Results ------\n')
        print(fah, 'degrees Fahrenheit is', int(result), 'degrees Celsius. \n')
        
    # ------ Converting Celsius to Fahrenheit ------
    if choice == 2:
        print('\n------ Celsius to Fahrenheit Conversion ------ \n')
        cel = int(input('Enter the temperature in Celsius you want to convert to Fahrenheit: '))
        result = c_to_f(cel)
        print('\n------ Calculating the Results ------\n')
        print(cel, 'degrees Celsius is', int(result), 'degrees Fahrenheit. \n')

    # ------ QUIT ------
    if choice == 3:
        print('\nGoodbye.')
        break

    # Ask the user if they would like to do another conversion
    selection = input('Would you like to do another conversion? (y/n): ')
    if selection == 'y':
        run = True
    else:
        run = False
        print('\nGoodbye.')
