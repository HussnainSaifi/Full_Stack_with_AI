# Part A — Python Lists (10 Intermediate-Level Questions)

"""1. Create a list comprehension that returns the squares of only the even numbers 
from 0 to 20. 
Tip: Use an if condition inside the comprehension. """

square = [i**2 for i in range(21) if i % 2==0]
print(square)





"""2. Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original. 
Tip: Use sorted() instead of .sort(). """

nums = [3, 1, 4, 1, 5, 9]
print(sorted(nums))






"""3. Remove duplicates from a list while preserving the original order. 
Tip: Track seen values in a new list. """

nums = [3, 1, 4, 1, 5, 9, 3, 4]
unique = []
[unique.append(i) for i in nums if i not in unique]
print(unique)





"""4. Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension. 
Tip: Use a nested loop inside the comprehension. """

li = [[1, 2], [3, 4], [5]]
num = []
for i in li:
    for x in i:
        num.append(x)
print(num)





"""Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore 
case. 
Tip: Use key=str.lower. """

names = ['alice', 'Bob', 'charlie', 'DAVID']
print(sorted(names, key=str.lower))






"""6. Replace items from index 2 to 4 in a list with [100, 200] using slice assignment. 
Tip: Use a[2:5] = [...]. """

li = [300, 400, 500, 700, 800, 900]
li[2:5] = [100, 200, 1000]
print(li)






"""7. Write a program to find all indices of a value in a list (e.g., all indices of 7). 
Tip: Use enumerate. """

numbers = [1, 7, 2, 7, 3, 7, 4]
target = 7
num = []
for i, val in enumerate(numbers):
    if val==target:
        num.append(i)
print(num)






"""8. Create a new list containing only elements that appear exactly once in the original 
list. 
Tip: Use list.count() inside a comprehension. """

numbers = [1, 2, 2, 3, 4, 3, 5]
num = [i for i in numbers if numbers.count(i)==1]
print(num)



"""9. Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]). 
Tip: Use slicing: lst[-1:] + lst[:-1]. """

n = [1,2,3,4]
print(n[-1:] + n[:-1])






"""10. Split a list into two lists: one with even numbers, one with odd numbers. 
Tip: Create two comprehensions"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 6, 17, 18, 19, 20, 21]  
even = [i for i in num if i % 2 == 0]
print("Even",even)
odd = [i for i in num if i % 2 != 0]
print("Odd",odd)





# Part B — Python Tuples (10 Intermediate-Level Questions) 

"""1. Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables. 
Tip: Use tuple() and simple unpacking. """

t = tuple([1, 2, 3, 4])
n1 , n2, n3, n4 = t       
print(n1)
print(n2)
print(n3)
print(n4)






"""2. Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements. 
Tip: Use a comprehension: x[1]. """

t = (('a', 1), ('b', 2), ('c', 3))
num = [i[1] for i in t]
print(num)








"""3. Write a function that returns multiple values (sum, min, max) using a tuple. 
Tip: Return (..., ..., ...) and unpack later. """

def multi(n):
    return sum(n), min(n), max(n)
t = (1, 2, 3, 4)
t1, t2, t3, t4 = multi(t)





"""4. Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list. 
Tip: Use + to join them. """

t1 = (1, 2, 3)
t2 = (4, 5)
print(list(t1+t2))




"""5. Given a tuple of numbers, find the element with the highest frequency. 
Tip: Loop through unique items using set(t). """

f = (1,2,3,4,6,6,1,3,4,3,2)
max_frequ = 0
result = None
for i in set(f):
    count = f.count(i)
    if count > max_frequ:
        max_frequ = count
        result = i
print(result)




"""6. Check if two tuples contain the same elements regardless of order. 
Tip: Compare sorted(tuple) values. """

q1 = (1,2,3)
q2 = (2,3,1)
if sorted(q1) == sorted(q2):
    print("Same Element yes")
else:
    print("not same")




"""7. Extract the last three items from a tuple using slicing. 
Tip: Use negative indexing: t[-3:]. """

s = (1,2,3,4,5,6,7,89,)
print(s[-3:])



"""8. Concatenate a tuple with itself three times (repeat operation). 
Tip: Use tuple * 3. """

e = (1,2,3,4)
print(e*3)




"""9. Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4). 
Tip: Use a comprehension inside tuple(). """

a = ((1,2),(3,4))
s = tuple([x for i in a for x in i])
print(s)




"""10. Store coordinates in tuples and calculate the Manhattan distance. 
Tip: Use absolute difference formula: abs(x1-x2) + abs(y1-y2). """

x = (5, 6)
y = (7, 2)
xy = abs(x[0] - y[0]) + abs(x[1] - y[1])
print(xy)


# Part C — Python Sets

"""1. Given two sets, find elements that are in the first set but not the second. 
Tip: Use the - operator. """

s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5}
s3 = s2 - s1
print(s3)




"""2. Find common items between three sets using intersection. 
Tip: Use set1 & set2 & set3. """

d1 = {1, 2, 3}
d2 = {1, 4, 5}
d3 = {1, 6, 7}
print(d1 & d2 & d3)





"""3. Given a sentence, return all unique words in lowercase. 
Tip: Split the string → lowercase → convert to set. """

line = "Learning python from youtube"
line.lower()
word = line.split()
print(set(word))





"""4. Convert a list with duplicates into a set, then back to a sorted list. 
Tip: Use sorted(set(list)). """

l = [1,2,3,4,5,1,2,3]
print(sorted(set(l)))





"""5. Check if one set is a strict subset of another. 
Tip: Use < operator. """

s1 = {1, 2}
s2 = {1, 2}

print(s1 < s2)




"""6. Use a set comprehension to collect all squares of numbers from 1 to 15 that are 
divisible by 3. 
Tip: Write {x*x for x in ... if x % 3 == 0}. """

w = {x*2 for x in range(1, 16) if x % 3 == 0}
print(w)




"""7. Count how many duplicate values exist in a list using sets. 
Tip: Compare lengths: len(list) - len(set(list)). """

c = [1,2,3,1]
q = len(c) - len(set(c))
print(q)




"""8. Write a program to remove all vowels from a string using a set. 
Tip: Use a vowel set and filter characters. """

v = set("AEIOUaeiou")
line = "Hello i am a programer"
re = "".join([i for i in line if i not in v])
print(re)





"""9. Find the symmetric difference between two sets. 
Tip: Use the ^ operator. """

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
sym = s1 ^ s2  
print(sym)





"""10. Check if two strings are anagrams using set comparison (unique characters only). 
Tip: Compare set(str1) with set(str2). """

st1 = "kings"
st2 = "kings"
if set(st1) == set(st2):
    print("leters are matching anagram")
else:
    print("Not an anagram")

# Part D — Python Dictionaries 

"""1. Count word frequencies in a sentence and store the results in a dictionary. 
Tip: Use d[word] = d.get(word, 0) + 1. """

sentence = "Hussnain loves python Hussnain loves coding"
words = sentence.split()
d = {}   
for word in words:
    d[word] = d.get(word, 0) + 1
print(d)





"""2. Invert a dictionary where all values are unique. 
Tip: Swap key and value in a loop. """

dic = {"a":1, "b":2, "c":3}
new_dic = {}
for keys, values in dic.items():
    new_dic[values]= keys
print(new_dic)





"""3. Merge two dictionaries where second dictionary overrides first. 
Tip: Use {**dict1, **dict2} or dict1 | dict2 (Python 3.9+). """

d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d3 = d1 | d2
print(d3)




"""4. Group words by their first letter into a dictionary of lists. 
Tip: Use setdefault. """

words = ["apple", "banana", "apricot", "blueberry", "cherry"]
dic = {}
for i in words:
    first = i[0]
    dic.setdefault(first, []).append(i)
print(dic)





"""5. Filter a dictionary to keep only entries with values greater than 50. 
Tip: Use a dictionary comprehension. """

d = {'a': 10, 'b': 60, 'c': 30, 'd': 80}
ftr = {k:v for k, v in d.items() if v > 50}
print(ftr)





"""6. Given a nested dictionary, safely access a deeply nested key. 
Tip: Chain .get() calls with default {}. """

data = {
    "student": {
        "detail": {
            "marks": 70
        }
    }
}
result = data.get("student", {}).get("detail", {}).get("marks", {})
print(result)




"""7. Write a dictionary comprehension that maps numbers 1 to 10 to their cubes. 
Tip: {x: x**3 for x in range(1,11)}. """

res = {x: x**3 for x in range(1, 11)}
print(res)




"""8. Find the key with the highest value in a dictionary. 
Tip: Use max(d, key=d.get). """

m = {'a': 10, 'b': 50, 'c': 30}
x = max(m, key= m.get)
print(x)




"""9. Combine two lists into a dictionary (keys from first list, values from second). 
Tip: Use zip(). """

keys = ['a', 'b', 'c']
values = [10, 20, 30]
l = dict(zip(keys, values))
print(l)




"""10. Remove all keys from a dictionary whose values are None. 
Tip: Check value before adding to new dict."""

d = {'a': 10, 'b': None, 'c': 30, 'd': None}
cleaned = {k: v for k, v in d.items() if v is not None}
print(cleaned)



