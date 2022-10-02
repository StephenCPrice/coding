import json
import os
import shutil
import flask

from pathlib import Path
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def catch():
    changed_file = 'myfile.json'          #change to the same file name, so I don't have to keep going back and changing it every time to test it.
    json_path = '/home/stephen/repos/coding/static'         
    try:            
        for file in os.listdir(json_path):       
            y = Path(file) 
            if y.suffix == '.json': 
                y = os.path.basename(y)                
                correct_file = json_path + '/' + y     
                break
            elif file == (os.listdir(json_path))[-1]: 
                return flask.abort(404)
    except:
            return flask.abort(404)                             
    new_file = json_path + '/' + changed_file
    try:
        shutil.move(correct_file, new_file)           #Changes file name to newfile. 
    except:
        return flask.abort(404)
    return new_file                               

app.run()