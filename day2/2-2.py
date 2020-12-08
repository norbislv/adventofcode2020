fails = open("input2.txt", "r")
input = fails.readlines()
l=len(input)
valid=0

for i in range(l):
	element = input[i].split() 
	required = element[0].split("-")
	firstPos=int(required[0])-1
	secondPos=int(required[1])-1
	letter=element[1][0]
	elementCount=element[2].count(letter)

	if (element[2][firstPos]==letter) or (element[2][secondPos]==letter):
		if (element[2][firstPos] != element[2][secondPos]):
			valid+=1

print valid
