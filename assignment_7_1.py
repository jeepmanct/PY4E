# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
#
for data in fh:
	data = data.rstrip().upper()
	print (data)
  
