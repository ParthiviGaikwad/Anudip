#WAP to create array elements between 25 to 45(10 elements).Arrange them in equal size array.

import numpy as np

ar=np.arange(25,45)
print (ar)

print("\n")

sub=np.split(ar,2)

for x in sub:
  print(x)

#Q.2)find array element greater than 10 

a=np.array([1,7,9,33,54,22,9,4])

gr=np.extract(a>10,a)
print(gr)


#WAP to concatenate two array apply all mathematical operator on the same

#WAP to concatenate two array
b=np.array([99,98])
c=np.concatenate((a,b)) #why throw error if only 1 pair of bracket?
print("Concatenate two array a and b= ",c)

#apply all mathematical operator on the same
add=c+2
sub=c-2
mul=c*2
div=c/2
print("add= ",add)
print("sub= ",sub)
print("mul= ",mul)
print("div= ",div)



#Q.4)Extract all odd numbers from array

a=np.array([1,7,9,33,54,22,9,4])
odd=a[a%2==1]
print(odd)
