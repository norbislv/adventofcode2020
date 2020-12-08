fails = open("input2.txt", "r")
input = fails.readlines()
l=len(input)
valid=0

for i in range(l):
	element = input[i].split() 
	print element
	required = element[0].split("-")
	minimum=int(required[0])
	maximum=int(required[1])
	letter=element[1][0]
	print element[2].count(letter)
	print minimum, maximum, letter
	elementCount=element[2].count(letter)
	if (minimum<=elementCount) and (elementCount<=maximum):
		valid+=1

print valid
