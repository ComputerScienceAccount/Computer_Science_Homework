def largest(list_of_numbers) :
	'''
	Return the largest number in list_of_numbers
	>>>largest([1,2,3,4,5])
	5
	'''
	list_of_numbers.sort()
	return list_of_numbers[-1]

def remove_duplicates(old_list) :
	'''
	Return a copy of old_list which has no duplicate elements
	>>>remove_duplicates([1,2,3,1,2,3,4,5])
	[1,2,3,4,5]
	'''
	new = []
	for item in old_list :
		if item not in new :
			new.append(item)
	return new

def common_element(list1,list2) :
	'''
	Return True if at least one item is common to both list1 and list2
	>>>common_element([1,2,3],[2,3,4])
	True
	'''
	for it in list1 :
		if it in list2 :
			return True
	return False

def list_to_string(list1) :
	'''
	Return a string consisting of all the items of list1
	>>>list_to_string([1,2,3,4,5])
	'12345'
	'''
	string = ''
	for item in list1 :
		string = string + item
	return string

def extend_list(list1,list2) :
	'''
	Modify list1 so that all the items of list2 are added to its end
	>>>extend_list([1],[2])
	[1,2]
	'''
	for item in list2 :
		list1.append(item)

def all_squares(max_number) :
	'''
	Return a list of all the squares from 1 to max_number
	>>>all_squares(26)
	[1,4,9,16,25]
	'''
	new = []
	for n in range(1,max_number+1) :
		if n*n <= max_number :
			new=new+[n*n]
	return new

def items_in_common(list1,list2) :
	'''
	Return a new list consisting of all the elements that list1 and list2 have in common
	>>>items_in_common([1,2,3],[2,3,4])
	[2,3]
	'''
	new = []
	for n in list2 :
		if n in list1 and n not in new :
			new.append(n)
	return new


def m12(list_of_numbers,upper_limit) :
	'''
	Return False if any of the numbers in list_of_numbers is greater than upper_limit
	>>>m12([1,2,3],2)
	False
	>>>m12([2,54,23],100)
	True
	'''
	b = True
	for e in list_of_numbers :
		if e > upper_limit :
			b = False
	return b
