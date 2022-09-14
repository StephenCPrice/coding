#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# Save clipboard content.

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste() #Makes a new dictionary element with the clipboard contents as the value, and the sys.argv[2] as the key
    if sys.argv[1].lower() == 'delete': #if delete is entered with another argument present it will delete the dictionary element with the key sys.argv[2]
        if sys.argv[2].lower() in mcbShelf:
            del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'delete': #If the user inputs 'delete' without any other arguments all elements in the shelf dictionary are deleted.
        mcbShelf.clear()
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
print(list(mcbShelf))
mcbShelf.close()