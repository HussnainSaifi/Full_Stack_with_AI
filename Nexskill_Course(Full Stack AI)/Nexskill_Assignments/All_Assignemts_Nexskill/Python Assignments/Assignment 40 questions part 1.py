# Part A — Python Lists (10 Beginner Questions)

"""1. Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements. 
Tip: Use nums[0] and nums[-1]. """

nums = [3, 1, 4, 1, 5]
print(nums[0],nums[-1])




"""2. Find the length of the list colors = ['red', 'blue', 'green']. 
Tip: Use len(colors). """

colors = ['red', 'blue', 'green']
print(len(colors))





"""3. Append 'yellow' to the list colors = ['red', 'blue']. 
Tip: Use append(). """

colors = ['red', 'blue']
colors.append("yellow")
print(colors)





"""4. Insert 'orange' at index 1 in fruits = ['apple', 'banana']. 
Tip: Use insert(index, value)."""

fruits = ['apple', 'banana']
fruits.insert(1, "orange")
print(fruits)





"""5. Remove 'banana' from fruits = ['apple', 'banana', 'grapes']. 
Tip: Use remove(value). """

fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print(fruits)






"""6. Pop the last element from items = [10, 20, 30] and print the popped value. 
Tip: Call items.pop(). """

items = [10, 20, 30]
items.pop(-1)
print(items)





"""7. Check if 3 is in the list nums = [1, 2, 3, 4]. 
Tip: Use the in operator. """

nums = [1, 2, 3, 4]
n = 3 in nums
print(n)





"""8. Print the slice [2, 3] from the list [0, 1, 2, 3, 4]. 
Tip: Use slicing: a[2:4]. """

Lis = [0, 1, 2, 3, 4]
print(Lis[2:-1])





"""9. Replace the element at index 1 in a = [5, 10, 15] with 12. 
Tip: Use assignment: a[1] = 12. """

a = [5, 10, 15]
a[1] = 12
print(a)





"""10. Count how many times 2 appears in [1, 2, 2, 3, 2]. 
Tip: Use list.count(value). """

b = [1, 2, 2, 3, 2]
c = b.count(2)
print(c)







# Part B — Python Tuples (10 Beginner Questions)

"""1. Create a tuple t = (10, 20, 30) and print the second element. 
Tip: Tuples use indexing: t[1]. """

t = (10, 20, 30)
print(t[1])




"""2. Find the length of tuple ('a', 'b', 'c'). 
Tip: Use len(). """

y = ('a', 'b', 'c')
print(len(y))



"""3. Unpack the tuple (4, 5) into variables x and y. 
Tip: x, y = (4, 5). """

x,y = (4, 5,)
print(x,y)




"""4. Check if 'b' is in the tuple ('a', 'b', 'c'). 
Tip: Use 'b' in tuple. """

e = ('a', 'b', 'c')
d = 'b' in e
print(d)




"""5. Create an empty tuple and print its type. 
Tip: Empty tuple is (). """

r = ()
print(type(r))




"""6. Concatenate (1, 2) and (3, 4) into a new tuple. 
Tip: Use + operator. """

k = (1, 2)
o = (3, 4)
print(k + o)



"""7. Repeat (7,) three times. 
Tip: Use tuple * number. """

f = (7,)
print(f*3)




"""8. Find the index of 2 in (1, 2, 3, 2). 
Tip: Use index() method. """

r = (1, 2, 3, 2,)
print(r.index(2))





"""9. Count how many times 2 appears in (1, 2, 3, 2). 
Tip: Use count() method. """

u = (1, 2, 3, 2)
print(u.count(2))


"""10. Create a single element tuple containing the value 5. 
Tip: Remember to use a comma: (5,). """

i = (5,)
print(type(i))




# Part C — Python Sets (10 Beginner Questions) 

"""1. Create a set from [1, 2, 2, 3] and print it. 
Tip: Use set(list). """

s = set([1, 2, 2, 3])
print(type(s))





"""2. Add element 4 to the set {1, 2, 3}. 
Tip: Use add(). """

v = {1, 2, 3}
p = v.add(4)
print(p)





"""3. Remove element 2 from the set {1, 2, 3}. 
Tip: Use remove()."""

w = {1, 2, 3}
w.remove(2)
print(w)





"""4. Check if 5 is in the set {1, 3, 5}. 
Tip: Use in operator."""

a = {1, 3, 5}
s = 5 in s
print(s)




"""5. Find the length of set {10, 20, 30}. 
Tip: Use len(). """

g = {10, 20, 30}
print(len(g))





"""6. Clear all elements from the set {1, 2, 3}. 
Tip: Use clear(). """

z = {1, 2, 3}
z.clear()
print(z)





"""7. Create a set {'a', 'b'} and add 'c' only if its missing. 
Tip: Check membership first: if 'c' not in s:. """

t = {'a', 'b'}
d = 'c' not in t
print(d, "c is not in set")
t.add('c')
print(t)




"""8. Convert list ['a', 'a', 'b'] into a set to remove duplicates. 
Tip: Casting removes duplicates automatically. """

e = set(['a', 'a', 'b'])
print(type(e))
print(e)




"""9. Create two sets and print their union. 
Tip: Use set1 | set2. """

w = {1, 3, 5, 7}
r = {2, 4, 6}
s = w | r
print(s)





"""10. Create two sets and print their intersection. 
Tip: Use set1 & set2. """

w = {1, 3, 5, 7, 2, 4}
r = {2, 4, 6, 2, 3, 7}
s = w & r
print(s)





# Part D — Python Dictionaries (10 Beginner Questions) 

"""1. Create a dictionary {'name': 'Ali', 'age': 25} and print the name. 
Tip: Use d['name']. """

d = {'name': 'Ali', 'age': 25}
print(d['name'])




"""2. Add key 'city': 'Lahore' to a dictionary. 
Tip: Use assignment: d['city'] = 'Lahore'. """

d = {'name': 'Ali', 'age': 25}
d["city"] = "Lahore"
print(d)





"""3. Change 'age' in {'name': 'Ali', 'age': 25} to 30. 
Tip: Assign a new value: d['age'] = 30. """

d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print(d)



"""4. Delete key 'age' from a dictionary. 
Tip: Use del d['age']. """

d = {'name': 'Ali', 'age': 25}
del d['age']
print(d)




"""5. Check if key 'salary' exists in a dictionary. 
Tip: Use in operator. """

d = {'name': 'Ali', 'age': 25}
c = "salary" in d
print(c)





"""6. Print all keys from {'a': 1, 'b': 2}. 
Tip: Use d.keys(). """

k = {'a': 1, 'b': 2}
print(k.keys())





"""7. Print all values from a dictionary. 
Tip: Use d.values(). """

k = {'a': 1, 'b': 2}
d = k.values()
print(d)
c = 2 in d
print(c)



"""8. Iterate and print key_value pairs from {'x': 10, 'y': 20}. 
Tip: Use for k, v in d.items(). """

d = {'x': 10, 'y': 20}
for k, v in d.items():
    print(k, v)




"""9. Use get() to safely read key 'score' from an empty dictionary. 
Tip: Use d.get('score', default_value). """


d = {}
print(d.get("score", 0))



"""10. Create a dictionary from two lists: keys = ['a','b'], values = [1,2]. 
Tip: Use dict(zip(keys, values))."""

k = ['a','b']
v = [1,2]
print(dict(zip(k, v)))



