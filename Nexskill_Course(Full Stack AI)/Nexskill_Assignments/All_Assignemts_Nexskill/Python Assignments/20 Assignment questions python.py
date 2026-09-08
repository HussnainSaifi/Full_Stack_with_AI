# BEGINNER LEVEL: STRINGS FUNDAMENTALS

# 1. Length of a String
p = input("Enter string: ")
print(len(p))





# 2. Uppercase and Lowercase
d = input("Enter your string: ")
print(d.upper())
print(d.lower())





# 3. Count a Character
a = input("Enter string: ")
z = input("Enter word: ")
print(f"Character {z} appears:", a.count(z), "times")





# 4. First & Last Character
x = input("Enter string: ")
if not x:
    print("Empty string")
else:
    print(x[0])
    print(x[-1])





# 5. Check Substring Presence
f = input("Enter string: ")
su = input("Enter substring: ")
print(su in f)






# 6. Slice a String
e = input("Enter string: ")
start = int(input("Enter 1st index: "))
end = int(input("Enter 2nd index: "))
print(e[start:end])






# 7. Reverse a String
b = input("Enter string: ")
print(b[::-1])






# 8. Replace Substring
o = input("Enter your string: ")
ol = input("Enter want to replace: ")
ne = input("Enter new word to replace: ")
print(o.replace(ol, ne))





# 9. Split and Join
u = input("Enter string: ")
wor = u.split()
jo = "-".join(wor)
print(jo)





# 10. Strip Whitespace
q = input("Enter string for strip : ")
print(q.strip())






# INTERMEDIATE LEVEL: STRING TASKS

# 1. Count Vowels & Consonants
m = input("Enter a string: ")
vowels = consonants = 0
for i in m:
    if i.isalpha():
        if i.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels, "Consonants:", consonants)





# 2. Palindrome Check (Ignore case & non-alphanumerics)
b = input("Enter string: ")
nor = ''.join(x.lower() for x in b if x.isalnum())
palindrome = nor== nor[::-1]
print("Is palindrome:", palindrome)





# 3. Title Case (Manual)
p = input("Enter sentence: ")
words = p.split()
title_case = ' '.join(word[0].upper() + word[1:].lower() if word else '' for word in words)
print("Title case:", title_case)





# 4. Find All Indices of a Substring (Allow Overlaps)
l = input("Enter string:")
sub = input("Enter substring:")
ind = [i for i in range(len(l)-len(sub)+1) if l[i:i+len(sub)] == sub]
print(ind)





# 5. Character Frequency Dictionary (case-insensitive, skip spaces)
f = input("Enter string: ")
fre = {}
for z in f.lower():
    if z != ' ':
        fre[z] = fre.get(z,0)+1
print (fre)




# 6. Anagram Checker (ignore spaces, punctuation, case)
t1 = input("Enter 1 string: ")
t2 = input("Enter 2 string: ")
c1 = sorted(c.lower() for c in t1 if c.isalpha())
c2 = sorted(c.lower() for c in t2 if c.isalpha())
print(c1 == c2)





# 7. Compress Repeated Characters (RLE-lite)
o = input("Enter a string: ")
if o:
    re = ""
    count = 1
    for i in range(1, len(o)):
        if o[i] == o[i-1]:
            count += 1
        else:
            re += o[i-1] + str(count)
            count = 1
    re += o[-1] + str(count)
else:
    re = ""
print(re)






# 8. Longest Word in a Sentence
u = input("Enter sentence: ")
tok = u.split()
lo = ""
for tok in tok:
    wo = ''.join(q for q in tok if q.isalpha())
    if len(wo) > len(lo):
        lo = wo
print(lo)





# 9. Remove Duplicate Characters but Keep Order
y = input("Enter string: ")
se = set()
re = ''
for k in y:
    if k not in se:
        re += k
        se.add(k)
print(re)






# 10. Mask Email Username
e = input("Enter email: ")
if '@' in e:
    usn, domain = e.split('@',1)
    if len(usn) > 2:
        mas = usn[0] + '*'*(len(usn)-2) + usn[-1]
    else:
        mas = usn
    m_e = mas + '@' + domain
    print(m_e)
else:
    print("wrong format")