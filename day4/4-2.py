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

for i in passports:
	if (i.find("byr:")!=-1):
		record[0]=1
	if (i.find("iyr:")!=-1):
		record[1]=1
	if (i.find("eyr:")!=-1):
		record[2]=1
	if (i.find("hgt:")!=-1):
		record[3]=1
	if (i.find("hcl:")!=-1):
		record[4]=1
	if (i.find("ecl:")!=-1):
		record[5]=1
	if (i.find("pid:")!=-1):
		record[6]=1
	if (i==''):
		if (sum(record)==7):
			valid+=1
		record=[0,0,0,0,0,0,0]
		
if (sum(record)==7): #peedeejaa rindinja nav ''
	valid+=1
print valid
	
	
