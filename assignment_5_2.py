largest = None
smallest = None
#
#
while True :
	try :
		num = input('Enter a number: ' )
		if num == 'done' : break
		cn = int(num)
#
		if largest < cn :
			largest = cn
		if smallest == None or smallest > cn :
			smallest = cn
	except:
		print('Invalid input')
#
print('Maximum is', largest)
print('Minimum is', smallest)
