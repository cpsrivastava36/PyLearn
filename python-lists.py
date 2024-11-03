#lists are ordered collection, store multiple values in single variable, items are separated b commas and enclosed within square brackets[]
# lists are changeable meaning we can alter them after creation so they are mutable.
marks = [3, 5, 6]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[:2])
#it also accepts negative indexing as well so print(marks[-3]) will print 0th index elemet whihc is len(marks)-index
print(marks[-3])
#check whether item present in list or not, no neefd to iterate whole list and if likr we do in regaulr other languages, here use keyword "in"
if 4 in marks:
    print("yes")
else:
    print("no")
if "Harry" in marks:
    print("found")
else:
    print("not found")
marks = [3, 5, 6, "Harry", True]
if "Harry" in marks:
    print("found")
else:
    print("not found")
#same rule applies to string as well
if "Har" in "Harry":
    print("Yes")
else:
    print("No")

#range index
# you can print range of list items by specifying where you want to start,where do you want to end and if you want to skip elements in between the range.
#listName[start: end: jumpIndex]
print(marks[1:4:2])

#List Comprehension
#are used to create lists from other iterables like lists, tuples, dictionaries, sets anbd even in arrays and stringsd
#List=[Expression(item) for item in iteratable if condition] #:expression: it is the item which is being iterated, #:iterable: it can be any data structure, #:condition: condition checks 
#if the item should be added to the new list or not.

names=["Heelo", "Saching", "Sehwag", "Dravid"]
namesWith_0 = [item for item in names if "o" in item]
print(namesWith_0)

#another example, accept item whihc has lenght >4
names = ["Priya", "Daivik", "Sachin", "Sehwag", "Prateek", "Deepu"]
namesWith_4 = [ name for name in names if len(name)>6]
print(namesWith_4)

#list methods
#1. append. the original method get modified
list=[1,2,3,45,87,9]
list.append("HARRY")
print(list)

#2.reverse()
list.reverse()
print(list)

#3.sort(reverse=True) // it only supports for cases where consistent items of same type are in list. Heterogeneous items in list can not ber reversed by this 
#method. you need to use  reverse() method for that.
#list.sort(reverse=True)
list1=[1,4,67,90]
print(list1.sort(reverse=True)) # this one doesnt print anything
print(list1)

#4. index gives element atthat index and count gives number of times that element was repeated
print(list1.count(67))

#5. copy method creates shallow copy of the same list and its copy by value and deosnt impact orginal list
list2=list1.copy()
print(list2)

#6. copy by brefernce is done by quals operator and it is deep copy of original list and any changes in copied list impacts the original list as well.
list3=list2
print(list3)
list3.append(22)
print("original list impacted ",list2)

#7. concatenate two list by using + operator
list4 = list3+list
print(list4)

#8. add alist to a list
colors=["violet","green","blue","yellow"]
rainbow=["violet","indigo","orange"]
colors.extend(rainbow)
print(colors)


