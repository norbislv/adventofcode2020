import re
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

def chkByr(byr):
	if (1920<=byr<=2002): return 1
	else: return 0
		
def chkIyr(iyr):
	if (2010<=iyr<=2020): return 1
	else: return 0
		
def chkEyr(eyr):
	if (2020<=eyr<=2030): return 1
	else: return 0
		
def chkPid(pid):
	if (re.match('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',pid)): return 1
	else: return 0

def chkHcl(hcl):
	if (re.match('#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]',hcl)): return 1
	else: return 0

def chkEcl(ecl):
	if (re.match('amb|blu|brn|gry|grn|hzl|oth',ecl)):return 1
	else: return 0
	
def chkHgt(hgt):
	h=re.match('[0-9][0-9][0-9]cm',hgt)
	if h:
		n=re.findall('\\d+', hgt)
		if (150<=int(n[0])<=193):return 1
		else: return 0
	h=re.match('[0-9][0-9]in',hgt)
	if h:
		n=re.findall('\\d+', hgt)
		if (59<=int(n[0])<=76):return 1
		else: return 0
	else: return 0
	

	
for i in passports:
	line = i.split()
	if not i:
		if (sum(record)==7):
			valid+=1
			print "valid"
			print record
		print
		record=[0,0,0,0,0,0,0]
		
	for z in line:
		op = z.split(":")
		print op
		if op[0]=="byr": record[0]=chkByr(int(op[1]))
		if op[0]=="iyr": record[1]=chkIyr(int(op[1]))
		if op[0]=="eyr": record[2]=chkEyr(int(op[1]))
		if op[0]=="hgt": record[3]=chkHgt(op[1])
		if op[0]=="hcl": record[4]=chkHcl(op[1])
		if op[0]=="ecl": record[5]=chkEcl(op[1])
		if op[0]=="pid": record[6]=chkPid(op[1])
		
if (sum(record)==7): #peedeejaa rindinja nav ''
	valid+=1	
	print "valid"
	print record
	
	
print valid
	
	
