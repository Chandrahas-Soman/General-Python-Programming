'''
Write a program that sorts a list of student last names, but the sort only uses the first two letters of the name. 
Nothing else in the name is used for sorting. Sorting is case sensitive and stable.

Input:

input consists of a sequence of up to 500 test cases. Each case starts with a line containing an integer 1 <= n <= 200.
After this follow n last names made up of letters, one name per line. Input ends when n = 0.

Output:

For each case, print the last names in sort of sorted order, one per line. Print a blank line between cases.
'''

import sys

sorted1 = []
count_list = []
argument_list = []

for x in sys.stdin:
	argument_list.append(x[:-1])

m = 0
while True:
	count_list.append(argument_list[m])
	if int(argument_list[m]) != 0:
		m = m + int(argument_list[m]) + 1
	else:
		break

p = 1
q = 0
for k in range(0,len(count_list)):
	if int(count_list[k]) == 0:
		break
	sorted1.append(argument_list[p])
	q = q + int(count_list[k])
	for i in range(p+1,q+1):
		sorted1.append(argument_list[i])
		for j in range(len(sorted1),1,-1):
			if sorted1[j-2][:2] <= sorted1[j-1][:2]:
				break
			else:
				temp = sorted1[j-1]
				sorted1[j-1] = sorted1[j-2]
				sorted1[j-2] = temp

	for lastname in sorted1:
		sys.stdout.write(lastname)
		sys.stdout.write("\n")
	
	if int(count_list[k+1]) != 0:
		sys.stdout.write("\n")
	p = p + int(count_list[k]) + 1
	q = q + 1
	sorted1 = []