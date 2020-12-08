fails = open('input4.txt', 'r')
passports=fails.read().splitlines()
valid=0
record=[
0,#byr 0
0,#iyr 1
0,#eyr 2
0,#hgt 3
0,#hcl 4
0,#ecl 5
0] #pid 6

def checkByr(byr):
	if (1920<=byr<=2002):
		return 1
	else:
		return 0
		
def checkIyr(iyr):
	


#for i in passports:
#	line = i.split()
#	for z in line:
#		print z
	
#print valid
	
	
