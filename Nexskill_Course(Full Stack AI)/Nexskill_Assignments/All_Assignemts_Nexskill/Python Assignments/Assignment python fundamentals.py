# Part 1: Input & Output Functions (print & input)


# Question no 1
"""1. Write a program to print "Hello, World!" and your name on two separate lines."""

print("Hello World")
print("Hussnain Saifi")



# Question no 2
"""2. Ask the user for their favorite color using input() and print
"Your favorite color is [color]"."""

Color = input("Please Enter your Favorite color: ")
print(Color)



# Question no 3
"""3. Use a single print() statement to display three different words separated by a hyphen (-)."""

print("Muhammad","Hussnain","Saifi", sep="-")



# Question no 4
"""4. Prompt the user for their birth year and print their age"""

a = int(input("Enter your birth year: "))
b = 2026 - a
print(b)



# Question no 5
"""5. Print the result of 5 + 5 such that the output is:
The sum of 5 and 5 is 10."""

sum = 5 + 5
print("The sum of 5 + 5 = ", sum)



# Question no 6
"""6. Use the end parameter in print() to join two separate print statements with a space."""

print("I am a programmer." ,end =" ")
print("I am learning python")



# Question no 7
"""7. Write a program that takes two strings from the user and prints them joined together."""

s1 = input("Please enter your string 1: ")
s2 = input("Please enter your string 2: ")
print("Your strings are joined: ", s1 + s2)



# Question no 8
"""8. Create a greeting that takes a user's name and prints
"Welcome, [Name]!" in all uppercase."""

Greeting = input("Please enter your name: ")
print("welcome ",Greeting.upper())



# Question no 9
"""9. Ask for a user's city and country, then print them in the format:
"City, Country"""

city = input("Please enter your city: ")
country = input("Please enter your country: ")
print("Your city is:",city , "and Your country is:", country)
 


# Question no 10
"""10. Experiment: What happens if you try to add a string and an integer in a print statement?
Write a code snippet that fixes this using str()."""

ex = str(input("hussnain""1234"))
print(ex)




# Part 2: Variables & Data Types

# Question no 11
"""11. Create an integer variable age and a float variable height. Print their types."""

age = int(78)
height = float(12.56)
print(type(age))
print(type(height))


# Question no 12
"""12. Store the value 3 + 4j in a variable. Print the variable and its type."""

val = 3 + 4j
print(type(val))


# Question no 13
"""13. Create a boolean variable is_python_fun and set it to True."""

is_python_fun = True
print(is_python_fun)
print(type(is_python_fun))


# Question no 14
"""14. Method 1: Assign three different values to three variables in a single line."""

color, movie, sport = "Blue", "Superman", "Hokey"
print(color,movie,sport)


#Question no 15
"""15. Method 2: Assign the same value to three different variables in a single line."""

movie = "Spiderman", "Ironman", "Batman"
print(movie)


# Question no 16
"""16. Take a numeric input from a user and convert it to a float."""

num = int(input("Please enter number: "))
print(float(num))
print(type(float(num)))



# Question no 17
"""17. Take a string input "100" and convert it to an int."""

user = str(input("Please enter your input: "))
print(int(user))
print(type(int(user)))



# Question no 18
"""18. Create a variable with a complex number and print only its real part."""

num = 1 + 2j
print(num.real)


# Question no 19
"""19. Define a string variable containing a paragraph and print its length."""

para = "my name is hussnian saifi. i am current learning full stack with ai course from nexskill"
print(len(para))


# Question no 20
"""20. Swap the values of two variables a and b without using a third variable."""

a=1
b=2
print("a = ", a, "b = ", b)
a, b = b, a
print("a = ", a, "b = ", b)



# Part 3: Arithmetic Operators 

# Question no 21
"""21. Write a program to calculate the area of a rectangle (Length × Width). """

length = 4
width = 6
area = length * width
print(f"Area of rectangle is {area}")



# Question no 22

"""22. Take two numbers and print the result of the first raised to the power of the second (a^b). """

z = 6
x = 8
Power = z ** x
print(f"Power of two number {z} ** {x} = {Power}")




# Question no 23

"""23. Demonstrate the difference between / (division) and // (floor division) with the numbers 10 
and 3. """


num1 = 10
num2 = 3
division = 10 / 3
floor_division = 10 // 3
print(f"Division of 10 and 3 is {division} and Floor division is {floor_division}")




# Question no 24

"""24. Use the modulus operator % to find the remainder when 25 is divided by 4."""

h = 25
l = 4
module = 25 % 4
print(f"{h} % {l} is {module}")




# Question no 25

"""25. Calculate the average of five numbers entered by the user. """

a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
c = int(input("Enter your 3rd number: "))
d = int(input("Enter your 4th number: "))
e = int(input("Enter your 5th number: "))
average = (a + b + c + d  + e) / 5
print(f"user 5 number average is {average}")





# Question no 26

"""26. Create a program that converts minutes into hours and remaining minutes."""

minutes = 200
hours = minutes // 60
remaning_minutes = minutes % 60
print(f"minutes {minutes} coverted into hours {hours}  and remaining minutes are {remaning_minutes}")




# Question no 27

"""27. Calculate the area of a circle where Area = \pi r^2 (Use 3.14 for \pi). """

pi = 3.14
radius = 6
area_of_circle = pi * radius ** 2
print(f"Area of a circle is {area_of_circle} when pi is {pi} and radius is {radius}")




# Question no 28

"""28. Find the cube of a number entered by the user. """

number = int(input("Please enter your number for cube: "))
cube = number ** 3
print(f"Your number is {number} and its cube is {cube}")





# Question no 29

"""29. Perform the calculation 10 + 5 * 2. Does Python follow PEMDAS? Prove it with code. """

cal = 10 + 5 * 2
print(cal)
print("Python follow the PEDMAS rule...")





# Question no 30

"""30. Write a program to calculate simple interest: (P \times R \times T) / 100. """

P = float(input("Please enter the investment amount: "))
R = float(input("Please enter the interest % you want on amount: "))
T = float(input("Please enter the time period, enter in years: "))
Si = (P * R * T) / 100
print(f"Principle you invest {P} Interest on it {R}% and Time period is {T} The simple interest you gain is {Si}")





# Part 4: Comparison & Logical Operators

# Question no 31
"""31. Compare two numbers entered by the user and print if the first is greater than the 
second. """

a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
print(a>b)





# Question no 32
"""32. Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result."""

c = int(input("Pleae enter the number to check its even or not: "))
evn = c % 2 == 0 
print(evn)




# Question no 33
"""33. Write a program that checks if a number is between 10 and 50 (inclusive) using and."""

d = int(input("Please enter your number to check its btwn 10 to 50: "))
print(d >= 10 and d <= 50)




# Question no 34
"""34. Check if a string entered by the user is equal to "Python"."""

e = str(input("Please enter your string: "))
print(e == "Python" or e == "python")





# Question no 35
"""35. Use the or operator to check if a user is either "Admin" or "Superuser"."""

f = input("Please enter your role: ")
print(f == "Admin" or f == "Superuser" or f == "admin" or f == "superuser")




# Question no 36
"""36. Demonstrate the not operator by reversing a Boolean variable."""

g = 1 > 2
print("1 > 2 =",g)
print(not g,":due to the not logic")




# Question no 37
"""37. Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result. """

k = 0.1 + 0.2 == 0.3
print(k,"Reason is because python do not store floating precision value")




# Question no 38
"""38. Take a user's age and check if they are NOT under 18. """

l = int(input("Please enter your age to see you are under 18 or not: "))
print(l <= 17)





# Question no 39
"""39. Check if a number is positive and odd using logical operators. """

z = int(input("Please enter your number to check its positive and odd or not: "))
print(z >= 0 and z % 2 != 0)





# Question no 40
"""40. Compare the lengths of two strings provided by the user. """

v = str(input("Please enter your 1st string: "))
m = str(input("Please enter your 2nd string: "))
print(len(v) == len(m))





# Part 5: Assignment Operators with Arithmetic 

# Question 41 
"""41. Initialize a variable x = 10. Use += to add 5 to it. """

x = 10
x += 5
print(x)





# Question 42 
"""42. Use -= to subtract 3 from a variable price. """

y = 4
y -= 3
print(y)



# Question 43 
"""43. Multiply a variable balance by 2 using the *= operator. """

z = 5
z *= 2
print(z)




# Question 44 
"""44. Divide a variable total by 4 using the /= operator. """

a = 40
a /= 4
print(a)





# Question 45 
"""45. Use **= to square a variable. """

b = 10
b **= 2
print(b)






# Question 46 
"""46. Create a counter variable and increment it by 1 using assignment operators. """

count = 1
count += 1
print(count)





# Question 47 
"""47. Use %= to find the remainder of a variable divided by 2 and update the variable. """

c = 5
c %= 2
print(c)




# Question 48 
"""48. Use //= to perform floor division on a variable and update it. """

f = 45
f //= 5
print(f)




# Question 49 
"""49. Start with n = 2. In three lines of code using assignment operators, turn it into 20."""

n = 2
n += 3
n *= 4
print(n)




# Question 50 
"""50. Ask the user for a number, then use += to add 10 to it and print the final result."""

u = int(input("Please enter your number: "))
u += 10
print("Result is", u)

