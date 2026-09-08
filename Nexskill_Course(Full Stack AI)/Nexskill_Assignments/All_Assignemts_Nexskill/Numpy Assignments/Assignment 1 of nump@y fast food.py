import numpy as np

latitude, longitude, name = np.genfromtxt(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Numpy Assignments\FastFoodRestaurants.csv",
    delimiter=',',
    usecols=(4, 5, 6),
    unpack=True,
    dtype=('f8', 'f8', 'U100'),
    encoding='utf-8',
    skip_header=1,
    invalid_raise=False,
    
)

# Clean output
print("name")
print(name)
print("latitude")
print(latitude)
print("lonhitude")
print(longitude)
print()
print("Statastic applying on dataset")
print()
print("Applying Mean on Latitude and Longitude ")
print("mean of lat", (np.nanmean(latitude)))
print("mean of lon", (np.nanmean(longitude)))
print()
print("Applying STD on Latitude and longitude")
print("STD of latitude",np.nanstd(latitude))
print("STD of longitude",np.nanstd(longitude))
print()
print("Median of Latitude and longitude")
print("Median of latitude ",np.nanmedian(latitude))
print("Median of longitude ",np.nanmedian(longitude))
print()
print("Percentile on latitude and longitude")
print("Percentile - 25 on latitude ", np.nanpercentile(latitude, 25))
print("Percentile - 75 on longitude ", np.nanpercentile(longitude, 75))
print()
print("Max and Min on latitude and longitude")
print("Min of Latitude ", np.nanmin(latitude))
print("Max of Lonitude ", np.nanmax(longitude))
print()
print("Applying math oprations on latitude and longitude")
print("square of latitude ",np.square(latitude))
print()
print("squareRoot of longitude ",np.sqrt(longitude))
print()
print("Power of longitude ", np.power(longitude, 2))
print()
print("absolute of latitude", np.abs(latitude))
print()
print("Performing basic maths")
print("Adding lonitude and latitude")
adiition = longitude + latitude
print(adiition)
print()
print("Sub on lat and lon")
sub = longitude - latitude
print(sub)
print()
print("Multiply lat and lon")
mul = latitude * longitude
print(mul)
print()
print("Div on lat and lon")
div = latitude / longitude
print(div)
print()
print("Applying Trig functions")
print()
lat_pie = (latitude/np.pi) + 2
print("latitude/pie is", latitude)
print()
print("calculate sin , cos, tan")
sin_val = np.sin(lat_pie)
cos_val = np.cos(lat_pie)
tan_val = np.tan(lat_pie)
print("sin is", sin_val)
print("cos is", cos_val)
print("tan is", tan_val)
print("exp is ", np.exp(lat_pie))
print()
print("Applying log on dataset")
log_arry = np.log(lat_pie)
log10_arry = np.log10(lat_pie)
print("Natural log ",log_arry)
print("log -10 is ",log10_arry)
print()
print("cal of hyphine")
hy_sin = np.sinh(lat_pie)
hy_cos = np.cosh(lat_pie)
hy_tan = np.tanh(lat_pie)
print("sinh is", hy_sin)
print("cosh is", hy_cos)
print("tanh is", hy_tan)
print()
print(" Applying Inverse Hyperbolic")
arc_sinh = np.arcsinh(lat_pie)
arc_cosh = np.arccosh(lat_pie)
print(arc_cosh)
print(arc_sinh)
print()
print("2 D arry")
D2_lon_lat = np.column_stack([latitude, longitude])
print(D2_lon_lat)
print()
print("dimension ", D2_lon_lat.ndim)
print("shape", D2_lon_lat.shape)
print("size ",D2_lon_lat.size)
print("data type ", D2_lon_lat.dtype)
print()
print("Slicing ")
D2_slice = D2_lon_lat[:5,:1]
print(D2_slice)
print()
print("Indexing")
D2_index = D2_lon_lat[1,1]
print(D2_index)
print()
# print("Loop")
# for i in D2_lon_lat:
#     print(i)
print()
print("Reshape")
D2_Reshape = np.reshape(D2_lon_lat,(9990,2))
print(D2_Reshape)
D2_shape = np.shape(D2_Reshape)
print(D2_shape)
D2_ndim = np.ndim(D2_Reshape)
print(D2_ndim)
print(D2_Reshape.size)





