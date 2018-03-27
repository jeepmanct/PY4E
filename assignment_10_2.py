name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mail = dict()
for line in handle :
    line = line.rstrip()
    #print(line)
    if line.startswith('From '):
		line=line.split()
		email = line[5]
		#print(email)
		email=email.split(":")
		#print(email)
		hour=email[0]
		mail[hour] = mail.get(hour,0) + 1
list = []
for hour, count in mail.items() :
	list.append( (hour, count) )
list.sort()
for hour, count in list :
	print (hour, count)
