
# debug = True
debug = False

test_list = [['apple','banana','carrot'],['date','egg','fruitcake']]

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
	col_count = len(input_list[0])
	
	temp_max_val = 0
	for i in range(row_count):
		if len(input_list[i][position]) > temp_max_val:
			temp_max_val = len(input_list[i][position])
	
	return temp_max_val


def getAllMaxSpacing(input_list):
	spacing_list = []
	col_count = len(input_list[0])
	
	for i in range(col_count):
		spacing_list.append(getMaxSpacing(input_list,i))

	return spacing_list


def addSpacing(input_list,add_char = ' '):
	string_list = []
	spacing_list = getAllMaxSpacing(test_list)
	additional_spacing = add_char * 2 + ' '
	row_count =  len(input_list)
	col_count = len(input_list[0])

	for i in range(row_count):
		temp_string = ''
		first = True
		for j in range(col_count):
			if first:
				first = False
			else:
				temp_string += additional_spacing
			temp_val = input_list[i][j]
			temp_val_len = len(temp_val)
			if temp_val_len < spacing_list[j]:
				temp_string += temp_val + ' ' + add_char * (spacing_list[j] - temp_val_len)
			else:
				temp_string += temp_val + ' '
		string_list.append(temp_string)

	return string_list
			
			# print(f'{input_list[i][j]} has a length of {len(input_list[i][j])} compared to {spacing_list[j]}')


# print(getAllMaxSpacing(test_list))

print(addSpacing(test_list,'-'))


# apple--banana--carrot---
# date---egg-----fruitcake

# apple  banana  carrot
# date   egg     fruitcake

'''
apple -- banana -- carrot ---
date --- egg ----- fruitcake 
'''
