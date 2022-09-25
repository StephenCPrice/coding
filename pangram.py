letters = 'abcdefghijklmnopqrstuvwxyz'
letters_in_pangram = []
def is_pangram(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(letters)):

        if letters[i] in s:
            x = True
        elif letters[i] not in s:
            if letters[i].upper() in s:
                x = True
                continue
            else:
                x = False
            break
    return x
print(is_pangram('Cwm fjord bank glyphs vext quiz'))