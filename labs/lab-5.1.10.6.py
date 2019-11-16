def fromDigitTo7Seg(digit):
	return {'0': "###\n# #\n# #\n# #\n###",\
		'1': "  #\n  #\n  #\n  #\n  #",\
		'2': "###\n  #\n###\n#  \n###",\
		'3': "###\n  #\n###\n  #\n###"}[digit]

def fromNumTo7Seg(num):
	lst = list(num)
	lst = map(lambda x: fromDigitTo7Seg(x), lst)
	lst = [l.split('\n') for l in lst]

	l = []
	for i in range(5): 
		l.append([lst[j][i] for j in range(len(lst))])
	l = map(lambda x: " ".join(x), l)
	for x in l:
		print (x)
	
# print(fromDigitTo7Seg('0'))
# print(fromDigitTo7Seg('1'))
# print(fromDigitTo7Seg('2'))
# print(fromDigitTo7Seg('3'))
fromNumTo7Seg('123')