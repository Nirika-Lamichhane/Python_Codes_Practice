print(3+5)
print(9-4)
print(6*5)
print(9/3) # true division :: it always returns the division in float value even if it is a whole number
print(9//3) #gives int value i.e. 3 only
print(8//3)  # removes decimal part
print(6%5)   # modulus:: gives the remainder i.e. decimal part
print(9**3) #power ma lagxa 9 ko power 3 exponentiation


a=3
a**=3
print(a)
a//=2
print(a)

#logical operators returns true or false
print (7<10 or 3>4)
print(not 4>3)
print(5>3 and 2<4)


#identity operators :: is and is not

#is checks if the two variables point to the same object in the memory
a=[1,2,3]
b=a #b points to the same list objects as a
c= [1,2,3]
#c is different list object wiht same eleemts

print(a is b)
print(a is c)

# membership operator are in and not in
print( 3 in a)
print (5 not in a)

#identity

print(a is not b)
print(a is not c)


x = 1000
y = 1000

print(x is y)       # Output: False, because they are different objects in memory
print(x == y)       # Output: True, because their values are the same

# For smaller integers, Python caches them, so:
x_small = 5
y_small = 5

print(x_small is y_small)  # Output: True, because they refer to the same cached object

#BITWISE OPERATOR: operation on binary numbers

y=5 #binary 000101
x=3 #binary 000011

result =x & y #bitwise and results 1 if both bits are 1 otherwise 0
print(result)

result = x | y #bitwise or :: if at least one bit is 1 then 1
print (result)

result=~y  #bitwise not i.e. flips all 0 to 1 and vise versa
print(result)

result = x ^y #XOR i.e. result is 1 if the bits are different and 0 otherwise
print(result)

x=9 #binary 001001
result =x<<2 #left shift: shifts the bits of an operand to the left by the specified numebr of positions
print(result)

x=5
result =x>>2 #right shift operator :: fills vacant with 0s
print(result)