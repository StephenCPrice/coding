import re, pyperclip

phone_regex = re.compile(r'''(
    (\d{3})
    (-|\s|\.)
    (\d{3})
    (-|\s|\.)
    (\d{4})   
    )''', re.VERBOSE)
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,5})
)''', re.VERBOSE)
mo = email_regex.search('stephencharlesprice@gmail.com')
print(mo.group())