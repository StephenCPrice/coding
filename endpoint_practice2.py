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
            if file == queried_file: 
                correct_file = json_path + '/' + file     
                break

            elif file == (os.listdir(json_path))[-1]: #If at the final iteration of the loop, and it is not a json file return a 404 error.
                return flask.abort(404)
    except:
        return flask.abort(404)                             

#replaces text with itself.
    try:
        with open(correct_file, 'r') as filee:
            f = filee.read()  
        with open(correct_file, 'w') as files:
            files.write(f)  
    except:
        return flask.abort(404)

     

    return correct_file                              

app.run()