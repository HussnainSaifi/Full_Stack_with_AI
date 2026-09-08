customer_info = "Customer name is Kim Jo and he located in california"
print(len(customer_info))
count = 0
for i in customer_info:
    count += 1
    print(i, "is at index" ,count)

print(customer_info.upper())
print(customer_info.lower())

Name = customer_info[17:23]
print(Name)

City = customer_info[-10:]
print(City)

