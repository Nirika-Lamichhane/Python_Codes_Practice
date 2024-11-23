list1=[8, 2.3,8,4, [-4, 5],["apple","banana"]]
print(list1) #mutable

# removing duplicate from list 
# set1= set(list1)  #error because our list include nested list

# print(set1)



tuple1=(("parrot","sparrow")) #not mutable
print(tuple1)

dict1={"name":"nirika","age":20,"canVote":True}
print(dict1) #mutable key value pairs

dict1["city"]="New York"
print(dict1)

del dict1["canVote"]
print(dict1)

list1.append(80)
print(list1)

list1.remove(2.3)
print(list1)

list1[0]=38
print(list1)


d1= {"name":"anamika","age":34,"country":"Nepal"}
print(d1)

l=[30,380,"nirika","good", ["apple","banana"]]
print(l)

t=("arey ","what you doing bro")
print(t)

my_set={1,2,3,4}
print(my_set)

set_dup={1,2,3,1,2,5,5} #dup are removed

print(set_dup)
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

t1=(2,3,3,4,2) #print all duplicate in list and tuple
print(t1)

#removing repeated from list
li=[2,3,4,5,4,5]
s1=set(li)
print(s1)
