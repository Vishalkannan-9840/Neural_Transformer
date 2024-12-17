x = [8, 1, 7, 10, 5]
minimum=x[0]
maximum=x[0]
for i in range(1, len(x)):
	if x[i] < minimum:
		minimum = x[i]
		
	if x[i] > maximum:
		maximum = x[i]
		
print('Minimum Element in the list', x, 'is', minimum)
print('Maximum Element in the list', x, 'is', maximum)
