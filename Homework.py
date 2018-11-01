# Simon Perrin-Roussel
# Homework for the 6th of November, 2018

def ev_ot_new(list1) :
	'''
	Return a new list [...] of the list
	>>>ev_ot_new([1,2,3,4,5,6,7,8,9,0])
	[1,3,5,7,9]
	'''
	return ev_ot_new[::2]

def ev_ot_modif(list1) :
	'''
	Modify the list [...] is removed
	>>>ev_ot_modif([1,2,3,4,5])
	>>>list1
	[2,4]
	'''
	for item in list1[::2] :
			list1.remove(item)

def sum_of_evens(list1) :
	'''
	Return the sum of all evens in list1
	>>>sum_of_evens([1,2,3,4])
	6 
	'''
	total = 0
	for it in list1 :
		if it % 2 == 0 :
			total = it + total
	return total

def collect_strings(list1) :
	'''
	Return a new list formed of the strings in list1
	>>>collect_strings(['a',2,'b'])
	['a','b']
	'''
	new1 = []
	for it in list1 :
		if type(it) == str :
			new1 = it + new1

def count_int(list1) :
	'''
	Return the number of integers in list1
	>>>count_int([4,5,'oboe',1,2,'4',3.4])
	4
	'''
	count = 0
	for it in list1 :
		if type(it)==int :
			count = 1 + count
	return count

def remove_strings_modif(list1) :
	'''
	Modify the list [...] any strings
	>>>remove_strings_modif([1,'hello',2])
	>>>list1
	[1,2]
	'''
	for item in list1 :
		if type(item)==str :
			list1.remove(item)
	return list1

#Conundrum exercise :

def m10(list_of_numbers, limit) :
	'''
	Return a new list containing all the numbers of list_of_numbers greater than limit
	>>>m10([1,2,3,4,5,6,7,8,9,10],5)
	[6,7,8,9,10]
	>>>m10([2,46,32,67,83],45)
	[46,67,83]
	'''
	l = []
	for e in list_of_numbers :
		if e > limit :
			l.append(e)
	return l