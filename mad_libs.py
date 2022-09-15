from pathlib import Path
import re
madlib_dict = {'ADJECTIVE' : '1', 'NOUN' : '1', 'ADVERB' : '1', 'VERB' : '1'}
def adjective(dict):
    for k, v in enumerate(dict):
        with open('/home/stephen/mad_libs_text.txt') as file:
            content = file.read()
            print(content)
            content = re.sub(list(dict)[k], dict[v], content)
    return content
print(type(madlib_dict))
print(adjective(madlib_dict))        
