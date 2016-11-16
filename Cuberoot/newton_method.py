num = input('Enter the number : ')
num =  float(num)
change = 0.000000001
guess=0.3*num
while ((abs(guess**3)-num)>change):
	fx = guess**3-num
	fxx = 3*(guess**2)
	guess = guess - (fx/fxx)
print guess
