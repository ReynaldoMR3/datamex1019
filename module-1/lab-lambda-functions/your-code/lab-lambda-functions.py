'''''
Challenge 1 - Passing a Lambda Expression to a Function
n the next excercise you will create a function that returns a lambda expression.
Create a function called modify_list. The function takes two arguments, a list and a lambda expression.
The function iterates through the list and applies the lambda expression to every element in the list.
Follow the steps as stated below:
    1. Define a list of any 10 numbers
    2. Define a simple lambda expression for eg that updates a number by 2
    3. Define an empty list
    4. Define the function -> use the lambda function to append the empty list
    5. Call the function with list and lambda expression
    6. print the updated list
    '''
l = [2, 34, 28, 94, 35, 10, 7, 80, 74, 20]
f = lambda x: x + 2
b = []


def modify_list(lst, fudduLambda):
    for x in l:
        b.append(f(x))


modify_list(l, 5)
print(b)
print("listo, siguiente ejercicio")
print(" ")

'''
Now we will define a lambda expression that will transform the elements of the list.
In the cell below, create a lambda expression that converts Celsius to Kelvin. Recall that 0°C + 273.15 = 273.15K
'''
convert_c = lambda x: x + 273.15

# Finally, convert the list of temperatures below from Celsius to Kelvin.
temps = [12, 23, 38, -55, 24]

sol = [convert_c(x) for x in temps]
print(sol)
print("listo, siguiente ejercicio")
print(" ")

'''
In this part, we will define a function that returns a lambda expression
In the cell below, write a lambda expression that takes two numbers and returns 1 if one is divisible by the other and zero otherwise.
Call the lambda expression mod.
'''

returns_div = lambda x, b: 1 if ((x / b) or (b / x)) else 0

print(returns_div(15, 12))
print("listo, siguiente ejercicio")
print(" ")

'''
Now create a function that returns mod. The function only takes one argument - the first number in the mod lambda function.
Note: the lambda function above took two arguments, 
the lambda function in the return statement only takes one argument but also uses the argument passed to the function.
'''


def divisor(new):
    """
        input: a number
        output: a function that returns 1 if the number is divisible by another number (to be passed later) and zero otherwise
        """
    return lambda a: 1 if ((a / new) or (new / a)) else 0


# Finally, pass the number 5 to divisor. Now the function will check whether a number is divisble by 5.
# Assign this function to divisible5
divisible5 = divisor(5)

#Test your function with the following test cases: divisible5(10), divisible5(8)
print(divisible5(10))
print(divisible5(8))
print("listo, siguiente ejercicio")
print(" ")

'''
Challenge 2 - Using Lambda Expressions in List Comprehensions
In the following challenge, we will combine two lists using a lambda expression in a list comprehension.
To do this, we will need to introduce the zip function. The zip function returns an iterator of tuples.
The way zip function works with list has been shown below:

list1 = ['Green', 'cheese', 'English', 'tomato']
list2 = ['eggs', 'cheese', 'cucumber', 'tomato']
zipped = zip(list1,list2)
list(zipped)

[('Green', 'eggs'),
 ('cheese', 'cheese'),
 ('English', 'cucumber'),
 ('tomato', 'tomato')]
'''

#In this exercise we will try to compare the elements on the same index in the two lists.
# We want to zip the two lists and then use a lambda expression to compare if: list1 element > list2 element
list1 = [1,2,3,4]
list2 = [2,3,4,5]
zip_lists= zip(list1,list2) # Zip the lists together
print(list(zip_lists))# Print the zipped list
print("listo, siguiente ejercicio")
print(" ")
#Complete the parts of the code marked as "###"

'''

compare = lambda ###: print("True") if ### else print("False")
for ### in zip(list1,list2):
    compare(###)

'''
compare = lambda x: print("True") if (x > x) else print("False")
for x in zip(list1,list2):
    compare(x)
print("listo, siguiente ejercicio")
print(" ")

'''
Challenge 3 - Using Lambda Expressions as Arguments
In this challenge, we will zip together two lists and sort by the resulting tuple.
In the cell below, take the two lists provided, zip them together and sort by the first letter of the second element of each tuple. 
Do this using a lambda function.
'''

list3 = ['Engineering', 'Computer Science', 'Political Science', 'Mathematics']
list4 = ['Lab', 'Homework', 'Essay', 'Module']

new_zip_list = zip(list3,list4)
c3_list = list(new_zip_list)
print(c3_list) #Lista de zip de las listas
print(c3_list[0][1][0]) #Esta es la primer letra del segundo elemento de la tupla
c3_list.sort(key=lambda x: x[0][1][0]) #Sort de la primera letra del segundo elemento de cada tupla
print(c3_list)

print("listo, siguiente ejercicio")
print(" ")


''''
Bonus Challenge - Sort a Dictionary by Values
Given the dictionary below, sort it by values rather than by keys. Use a lambda function to specify the values as a sorting key.
'''
d = {'Honda': 1997, 'Toyota': 1995, 'Audi': 2001, 'BMW': 2005}
f={}
for i in d.keys():
    f[0]=d.get(i)

print(f)
print(sorted(f.items(), key= lambda v: v)) 
