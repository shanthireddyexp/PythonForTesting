#Concatination
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#Length of string
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

#String lower and upper cases
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#replace
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

#Split
text = "Python is awesome"
words = text.split()
print("Words:", words)

#String strip
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#Substring
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")