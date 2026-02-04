message="Hello World!!!  "
print(message.strip())
print(message.upper())
print(message.replace("World","python"))
print(message[0])
label= "Data Science"
print(label[0])
print(label[::-1])
print(label[:6])
print(label[7:])
print(label[2:6:-1])
print(label[0::1])
print(list(label))
print(list(label[:6]))
label.split()
for i in label:
    print(""+i)

print("i love \"python programming\"")
a=[1,5,3,4,2,7,8,9,6]
a.sort()
print("sorted:",a)
a.append(10)
print(a)
a.pop()
print(a)
print(a.index(7))
a.reverse()
print(a)
a.extend([10])
print(a)
import numpy as np
num=np.argmax(a)
print(num)
a=(1,3,2,2,2,4,5,3,7)
print(a.count(3))
print(a.index(3))
values=[1,2,3,4,5,6,7,8]
sum=lambda a,b:a+b
print(sum(2,5))
abc=lambda x:x*x
print(abc(2))
values=[1,2,3,4,5,6,7,8]
print(list(map(lambda x:x+2,values)))
e=list(filter(lambda x:x%2==0,values))
print(e)
print(list(filter(lambda x:x%2==0,values)))
values=[1,2,3,4,5,6,7,8]
from functools import reduce
print(reduce(lambda x,y:x+y,values))
print()