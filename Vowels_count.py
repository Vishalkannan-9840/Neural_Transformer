h=input("Enter any variable: ")
count_vowels=0
h=h.lower()
for i in h:
  if i=='a' or i=='e' or i=='i' or i=='o' or i=='u': 
       count_vowels+=1
if count_vowels==0:
     print("there is no vowels")
else:
     print("number of the vowels present:",str(count_vowels))
