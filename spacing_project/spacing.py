
# debug = True
debug = False

# test_list = [['apple','banana','carrot'],['date','egg','fruitcake']]

def getMaxSpacing(input_list, position = 0):
	'''
	returns the max length from the input_list at the given position

	examples: [['apple','banana','carrot'],['date','egg','fruitcake']]
		position 0 should return 5
		position 1 should return 6
		position 2 should return 9
	
	precondition: input_list is a non-empty list of non-empty lists

	precondition: position is an integer greater than or equal to 0
	'''
	
	assert type(input_list) == list, 'input_list needs to be a list'
	assert type(position) == int, 'position needs to be an integer'
	assert position >= 0, 'position needs to be greater than or equal to zero'
	assert len(input_list) > 0, 'input_list can not be empty'
	assert len(input_list[0]) > 0, 'input_list elements can not be empty lists'

	row_count =  len(input_list)
	
	return row_count

# if __name__ == 
# getMaxSpacing(test_list)