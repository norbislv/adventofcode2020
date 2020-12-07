fails = open('input3.txt', 'r')
forest=fails.read().splitlines()
platums = len(forest[1])
garums = len(forest)
x=[0,0,0,0,0]
y=0
tree=[0,0,0,0,0]
xslope=[1,3,5,7,1]
for y in range(1,garums):
	for i in range(0,4):
		x[i]+=xslope[i]
		if (forest[y][x[i]%platums]=='#'):
			tree[i]+=1
for y in range(2,garums,2):
	x[4]+=xslope[4]
	if (forest[y][x[4]%platums]=='#'):
		print (x[4]),
		print (y)
		tree[4]+=1
print tree
print tree[0]*tree[1]*tree[2]*tree[3]*tree[4]

