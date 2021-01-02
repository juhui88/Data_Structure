import time, random

def sum(A, n):
	start = time.time()
	B = [[0 for col in range(n)] for row in range(n)]
	
	for j in range(n):
		for i in range(j+1):
			B[i][j] += A[i]
	
	print(time.time()-start) 

n = int(input("n값을 입력하시오(1이상 5000이하)\n"))
A = []
for i in range(n):
	k = random.randint(1,100)
	A.append(k)

sum(A,n)