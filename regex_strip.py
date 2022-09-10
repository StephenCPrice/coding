'''Regex Version of the strip() Method
Write a function that takes a string and does the same thing 
as the strip() string method. If no other arguments are passed 
other than the string to strip, then whitespace characters will 
be removed from the beginning and end of the string. Otherwise, 
the characters specified in the second argument to the function 
will be removed from the string.'''

import re
print(f'what text would you like to be stripped from?')
user_text= input()
print(f'What character would you like to strip from the text?')
stripped_char = input()
def regex_strip(text, charr): 
    print(re.sub(charr, '', text, flags=re.I))
regex_strip(user_text, stripped_char)