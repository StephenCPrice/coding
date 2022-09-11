'''Regex Version of the strip() Method

Write a function that takes a string and does the same thing 
as the strip() string method. If no other arguments are passed 
other than the string to strip, then whitespace characters will 
be removed from the beginning and end of the string. Otherwise, 
the characters specified in the second argument to the function 
will be removed from the string.'''

import re
print(f'what text would you like to be stripped from?')
user_text = input()
print(f'What character would you like to strip from the text?')
stripped_char = input()
def regex_strip(text, charr):                           #"strips" the charr from left to right, and stops when it gets to a charr that isn't supposed to be stripped.
    lol = []                                            #function runs again after being reversed, and finally it is reversed again and then printed for the user.
    ambiguously_done = []
    for i in range(len(text)):
        if text[i] == charr:
            lol.append(re.sub(charr, '', text[i], flags=re.I))
        if text[i] != charr:
            lol.append(text[i:])
            ambiguously_done = (''.join(lol))
            break
    return ambiguously_done
reversed_user_text =  (regex_strip(user_text, stripped_char))[::-1]  
reversed_and_stripped = (regex_strip(str(reversed_user_text), stripped_char))[::-1]
print(rf'Your result is: {reversed_and_stripped}')