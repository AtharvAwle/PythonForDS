#arrays of python

li = [2 , 1 , 4 , 5 , 8 , 7 , 6 , 4 , 7 , 8 , 6 ]

#this is a list and original strings gets change when we use any of the methods
li.sort()  #sorts the list in assending
li.sort(reverse=True) #to sort the list in decending manner
li.append(99)  #adds an element at the end of list
li.remove(4) #removes a specific element
li.pop()  #pops the last element from the list
li.clear()  #emptys the array/list
li.index(2)  #gives the index of the given element
li.extend([334,34,34,234234,23424])  #adds the another list
print(li)


#w3 school docs
#
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
