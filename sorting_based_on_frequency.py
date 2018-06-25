'''
Problem statement: Given an array sort that array in a fashion that
1. The number with the highest frequecy comes first.
2. If there are multiple numbers with the same frequency (>= 2) then they should be sorted in descending order.
3. If there are multiple numbers with frequency = 1 then they should get sorted in ascending order.
4. numbers with frequency >= 2 should come before the numbers with frequency 1.

All the numbers are no-negative integers.

Sample Input1: [3, 1, 2, 5, 7, 5, 7, 2, 5, 4, 4, 4, 7, 0]
Sample Output1: [7, 7, 7, 5, 5, 5, 4, 4, 4, 2, 2, 0, 1, 3]

Sample Input: [3, 1, 2, 5, 5, 7, 2, 5, 4, 4, 4, 7, 0]
Sample Output: [5, 5, 5, 4, 4, 4, 7, 7, 2, 2, 0, 1, 3]


'''
a = [1,6,3,4,5,6,7,7,4,6]

count_sort = []
temp = []
output = []

# count sort
for i in range(0,len(a)+1): 
	count_sort.append(0)

for i in a:
	count_sort[i] = count_sort[i] + 1

is_max_count_one = False
max_prev = 0

# _ means nothing.
for _ in range(0, len(a)-1):
	
	prev_flag = True
	max_count = max(count_sort)
	max_index = count_sort.index(max_count)

	# This 'if' takes care of ascending and decending order.
	# 'temp' contains list of numbers in ascending order having same max count. e.g. [5,5,5] or [2,2,7,7] 
	if max_prev != max_count:
		if is_max_count_one == False:
			output = output+temp[::-1]
			temp = []
		else:
			output = output+temp
			temp = []

	if max_count == 1:
		is_max_count_one = True

	# Here we are populating the temporary list (temp)
	# Moreover, we are making max_count = 0 so that in the next iteration new max will be chosen.
	for j in range(0, max_count):
		if prev_flag:
			max_prev = max_count
			prev_flag = False
		temp.append(max_index)
		count_sort[max_index] -= 1

print(output)
