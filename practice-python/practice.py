print(5)
print(-10)
print(3.14)
print("ㅋ"*100)
print(not True)

var1 = "variant test"
print(var1)

print(5//3)
print(10//3)

print(3**3)
print(pow(3,3))

from random import *
print(int(random()*100))
print(randrange(1,2))
print(randint(1,2))

strisarray = "0123456789"
print(strisarray[0])
print(strisarray[9])
print(strisarray[0:2])
print(strisarray[:7])
print(strisarray[:-7])

struplow = "Python is funny!"
print(struplow.upper())
print(struplow.lower())
print(struplow.isupper())
print(struplow[0].isupper())

print("Red Apple¥rsPine")



array1 = ["a1", "b1", "c1"]
print(array1)
array2 = {"a1" : "a11", "b1" : "b11"}
print(array2)
array2["a1"] = "a11111"
array2["c1"] = "c11"
del array2["b1"]
print(array2)