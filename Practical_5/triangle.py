# Determine whether i>10 or not,
# if i<10,
# 	i=i+1
# elif i=10
# 	done.stop.
n=1
Sum=0
# determine the initial value of i and sum
for i in range(0,10):
	Sum=Sum+n
	n=n+1
	print(Sum)
# Another way
x=1
# determine initial value of x
for b in range(0,10):
     a=range(0,x+1)
     print(sum(a,0))
     x+=1

