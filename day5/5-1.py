fails = open('input5.txt', 'r')
passes=fails.read().splitlines()
row=0
col=0
sid=0
oldsid=0

for bp in passes:
	for i in range(0,7):
		if (bp[i]=="B"): row+=2**(6-i)
	for i in range(7,10):
		if (bp[i]=="R"): col+=2**(9-i)
	sid=row*8+col
	row=0
	col=0

	if (sid>oldsid):
		oldsid=sid
		sid=0
print oldsid
	
		
