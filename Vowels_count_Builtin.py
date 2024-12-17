string = input("Enter any variables")
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
	print(count)
