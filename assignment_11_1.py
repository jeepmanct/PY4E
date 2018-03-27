name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_55624.txt"
handle = open(name)
import re

data=list()

for line in handle:
     find = re.findall('[0-9]+',line)
     data = data + find

sum=0
for number in data:

    sum = sum + int(number)

print(sum)
