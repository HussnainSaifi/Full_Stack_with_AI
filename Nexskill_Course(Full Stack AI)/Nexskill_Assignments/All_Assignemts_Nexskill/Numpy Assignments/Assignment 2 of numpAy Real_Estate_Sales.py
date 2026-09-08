import numpy as np
srl_num, asse_value, sale_amt, sale_rto =np.genfromtxt(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Numpy Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv",
    delimiter=",",
    usecols=(0,5,6,7),
    dtype=("i8,f8,f8,f8"),
    invalid_raise=False,
    unpack=True,
    skip_header=1)
print("Serial Numbers",srl_num)
print()
print("Accessed Values", asse_value)
print()
print("Sales Amount", sale_amt)
print()
print("Sales Ratio", sale_rto)
print()
# statistics operations
srl_mean = np.mean(srl_num)
print("Mean of Serial Numbers ",srl_mean)
print("Median of Sales Amount ",np.median(sale_amt))
print("Average of Sales Ratio ", np.average(sale_rto))
print("Percentile of 25% ", np.percentile(srl_num, 25))
print("max of Sales Amount", np.max(sale_amt))
print("min of Sales Amount", np.min(sale_amt))
print()
# maths operations
print("Square of Sales Ratio", np.square(sale_rto))
print("SquareRoot of sales ratio", np.sqrt(sale_amt))
print("Power on sales ratio", np.power(sale_rto,4))
print("absolute of Sales Ratio", np.abs(sale_rto))
print()
# Perform basic arithmetic operations
adition = srl_num + sale_amt
sub = sale_amt - sale_rto
mul = srl_num * sale_rto
div = sale_amt / sale_rto
print("Addition", adition)
print("Substraction", sub)
print("Multiply", mul)
print("Division", div)
print()
#Trigonometric Functions
print("sine", np.sin(srl_num))
print("cos", np.cos(srl_mean))
print("Tan", np.tan(sale_amt))
print()
# Calculate the natural logarithm and base-10 logarithm
print("Natural log of Sales Amount", np.log(sale_amt))
print("Log base 10 on sales ratio", np.log10(sale_rto))
print()
# Hyperbolic
print("Hyperbolic sinh", np.sinh(srl_num))
print("Hyperbolic cosh", np.cosh(srl_num))
print("Hyperbolic Tanh", np.tanh(srl_num))
print()
# Inverse Hyperbolic
print("Inverse Hyperbolic Tan", np.arctanh(srl_num))
print("Inverse Hyperbolic sin", np.arcsinh(sale_amt))
print("Inverse Hyperbolic cos", np.arccosh(sale_amt))
print()
# 2 dimentional arrary
D_arry = np.array([srl_num, sale_rto])
print("2 Demension array ",D_arry)
print("Shape", np.shape(D_arry))
print("Size", np.size(D_arry))
print("Number of Demension are ", np.ndim(D_arry))
print()
# Splicing array
D_slicing = D_arry[:3, :1]
print("Slicing from row index 0 to 3 and in clomn feom 1 to 3 ",D_slicing)
print()
print("Indexing")
d_index = D_arry[1,0]
print(d_index)
d_index = D_arry[0,98]
print(d_index)
print()
for i in np.nditer(D_arry):
    print("nditer",i)

print("Denumerate")
for i in np.ndenumerate(D_arry):
    print(i)

print()
print("Reshape")
All_Data = srl_num, sale_amt, sale_rto, asse_value
print(np.reshape(All_Data, (139, 4)))
print(np.shape(All_Data))
print(All_Data)
print(np.size(All_Data))
print(np.ndim(All_Data))
