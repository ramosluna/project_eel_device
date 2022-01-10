<<<<<<< Updated upstream
test = ':10000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00'
s = "This be a string"
if test.find(":") == -1:
    print("No 'is' here!")
else:
    print("Found 'is' in the string.")
=======
#first method is called on the object to converts it to an iterator object.
#next() method is called on the iterator object to get the next element of the
#comp_list = [x ** 2 for x in range(7) if x % 2 == 0]
#list = [i for i in range(11) if i % 2 == 0]


value1 = [x for x in open('./task.txt')if x.startswith('TaskId') or x.startswith('taskId')]
print(value1)
>>>>>>> Stashed changes
