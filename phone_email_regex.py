import re, pyperclip

phone_regex = re.compile(r'''(
    (\d{3}) # Area Code
    (-|\s|\.) #seperator
    (\d{3}) # 3 middle numbers
    (-|\s|\.) # seperator
    (\d{4})   #4 final numbers
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username of email
    @ 
    [a-zA-Z0-9.-]+ #domain
    (\.[a-zA-Z]{2,5}) #.com/net/ect
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches, x = [], 0
for groups in phone_regex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in email_regex.findall(text):
       matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found.')