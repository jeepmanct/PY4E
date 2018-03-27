name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

count = 0

mail = dict()
for line in fh:
	line.rstrip()
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		count = count + 1
		mail[email] = mail.get(email,0) + 1
count = None
for key in mail:
	if count is None or mail[key] > count:
		count = mail[key]
		efrom = key
print (efrom, count)
