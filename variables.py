m=1.1 
A=3
print(A)
print(m)
f=complex(4,6)           #variables are case sensitive

print(f) 
b="nriika"
print(b)
c='nirika'
print(c)
nirika=9
print(nirika)
d=True
e=None
a=194
a1=932
# print(a+b)  to add same data type huna parxa
print(a+a1)
print("the type of m is ", type(m))


print("the type of a is ", type(a))
print("the type of b is ", type(b))
print("the type of c is ", type(d))
print("the type of d is ", type(e))
print("the type of A is ", type(A))
c= 3+4j
# print(int(c)) raise Typeerror cant convert complex to any data type directly
print(int(c.real))
print(float(c.real))
print(float (c.imag))
