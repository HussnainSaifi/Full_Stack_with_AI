# STRING MANIPULATION


# 1. Create a new string made of first, middle, and last character

o = input("Enter string: ")
mi = len(o)//2
new = o[0] + o[mi] + o[-1]
print(new)




# 2. Count occurrences of all characters in a string

y = input("Enter string: ")
fr = {}
for i in y:
    fr[i] = fr.get(i, 0) + 1
print(fr)





# 3. Reverse a given string

r = input("Enter string: ")
re = r[::-1]
print(re)





# 4. Split a string on hyphens

v = input("Enter hyphens wali string: ")
sp = v.split('-')
print(sp)






# 5. Remove special symbols / punctuation from a string

import string
j = input("string please : ")
cs = ''.join([i for i in j if i.isalnum() or i.isspace()])
print(cs)





# LIST MANIPULATION


# 1. Reverse a list in Python

ls = [1,2,3,4,5]
rel = ls[::-1]
print(rel)





# 2. Turn every item of a list into its square

lt = [1,2,3,4,5]
sql= [x**2 for x in lt]
print(sql)






# 3. Remove empty strings from a list of strings

kl = ["Python", "", "Java", "", "C++"]
cl = [x for x in kl if x != ""]
print(cl)





# 4. Add new item to list after a specified item

lst = ["a","b","c","d"]
id = "x"
ad = "b"
index = lst.index(ad)+1
lst.insert(index, id)
print(lst)




# 5. Replace list’s item with new value if found

lst = ["a","b","c","d"]
old = "c"
new = "z"
if old in lst:
    i = lst.index(old)
    lst[i] = new
print("Replaced list:", lst)






# DICTIONARY MANIPULATION


# 1. Check if a value exists in a dictionary

d = {'a':10,'b':20,'c':30}
va= 20
ex = va in d.values()
print(ex)







# 2. Get the key of minimum value from dictionary

f = {'a':10,'b':5,'c':30}
minkey = min(d, key=d.get)
print(minkey)





# 3. Delete a list of keys from a dictionary

n = {'a':10,'b':20,'c':30,'d':40}
k = ['b','d']
for i in k:
    d.pop(k, None)
print(d)






# TUPLE MANIPULATION


# 1. Reverse a tuple

w = (1,2,3,4,5)
rt = w[::-1]
print(rt)





# 2. Access value 20 from the tuple

h = (10,20,30,40)
print(h[1])





# 3. Swap two tuples

j1 = (1,2,3)
j2 = (4,5,6)
j1, j2 = j2, j1
print(j1, j2)






# LOOP MANIPULATION


# 1. Print first 10 natural numbers using while

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()







# 2. Print even numbers till input number

n = int(input("Enter num: "))
for i in range(2, n+1, 2):
    print(i, end=" ")
print()






# 3. Print odd numbers till input number

a = int(input("Enter num: "))
for i in range(1, a+1, 2):
    print(i, end=" ")
print()





# 4. Print prime numbers till input number

n = int(input("Enter num: "))
for i in range(2, n+1):
    prime = True
    for i in range(2, int(i**0.5)+1):
        if i % i == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")
print()





# 5. Print multiplication table of a given number

nu = int(input("Enter num: "))
for i in range(1, 11):
    print(f"{nu} x {i} = {nu*i}")