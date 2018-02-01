# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


def last2(str) :
	
	count = 0
	for i in range (0 , len(str) -3):
		
		if str[i:i+2] == str[-2:]:
			count += 1

	print(count)

last2('edaxedxcded')
last2('hixxhi')
last2('xaxxaxaxx')
last2('axxxaaxx')