print("Wellcome to my lsit practice")
customer_list = ["Hussnain", 5523, 35.7, True]
print(customer_list)

print(type(customer_list))

customer_list.append("AbuBakar")
print(customer_list)

customer_list.insert(1, "Lahore")
print(customer_list)

print(customer_list[1])
print(customer_list[2])
print(type(customer_list[2]))

customer_list.remove(5523)
print(customer_list)

customer_list.pop(1)
print(customer_list)


customer_list[0] = "Saifi"
print(customer_list)