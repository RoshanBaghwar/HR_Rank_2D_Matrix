R, C = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()] for row in range(R)]
S = set()
for i in range(R):
	for j in range(C):
		S.add(arr[i][j])

D = dict()
rank = 1
for i in S:
	D[i] = rank
	rank += 1

newArr = []
for i in range(R):
	ar = []
	for j in range(C):
		ar.append(D[arr[i][j]])
	newArr.append(ar)

for i in newArr:
	for j in i:
		print(j, end = " ")
	print()