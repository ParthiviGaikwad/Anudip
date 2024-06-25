import numpy as np

#Extract all odd numbers from arr
a=np.array([1,6,8,9,4,77,10])
ex=np.extract(a%2==0,a)
print("Extract all odd numbers from array ",ex)

#find array element greater than 10
gr=np.extract(a>10,a)

#WAP to concatenate two array
b=np.array([99,98])
c=np.concatenate((a,b)) #why throw error if only 1 pair of bracket?
print("Concatenate two array a and b= ",c)

#apply all mathematical operator on the same
add=a+2
sub=a-2
mul=a*2
div=a/2
print("add= ",add)
print("sub= ",sub)
print("mul= ",mul)
print("div= ",div) 
