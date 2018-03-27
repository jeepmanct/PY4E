#empty list
lst = list()

fname = input("Enter file name: ")

try:
	fh = open(fname)

except:
	print("File Cannot be read...exiting", fname)
	quit()

#
#

for line in fh:

	#print(line)

	for word in line.split():

		if not word in lst:

			lst.append(word)

lst.sort()
print (lst)
