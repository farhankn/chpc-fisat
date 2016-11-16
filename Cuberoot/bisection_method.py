num = raw_input('Enter the num : ' )
num =  float(num)
epsilon = 0.00001
low =0.0
high = max(1.0,num)
mid = (low+high)/2.0
while (abs(mid**3-num)>=epsilon):
    if mid**3<num:
        low = mid
    else:
        high = mid
    mid =(low+high)/2.0
print 'The cube root of '+ str(num) +' is '+ str(mid)
