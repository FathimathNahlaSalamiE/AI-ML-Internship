string = "hello world"

#1
rev = string[::-1]
print(rev)

#2
result = "".join(string.split())
print(result)

#3
if string == string[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")

#4
print(string.replace("world","worlds"))

#5
vowels = "aeiou"
print(len([i for i in string.lower() if i in vowels]))