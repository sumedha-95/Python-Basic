#Paper Number 0
#IT 20643218 - B.M.S.L.Bandaranayaka

# recursive function to calculate
# multiplication of two numbers
x= int(input("Enter Number X: "))
y= int(input("Enter Number Y: "))

def product( x , y ):
	# if x is less than y swap
	# the numbers
	if x < y:
		return product(y, x)
	
	# iteratively calculate y
	# times sum of x
	elif y != 0:
		return (x + product(x, y - 1))
	
	# if any of the two numbers is
	# zero return zero
	else:
		return 0
	    
result =(product(x, y))
print("Answer is :" , str(result))

