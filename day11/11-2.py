import numpy as np 
import copy
fails = open('input.txt', 'r')
inp=fails.readlines()
playfieldLen=len(inp)
playfieldWid=len(inp[1])-1 #jo beidzas ar /n
playfield=np.zeros([playfieldLen, playfieldWid,] , dtype=np.int8)
newPlayfield=np.zeros([playfieldLen, playfieldWid] , dtype=np.int8)

def checkSeat(ix,iy):
	seat=0
	for x in range(ix-1, ix+2):
		for y in range(iy-1, iy+2):
			if (x>=0) and (y>=0) and (x<playfieldWid) and (y<playfieldLen):
				if ((ix!=x) or (iy!=y)):
					if (playfield[y,x] > 0):
						seat+=1
	if (seat>=4): 
		newPlayfield[iy,ix]=0
	elif (seat==0):
		newPlayfield[iy,ix]=1
	return seat

#fill initial array
for y in range (0, playfieldLen):
	for x in range (0, playfieldWid):
		if (inp[y][x]=="L"):
			playfield[y,x]=0
		if (inp[y][x]=="."):
			playfield[y,x]=-1

#fill new state array because we aren't changing all elements in checkSeat()
newPlayfield=copy.deepcopy(playfield)

#compute next iteration
while (1):	
	for y in range(0,playfieldLen):
		for x in range (0,playfieldWid):
			if (playfield[y,x]>=0): 
				checkSeat(x,y)
				
	if (np.array_equal(playfield, newPlayfield)): break
	playfield=copy.deepcopy(newPlayfield)
	#print newPlayfield
	
	
print "result:"
print newPlayfield[newPlayfield>0].sum()

	


