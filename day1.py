def gcd_sub(a, b):
	while a * b != 0:
		if a > b :
			a = a-b
		else:
			b = b-a
	return a+b

def gcd_mod(a, b):
	while a * b != 0:
		if a > b:
			a = a%b
		else:
			b = b%a
	return a+b

def gcd_rec(a, b):
	if(b ==0):
		return a
	else:
		return gcd_rec(b,a%b)
		
# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
a,b = input().split(" ")

x = gcd_sub(int(a),int(b))
y = gcd_mod(int(a),int(b))
z = gcd_rec(int(a),int(b))
print(x, y, z)