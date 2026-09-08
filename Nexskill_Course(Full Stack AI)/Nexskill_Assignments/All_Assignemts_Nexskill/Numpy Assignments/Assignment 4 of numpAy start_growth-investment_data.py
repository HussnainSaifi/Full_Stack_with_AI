import numpy as np
funding_rounds, investment_amt, valuation, no_of_instrs, growth_rate = np.genfromtxt(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Numpy Assignments\startup_growth_investment_data.csv",
    delimiter=",",
    usecols=(2,3,4,5,8),
    unpack=True,
    dtype=("i8, f8, f8, i8, f8"),
    skip_header=1,
    invalid_raise=False)
All_data = funding_rounds, investment_amt, valuation, no_of_instrs, growth_rate
print(All_data)


#            Statistics Operation

print("Mean of Funding Rounds ",np.mean(funding_rounds))
print("Median of investment amount ",np.median(investment_amt))
print("Average of Valuation ", np.average(valuation))
print("Percentile of 25% ", np.percentile(no_of_instrs, 25))
print("max of Growth rate", np.max(growth_rate))
print("min of Funding rounds", np.min(funding_rounds))
print()

#               Maths operations on Funding Rounds
print("Square ", np.square(funding_rounds))
print("SquareRoot ", np.sqrt(funding_rounds))
print("Power ", np.power(funding_rounds, 6))
print("absolute ", np.abs(funding_rounds))
print()

#                  Arithmetic Operations
adition = funding_rounds + no_of_instrs
sub = investment_amt - valuation
mul = growth_rate * valuation
div = no_of_instrs / investment_amt
print("Addition", adition)
print("Substraction", sub)
print("Multiply", mul)
print("Division", div)
print()

#                    Trigonometric functions on Investment amount
print("sine", np.sin(investment_amt))
print("cos", np.cos(investment_amt))
print("Tan", np.tan(investment_amt))
print()

#                      Natural logarithm and base10 logarithm on growth rate
print("Natural log ", np.log(growth_rate))
print("Log base 10 ", np.log10(growth_rate))
print()

#                        Hyperbolic on Funding Rounds
print("Hyperbolic sinh", np.sinh(funding_rounds))
print("Hyperbolic cosh", np.cosh(funding_rounds))
print("Hyperbolic Tanh", np.tanh(funding_rounds))
print()

#                        Inverse Hyperbolic on Num_of_investers
print("Inverse Hyperbolic Tan", np.arctanh(no_of_instrs))
print("Inverse Hyperbolic sin", np.arcsinh(no_of_instrs))
print("Inverse Hyperbolic cos", np.arccosh(no_of_instrs))
print()

#                       2-Dimension Array
D2_arry = np.array([funding_rounds, no_of_instrs])
print("2-Demension array ",D2_arry)
print("Shape ",np.shape(D2_arry))
print("Size ",np.size(D2_arry))
print("Num of Demension ",np.ndim(D2_arry))
print()

#                          Splicing on Array
D2_slicing = D2_arry[:3, :2]
print("Slicing from row index 0 to 1 and in clomn feom 1 to 2 ",D2_slicing)
print()

print("Indexing")
d2_index = D2_arry[1,500]
print(d2_index)
d2_index = D2_arry[0,600]
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
print(np.reshape(All_data, (5000, 5)))
print(np.shape(All_data))
print(All_data)
print(np.size(All_data))
print(np.ndim(All_data))