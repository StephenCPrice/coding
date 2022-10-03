import json
import os 
import shutil 
import flask 

from pathlib import Path 
from flask import Flask, request 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def catch():
    json_path = './static'
    queried_file = request.args.get('file') #?file=myfile.json
    changed_file = 'myfile.json'   #same file for obv reasons     
    try:            
        for file in os.listdir(json_path): 
            print(file, queried_file)      
            if file == queried_file: 
                print(True)
                correct_file = json_path + '/' + file       
                break
            elif file == (os.listdir(json_path))[-1]: #If at the final iteration of the loop, and it is not a json file return a 404 error.
                return flask.abort(404)
    except:
        return flask.abort(404)                                         
    try:
        new_file = json_path + '/' + changed_file
        shutil.move(correct_file, new_file)           #Changes file name to newfile. 
    except:
        return flask.abort(404)
# open new_file, load json, and return to client.        
    f = open(new_file, 'r')
    new_file = json.load(f)
    f.close()

    return new_file                   

app.run()