import json 
import os 
import flask 

from flask import Flask, request 
from pathlib import Path 

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def catch():
    json_path = './static'
    queried_file = request.args.get('file') #?file=myfile.json

    try:            
        for file in os.listdir(json_path):       
            if file.name == queried_file: 
                correct_file = json_path + '/' + file.name        
                break
            elif file == (os.listdir(json_path))[-1]: #If at the final iteration of the loop, and it is not a json file return a 404 error.
                return flask.abort(404)
    except:
        return flask.abort(404)                             #If there is an error for some reason return a 404
    try:
        p = open(correct_file)
        json_object = json.load(p)                              
        p.close()
    except:
        return flask.abort(404)

    back_to_the_json = json.dumps(str(json_object.items()).replace('.', ' '))

    return back_to_the_json                                 
app.run()
