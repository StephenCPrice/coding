import flask, os, json
from pathlib import Path
app = flask.Flask(__name__, static_folder='static')
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def catch():

    json_path = '/home/stephen/repos/coding/static'         #json_path = some_var to make it more automateable

    try:            
        for i, x in enumerate(os.listdir(json_path)):       #loop through files in the directory to find the FIRST one ending in .json
            y = Path(x)  #Path object 
            if y.suffix == '.json': 
                y = os.path.basename(y)                     #takes the basename of the Path object, and converts it into a string. I first tried doing abspath, but for some reason the path did not include /static/json.json. In hindsight perhaps because static_folder in app is set to static.
                correct_file = json_path + '/' + y          #I could append all .json files to a list and use some logic to try and find the most accurate file, but this fulfills the requirement you set I think.
                break
            elif x == (os.listdir(json_path))[-1] and y.suffix != '.json' : #If at the final iteration of the loop, and it is not a json file return a 404 error.
                return flask.abort(404)
    except:
        return flask.abort(404)                             #If there is an error for some reason return a 404
    
    p = open(correct_file)
    json_object = json.load(p)                              #json_object only has one key?
    p.close()

    back_to_the_json = json.dumps(str(json_object.items()).replace('.', ' '))

    return back_to_the_json                                 #I have no idea how to keep the original structure of the json file in the returned file, seems like it would make the function alot more complicated unless there is something i'm missing.

app.run()