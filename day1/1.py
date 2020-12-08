fails = open("input1.txt", "r")
input = fails.readlines()
l=len(input)

for i in range(l):
	for k in range(i,l):
		if (2020 - int(input[i])-int(input[k]))==0:
			print int(input[i])*int(input[k])

