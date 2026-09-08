# Question 1: 
# Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
# (Celsius * 9/5) + 32) 

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)





# Question 2: 
# Calculate Area of a Rectangle 

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of Rectangle:", area)





# Question 3: 
# Calculate Compound Interest 
# Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time 

P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest (%): "))
T = float(input("Enter time in years: "))

CI = P * (1 + R/100)**T - P
print("Compound Interest:", CI)






# Question 4: 
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter. 

length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
print("Perimeter of Rectangle:", perimeter)








# Question 5: 
# Average of Three Numbers - Input three numbers and print their average. 
 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average:", average)




# Question 6: 
# Square and Cube of a Number - Ask the user for a number and display its square and cube. 

num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square:", square)
print("Cube:", cube)




# Question 7: 
# Distribute Items Equally - You have n candies and k students. 
# Write a program to find: 
# how many candies each student gets 
# how many are left

candies = int(input("Enter number of candies: "))
students = int(input("Enter number of students: "))
each_gets = candies // students
leftover = candies % students
print("Each student gets:", each_gets)
print("Candies left:", leftover)




# Question 8: 
# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss 

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > cost_price:
    print("Profit:", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss:", cost_price - selling_price)
else:
    print("No Profit No Loss")





# Question 9: 
# Total Marks and Percentage 
# Input marks of 5 subjects. Print: 
#  Total marks 
#  Percentage 
#  Average 

marks = []
for i in range(1,6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)





# Question 10: 
# Salary Calculator 
# Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA 

basic = float(input("Enter basic salary: "))
HRA = 0.2 * basic
DA = 0.15 * basic
total_salary = basic + HRA + DA
print("HRA:", HRA)
print("DA:", DA)
print("Total Salary:", total_salary)




# Question 11: 
# Age in Months and Days 
# Input your age in years. Calculate and print age in: 
#  Months 
#  Days (approximate)

age_years = int(input("Enter your age in years: "))
months = age_years * 12
days = age_years * 365 
print("Age in months:", months)
print("Age in days (approx):", days)





# Question 12: 
# Currency Converter (USD to PKR) 
# Input amount in USD. Convert using a fixed exchange rate. 

usd = float(input("Enter amount in USD: "))
exchange_rate = 279
pkr = usd * exchange_rate
print(f"{usd} USD = {pkr} PKR")




# Question 13: 
# Sum of First N Natural Numbers 
# Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2 

n = int(input("Enter n: "))
total = n * (n + 1) // 2
print("Sum of first", n, "natural numbers:", total)






# Question 14: 
# Percentage of Correct Answers 
# Input total questions and correct answers, and calculate the percentage score.

total_questions = int(input("Enter total questions: "))
correct_answers = int(input("Enter correct answers: "))
percentage = (correct_answers / total_questions) * 100
print("Percentage score:", percentage, "%")





# Question 15: 
# Speed, Distance, and Time 
# Input distance and time, and calculate speed. 

distance = float(input("Enter distance (km): "))
time = float(input("Enter time (hours): "))
speed = distance / time
print("Speed:", speed, "km/h")




# Question 16: 
# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2) 

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
BMI = weight / (height ** 2)
print("BMI:", BMI)




# Question 17: 
# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes

minutes = int(input("Enter total minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes = {hours} hours {remaining_minutes} minutes")



