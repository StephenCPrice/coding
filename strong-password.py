import re
password = input()                                                                          #asks for password
def password_checker(passs):                                                                #pass word strength checker
    password_check_len = re.compile(r'\w')                                                  #used later to check the total length of password
    password_check_cap = re.compile(r'[A-Z]')                                               #checks if there is at least one capital letter
    password_check_num = re.compile(r'[0-9]')                                               #checks if there is at least one number
    cap_result = password_check_cap.findall(passs)                                              
    num_result = password_check_num.findall(passs)                                          #findall matches and store to variable
    len_result = password_check_len.findall(passs)
    if len(len_result) >= 8 and len(cap_result) >= 1 and len(num_result) >= 1:              #does the check and prints result.
        print('Your password is sufficiently strong.')
    else: 
        print('Your password is not strong enough.')
password_checker(password)