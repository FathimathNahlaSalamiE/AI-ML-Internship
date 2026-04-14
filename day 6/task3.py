a = "malayalam"

#1
print(a[::-1])

#2
if a == a[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#3
characters = {}
for i in a:
    characters[i] = characters.get(i,0)+1
print(characters)

#4
vowels = len([i for i in a.lower() if i in "aeiou"])
print(vowels)
consonants = len([i for i in a.lower() if i >= chr(97) and i <= chr(122)]) - vowels
print(consonants)