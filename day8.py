print("What game \"should\" I make today?")
# f-string (String format)
"""user_name = input()
age = input()
greeting_msg_formatted = f"Hello, {user_name}. Your age is {age} years old."
print(greeting_msg_formatted)
"""
# splitting
#c = "I love lovers."
#print(c.split()) # In the bracket, you can choose what to be split by.
# in / not in
s = "I love peacock!"
#print("o" in s) # Capital letters are different.
# String loop
#print(s.replace("pea", "huge ").replace("love", "suck"))
# string loop
# 1. loop by characters
# 2. loop by index
"""
for i in range(10, len(s)):
    print(s[i].upper())
"""
# 3. Enumerate || gives both character and index || the first one is index.
"""
for i, char in enumerate(s):
    print(i, char)
"""
string = input()
new_string = ""
for i in range(len(string)-1):
    new_string += string[i] + "_"
print(new_string + string[-1])