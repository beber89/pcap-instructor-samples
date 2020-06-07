class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
    pass
	# put your code here

class FileEmpty(StudentsDataException):
    pass
	# put your code here

with open("student_grades.txt", 'r') as fo:
    data = fo.read()

for firstname, lastname, mark in map(lambda s: s.split(), data.split('\n')):
    print(firstname)
    print(lastname)
    print(mark)

