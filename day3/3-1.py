fails = open('input3.txt', 'r')
forest=fails.read().splitlines()
platums = len(forest[1])
garums = len(forest)
x=0
y=0
tree=0

for y in range(1,garums):
	x+=3
	if (forest[y][x%platums]=='#'):
		tree+=1
print tree

