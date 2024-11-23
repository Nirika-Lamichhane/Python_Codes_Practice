name = "Alice"
message = "Hello, {}!".format(name)
print(message)

str_with_escape = 'This is a backslash: \\ and a newline: \nHello!'
print(str_with_escape)

# string literals
a ='''
he said 
nirika
how are you?
i replied "i am good"
'''
print(a)

#for loop
for character in a:
    print(character)
    '''
    this prints every single character of word in a single line and new
    line occurs after each word
    '''
name="nirika"
for character in name:
    print(character)


print("\n")
print(name[4])

#indexing of string 

names=["nirika","arika","aditya","avinash","meera"]
print(names[0:4])

#join 
names1=" ".join(names)
print(names1)


name="akash","nriika"
print(name[2:9])

#length of string

l=len(name)
print(l)

fruit="mango"
length = len(fruit)
print("Mango is a ",length,"letter word")

print(fruit[0:4])
print(fruit[:4])  #esle suruma afai 0 haldinxan
print(fruit[1:4])  #including 1 but not icluding 4
print(fruit[4:])
print(fruit[0:-3])
print(fruit[-3:-1])

#string operation
a="!@nirika!@!@"
print(len(a))
print(a.upper())
print(a.replace("!@", "arika"))
print(a.rstrip("!@"))

b= "nirika is good"
print(b.split())

'''
split() and rstrip() is different in python as rstrip
removes trailing element right after the string we can give any element
and strip() removes the whitespaces and tabs and print out in the list format
'''

#center method

newOne="Introduction to java and I am nirika Lamichhane"
print(newOne.capitalize())

str1="welcome to console"
print(str1.capitalize())
print(str1.center(40))
print(str1.center(40,"*"))

print(len(str1))
print(len(str1.center(40)))

#count method: count with the same technique as length.

m="nirika!@ nirika nirika"
print(m.count("nirika"))
print(m.split(" "))

print(m.endswith("a"))

n="nirika is here to do python programming"
print(n.endswith("to",4,10))

#find and index is used to get index 
'''
find return -1 if not present
index gives error
'''
str1="He's name is Dane. He is 80 years old and is an honest man"
print(str1.find("is"))
# print(str1.index("ishh")) error

print(str1.isalnum())
str2 = "hi nirika"
print(
    str2.isalnum()
)
print(str2.isalpha()) #false due to space

str="hi guys!! i am nirika \n "
print(str.title())
print(str.isprintable())

str="hi guys!! i am nirika"
print(str.isprintable())

str1= "hi , i AM nIRIKA lAMIchhane"
print(str1.swapcase())