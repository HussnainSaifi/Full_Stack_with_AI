# PART A 

import re
from collections import Counter
import math
import copy
from collections import namedtuple


# Q1 Count vowels and consonants
def q1(s):
    vowels = "aeiou"
    v = 0
    c = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

print("Q1:", q1("Hello World"))


# Q2 Title case
def q2(s):
    small = ["and", "of", "the", "in"]
    words = s.split()
    result = []

    for i in range(len(words)):
        w = words[i].lower()
        if i == 0 or i == len(words)-1 or w not in small:
            result.append(w.capitalize())
        else:
            result.append(w)

    return " ".join(result)

print("Q2:", q2("the lord of the rings"))


# Q3 Replace whole word
def q3(text, old, new):
    return re.sub(r'\b'+old+r'\b', new, text)

print("Q3:", q3("cat scatter cater", "cat", "dog"))


# Q4 String compression
def q4(s):
    result = ""
    count = 1

    for i in range(len(s)):
        if i < len(s)-1 and s[i] == s[i+1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    return result

print("Q4:", q4("aaabbc"))


# Q5 Balanced brackets
def q5(s):
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False
            last = stack.pop()
            if ch == ")" and last != "(":
                return False
            if ch == "]" and last != "[":
                return False
            if ch == "}" and last != "{":
                return False
    return len(stack) == 0

print("Q5:", q5("{[()]}"))


# Q6 Longest word
def q6(s):
    words = re.findall("[A-Za-z]+", s)
    max_len = 0

    for w in words:
        if len(w) > max_len:
            max_len = len(w)

    count = 0
    for w in words:
        if len(w) == max_len:
            count += 1

    return max_len, count

print("Q6:", q6("I love programming in python"))


# Q7 Anagram
def q7(a, b):
    a = "".join(ch.lower() for ch in a if ch.isalpha())
    b = "".join(ch.lower() for ch in b if ch.isalpha())
    return Counter(a) == Counter(b)

print("Q7:", q7("listen", "silent"))


# Q8 Extract emails
def q8(s):
    return re.findall(r'\S+@\S+\.\S+', s)

print("Q8:", q8("test@gmail.com abc@yahoo.com"))


# PART B 

from collections import deque

# Q9 Moving average
def q9(data, k):
    if k <= 0 or k > len(data):
        return []

    result = []
    window_sum = 0

    for i in range(len(data)):
        window_sum += data[i]

        if i >= k:
            window_sum -= data[i-k]

        if i >= k-1:
            result.append(window_sum / k)

    return result

print("Q9:", q9([1,2,3,4,5], 3))


# Q10 Polynomial
def q10(coeffs, x):
    result = 0
    for c in coeffs:
        result = result * x + c
    return result

print("Q10:", q10([1,2,3], 2))


# Q11 GCD & LCM
def q11(nums):
    g = nums[0]
    l = nums[0]

    for n in nums[1:]:
        g = math.gcd(g, n)
        l = abs(l*n) // math.gcd(l, n)

    return g, l

print("Q11:", q11([4,6,8]))


# Q12 Prime factors
def q12(n):
    factors = {}
    d = 2

    while d*d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1

    if n > 1:
        factors[n] = 1

    return factors

print("Q12:", q12(60))


# Q13 Matrix
def q13_add(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def q13_scalar(A, k):
    result = []
    for row in A:
        new_row = []
        for val in row:
            new_row.append(val * k)
        result.append(new_row)
    return result

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

print("Q13 Add:", q13_add(A,B))
print("Q13 Scalar:", q13_scalar(A,2))


# Q14 Percentage change
def q14(prices):
    changes = []

    for i in range(1, len(prices)):
        change = (prices[i] - prices[i-1]) / prices[i-1]
        changes.append(change)

    total = 1
    for c in changes:
        total *= (1 + c)

    return changes, total-1

print("Q14:", q14([100,110,121]))


# PART C 

# Q15 Type parsing
def q15(data):
    result = {}

    try:
        result["age"] = int(data.get("age", 0))
    except:
        result["age"] = 0

    try:
        result["price"] = float(data.get("price", 0))
    except:
        result["price"] = 0

    val = str(data.get("active", "")).lower()
    result["active"] = val in ["true","1","yes"]

    result["date"] = data.get("date", "N/A")

    return result

print("Q15:", q15({"age":"20","price":"10.5","active":"yes"}))


# Q16 Tuple mutability
def q16():
    t = (1,[2,3],4)
    print("Before:", t)
    t[1].append(99)
    print("After:", t)

q16()


# Q17 Dict keys
def q17():
    d = {}
    d[1] = "ok"
    d[(1,2)] = "ok"
    print("Valid:", d)

    try:
        d[[1,2]] = "no"
    except:
        print("List not allowed")

q17()


# Q18 Shallow vs deep
def q18():
    a = [[1,2],[3,4]]
    b = copy.copy(a)
    c = copy.deepcopy(a)

    a[0][0] = 99

    print("Original:", a)
    print("Shallow:", b)
    print("Deep:", c)

q18()


# Q19 Sorting
def q19(lst):
    return sorted(lst, key=lambda x: (not x.isdigit(), x.lower()))

print("Q19:", q19(["apple","10","Banana","2"]))


# Q20 Duck typing
def q20(seq):
    total = 0
    try:
        for x in seq:
            total += x
        return total
    except:
        return "Error"

print("Q20:", q20([1,2,3]))


# Q21 Namedtuple
def q21():
    Student = namedtuple("Student", ["name","marks"])
    s = Student("Ali",[80,90,100])
    avg = sum(s.marks)/len(s.marks)
    print("Name:", s.name)
    print("Avg:", avg)

q21()


#  PART D 

# Q22 First even
def q22(data):
    for sub in data:
        for num in sub:
            if num % 2 == 0:
                return num
    return None

print("Q22:", q22([[1,3],[5,7,8]]))


# Q23 Filter lines
def q23(lines):
    result = []
    for line in lines:
        if line.strip() == "" or line.strip().startswith("#"):
            continue
        result.append(line)
    return result

print("Q23:", q23(["hi","","#comment","bye"]))


# Q24 Sum until sentinel
def q24(nums):
    total = 0
    for n in nums:
        if n == -999:
            break
        total += n
    return total

print("Q24:", q24([10,20,-999,50]))


# Q25 Validate tokens
def q25(s):
    total = 0
    invalid = 0

    for t in s.split():
        try:
            total += int(t)
        except:
            invalid += 1

    return total, invalid

print("Q25:", q25("10 20 abc 30"))


# Q26 Menu
def q26():
    while True:
        print("1.A 2.B 3.Exit")
        ch = input("Enter: ")

        if ch == "1":
            print("Coming soon")
            pass
        elif ch == "2":
            print("Coming soon")
            pass
        elif ch == "3":
            break
        else:
            print("Invalid")



# Q27 Retry
def q27():
    for i in range(3):
        pwd = input("Enter password: ")
        if pwd == "1234":
            print("Success")
            break
        else:
            print("Wrong")
    else:
        print("Failed")




# PART E (LISTS)

# Q28 Remove duplicates (keep order)
def q28(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print("Q28:", q28([1,2,2,3,1,4]))


# Q29 Split into chunks
def q29(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i+n])
    return result

print("Q29:", q29([1,2,3,4,5], 2))


# Q30 Second largest unique
def q30(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

print("Q30:", q30([1,5,3,5,2]))


# Q31 Rotate list
def q31(lst, k):
    if len(lst) == 0:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print("Q31:", q31([1,2,3,4,5], 2))


# Q32 Squares of even numbers
def q32(nums):
    return [x*x for x in nums if x % 2 == 0]

print("Q32:", q32([1,2,3,4,5]))


# Q33 Flatten one level
def q33(lst):
    result = []
    for sub in lst:
        for x in sub:
            result.append(x)
    return result

print("Q33:", q33([[1,2],[3],[4,5]]))


# Q34 Element-wise sum
def q34(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

print("Q34:", q34([1,2,3],[4,5,6]))


# Q35 Find indices
def q35(lst, target):
    result = []
    for i in range(len(lst)):
        if lst[i] == target:
            result.append(i)
    return result

print("Q35:", q35([1,2,3,2,4], 2))


# PART F (TUPLES) 

# Q36 Swap variables
def q36():
    a = 5
    b = 10
    a, b = b, a
    print("Q36:", a, b)

q36()


# Q37 Min max avg
def q37(lst):
    mn = min(lst)
    mx = max(lst)
    avg = sum(lst) / len(lst)
    return mn, mx, avg

print("Q37:", q37([1,2,3,4]))


# Q38 Pair grouping
def q38(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append((lst[i], lst[i+1]))
    return tuple(result)

print("Q38:", q38([1,'a',2,'b']))


# Q39 Sort tuples by second
def q39(data):
    return sorted(data, key=lambda x: x[1])

print("Q39:", q39([('a',3),('b',1),('c',2)]))


# Q40 Distance between points
import math
def q40(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

print("Q40:", q40((0,0),(3,4)))


# PART G (SETS)

# Q41 Unique words
def q41(s):
    words = re.findall("[a-zA-Z]+", s.lower())
    return set(words)

print("Q41:", q41("Hello hello world"))


# Q42 Set operations
def q42(A, B):
    return A|B, A&B, A-B, A^B

print("Q42:", q42({1,2,3},{2,3,4}))


# Q43 Remove duplicates using set
def q43(lst):
    return list(set(lst))

print("Q43:", q43([1,2,2,3]))


# Q44 Missing numbers
def q44(lst, n):
    return list(set(range(1,n+1)) - set(lst))

print("Q44:", q44([1,2,4,6], 6))


# Q45 Common items in all lists
def q45(lists):
    common = set(lists[0])
    for l in lists[1:]:
        common = common & set(l)
    return common

print("Q45:", q45([[1,2,3],[2,3,4],[2,5,3]]))


# PART H (DICTIONARIES) 

# Q46 Word frequency
def q46(s):
    words = re.findall("[a-zA-Z]+", s.lower())
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    return d

print("Q46:", q46("hello world hello"))


# Q47 Invert dictionary
def q47(d):
    return {v:k for k,v in d.items()}

print("Q47:", q47({"a":1,"b":2}))


# Q48 Merge dictionaries
def q48(d1, d2):
    return {**d1, **d2}

print("Q48:", q48({"a":1},{"a":2,"b":3}))


# Q49 Group names
def q49(names):
    result = {}
    for name in names:
        key = name[0].lower()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result

print("Q49:", q49(["Ali","Ahmed","Bilal","Babar"]))


# Q50 Safe lookup
def q50(d, key, default, counter):
    if key in d:
        return d[key]
    else:
        counter[0] += 1
        return default

count = [0]
print("Q50:", q50({"a":1},"b",0,count))
print("Default used:", count[0])



