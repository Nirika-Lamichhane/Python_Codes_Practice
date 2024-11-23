#if else

a= int(input("enter your age: "))
if (a>18):
    print("vote")

else:
    print("cant vote")

#elseif

a= int(input("enter a numbers: "))
if (a<0):
    print("negative")
elif (a==0):
    print("zero")

else:
    print("positive")
    
# match case statement:: default is not necessary in each case
y= int (input("Enter the number: "))

match y:
  case 1:
    print ("one")
    
  case 2:
    print ( "the number is 2")
  case 3:
    print (" it is 3")

  case _ : #_ is used for default case
    print ("this is default " , y)

