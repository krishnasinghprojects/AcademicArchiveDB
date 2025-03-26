num=float(input("Enter The Number : "))
approx=0.5*num
better=0.5*(approx+num/approx)
while(better!=approx):
    approx=better
    better=0.5*(approx+num/approx)
print("Square Root : ",better)