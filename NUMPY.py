#Extract element greater than 5
import numpy as np
arrray=np.array([0,1,2,3,4,5,6,7,8,9])
a=np.array([11,22,33,54,55,66,77,99])
greater_than_5=np.extract(arrray>5, arrray)
print(greater_than_5)


#Split the array into 2 equal sized sub arrays
import numpy as np
x=np.array([9,8,7,6,5,4,3,2,1,0])

sub=np.split(x,2)
print(sub)

#Print sub array using for loop
for p in sub:
  print(p)


import numpy as np
ar=np.array([55,87,32,12,90,45,73,91,69])

#Sort the array in ascending order (creates a new sorted array)
asending_sort= np.sort(ar)
print ("ASCENDING:  ", asending_sort)

#Sort the array in descending order (creates a new sorted array)
desending_sort= np.sort(ar)[::-1]
print ("DESCENDING:  ", desending_sort)
