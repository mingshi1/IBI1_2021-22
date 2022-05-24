# Identify whether p=64 or not
# If p<64,
# keep calculating...
# If p=64,
# print the result.
n=0
p=1
sen=''
# determine the initial value of n and p
# define 'sen' as the sentence we finally get
while p<=64:
	p=(n**2+n+2)/2
	# find n with p
	sen=sen+str(n)+" "
	# add the result into the sentence
	n=n+1
	# repeat doing the process
print(sen)
