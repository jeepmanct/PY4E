# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
#validate file
try:
	fh = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
#
#
# Define Variables
#
#
avg=0
counter=0
total=0
#
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    counter = counter + 1
    conf = float(line[21:])
    total=conf + total
avg = total / counter

print('Average spam confidence:', avg)
