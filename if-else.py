applePrice = 210
budget = 200
if( applePrice <= budget):
    print("You can buy apple")
else:
    print("You cant buy apple") 

x =int(input(f'enter the value of x '))

match x:
    case 0:
        print(f'x is zero')
    case 1:
        print(f'x is 1')
    case 4:
        print(f'x is 4')
    case _ :
        print(f' x is default ')

inputNum = input("please input your favourite color ")
for char in inputNum:
    print(char)

#range function9
for num in range(10) :
    print(num)

#range function with 2 params
for num in range(1, 10) :
    print(num)
print(f'start of 3 range param with step 1')
#range function with 3 params, step function5656
for num in range(1, 10, 1) :
    print(num)
print(f'start of 3 range param with step 2')
#range function with 3 params, step function
for num in range(1, 10, 2) :
    print(num)
print(f'start of 3 range param with step 2 and stop 11')
#range function with 3 params, step function
for num in range(1, 11, 2) :
    print(num)
print(f'start of 3 range param with step -2 and stop 11')
#range function with 3 params, step function
for num in range(11, 1, -2) :
    print(num)
while True:
    print("emulating do while loop")
    break
num=int(input(f'enter number for while to run '))
