def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
calculateGmean(5, 7)

def calculateGreater(a, b):
    if(a>b):
        print("A is grater than B")
    elif(a==b):
        print("B is equal to A")
    else:
        print("B is greater than A")
calculateGreater(20, 25)

def calculateHyperbola(a, b):
    pass

def calculateAverage(a, b):
    avg= (a+b)/2
    print("avergae of 2 numbers is", avg)
calculateAverage(10, 20)

#default args , required args, arbitrary args are such use cases of same thing
#can provide default values while creating function. function with default values assume a default valu in case if value for that args in not provided
# def name(firstName, middleName="Prakash", lastName="Srivastava"):
#   print("Hi", firstName, middleName, lastName)

def defaultVluesTest(a=20, b=10):
    print("default values test ", a, b)

defaultVluesTest()

#varibale length args
#for in case you have user defined list of numbers, so you create a fucntion, pass var* before the param name while defining the function. function
# accesses the args by processing them in form of dictionary or tuple
# case -1 : Arbitrary args: function access args by procesig them in form of tuple.

def name(*name):
    print("Heloo, ", name[0], name[1], name[2])

name("Chandra", "Prakash", "Srivastava")

def average(*num):
    sum=0
    for i in num:
        sum = sum + i
    print("Average is ", sum/(len(num)))

average(1,2,3,4,5)
#case-2 : KeyWord Aribitrary args : function access args by processing them in form of dictionary(key-value pair like map). its syntax is **var.

def name(**name):
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Prakash", lname="Srivastava", fname="Chandra")


a=9
b=10

