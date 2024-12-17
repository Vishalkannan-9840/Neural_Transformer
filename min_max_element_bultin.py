def minimum(a, n):
	mini = a.index(min(a))

	maxi= a.index(max(a))

	print("The maximum is at position", maxi + 1)
	print("The minimum is at position", mini + 1)

a = [3, 4, 1, 3, 4, 5]
minimum(a, len(a))
