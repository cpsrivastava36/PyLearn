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