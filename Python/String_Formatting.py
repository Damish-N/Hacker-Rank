# n=int(input())
# print(n)

# for i in range(1,n+1):
# 	print(i)
def print_formatted(number):
	# print(number)
	# for i in range(1,number+1):
	# 	print("{} {} {} {}".format(i,oct(i)[2:],hex(i)[2:],bin(i)[2:]))
		# print(bin(i)[2:])
	n=number;
	w = len("{0:b}".format(n))
	for i in range(1,n+1):
  		print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
