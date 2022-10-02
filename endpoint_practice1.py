import flask, os, json, shutil
from pathlib import Path
app = flask.Flask(__name__, static_folder='static')
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])

def catch():
    changed_file = 'myfile.json'          #changing to the same file name, so I don't have to keep going back and changing it every time to test it.
    json_path = '/home/stephen/repos/coding/static'         
    try:            
        for i, x in enumerate(os.listdir(json_path)):       
            y = Path(x)  #Path object 
            if y.suffix == '.json': 
                y = os.path.basename(y)                     
                correct_file = json_path + '/' + y          
                break
            elif x == (os.listdir(json_path))[-1] and y.suffix != '.json' : 
                return flask.abort(404)
    except:
        return flask.abort(404)                             
    new_file = json_path + '/' + changed_file

    shutil.move(correct_file, new_file)           #Changes file name to newfile while keeping the same file path. 

    return new_file                               

app.run()