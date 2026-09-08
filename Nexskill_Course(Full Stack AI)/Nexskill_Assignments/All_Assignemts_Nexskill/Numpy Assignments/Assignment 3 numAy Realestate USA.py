import numpy as np
broker, pri, bed, bath, acer_lot, street = np.genfromtxt(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Numpy Assignments\RealEstate-USA (1).csv",
              delimiter=",",
              usecols=(0,2, 3, 4, 5, 6),
              dtype=("i8, i8, i8, i8, f8, i8"),
              invalid_raise=False,
              unpack=True,
              skip_header=1)
All_data = broker, pri, bed, bath, acer_lot, street
print(All_data)

# Statistics operations
price_mean = np.mean(pri)
print("Mean of Price ",price_mean)
print("Median of broker ",np.median(broker))
print("Average of bath ", np.average(bath))
print("Percentile of 25% ", np.percentile(acer_lot, 25))
print("max of bed", np.max(bed))
print("min of street", np.min(street))
print()

# Maths operations
print("Square of acer_lot ", np.square(acer_lot))
print("SquareRoot of pri", np.sqrt(pri))
print("Power on broker", np.power(broker, 3))
print("absolute of bath", np.abs(bath))
print()

# Perform basic arithmetic operations
adition = bed + bath
sub = acer_lot - street
mul = bed * pri
div = broker / acer_lot
print("Addition", adition)
print("Substraction", sub)
print("Multiply", mul)
print("Division", div)
print()

#  Trigonometric functions
print("sine", np.sin(pri))
print("cos", np.cos(bed))
print("Tan", np.tan(street))
print()

#  Calculate the natural logarithm and base10 logarithm
print("Natural log of Price", np.log(pri))
print("Log base 10 on Acer Lot", np.log10(acer_lot))
print()

#  Hyperbolic
print("Hyperbolic sinh", np.sinh(bath))
print("Hyperbolic cosh", np.cosh(pri))
print("Hyperbolic Tanh", np.tanh(street))
print()

# Inverse Hyperbolic
print("Inverse Hyperbolic Tan", np.arctanh(acer_lot))
print("Inverse Hyperbolic sin", np.arcsinh(bed))
print("Inverse Hyperbolic cos", np.arccosh(broker))
print()

# 2dimentional arrary
D2_arry = np.array([bed, bath])
print("2 Demension array ",D2_arry)
print("Shape", np.shape(D2_arry))
print("Size", np.size(D2_arry))
print("Number of Demension are ", np.ndim(D2_arry))
print()

# Splicing-array
D2_slicing = D2_arry[:2, :3]
print("Slicing from row index 0 to 1 and in clomn feom 1 to 2 ",D2_slicing)
print()

print("Indexing")
d2_index = D2_arry[0,4]
print(d2_index)
d2_index = D2_arry[0,1]
print(d2_index)
print()

for i in np.nditer(D2_arry):
    print("nditer",i)

print("Denumerate")
for i in np.ndenumerate(D2_arry):
    print(i)

print()

# Reshaping
print("Reshape")
print(np.reshape(All_data, (200, 6)))
print(np.shape(All_data))
print(All_data)
print(np.size(All_data))
print(np.ndim(All_data))
