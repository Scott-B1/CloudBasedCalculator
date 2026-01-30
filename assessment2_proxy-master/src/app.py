from flask import Flask
from flask import request
from flask import Response
import json
import requests

app = Flask(__name__)


saved_num = dict()

def add_dict(data): #stateful saving to a dictionary
    saved_num[len(saved_num)]= int(data) #save a num passed in to a 1 based index length
    return str(len(saved_num)-1) #return length-1 to prevent out of bounds for search

def search_dict(data): #stateful searching from a dictionary
    if int(data) in saved_num: #if data is present
        x = saved_num[int(data)] #get data abd return
        return str(x)
    else:
        return str(0) #else return 0

def get_FunctionPath(operator): #pass in a function path, if it matches return the link, otherwise return "Invalid Function URL"
    with open('src/urls.json', 'r') as f:
        data = json.load(f) #Load in the data as json

        switcher = { #switch statement for each possible function
        "add": data["add"],
        "subtract": data["subtract"],
        "multiply": data["multiply"],
        "square": data["square"],
        "divide": data["divide"],
        "modulo": data["modulo"],
        "add2": data["add2"],
        "subtract2": data["subtract2"],
        "multiply2": data["multiply2"],
        "square2": data["square2"],
        "divide2": data["divide2"],
        "modulo2": data["modulo2"],
        }
    return switcher.get(operator, "Invalid Function URL")

@app.route('/')
def index():
    try:
        x = request.args.get('x') #get the arguments, pass in the operator to get from the switch function

        if 'operator' in request.args:
            functionOperator = request.args.get('operator')
            functionURL = get_FunctionPath(functionOperator)

        if functionOperator == "save": #Stateful Saving of Current Value
            reply = add_dict(x)
        elif functionOperator == "load": #Stateful loading of current value
            reply = search_dict(x)
        else:
            reply = requests.get(functionURL + '?x=' + '1' + '&y=' + '1') #C2, test with fake data to see if the url is up
            if reply.status_code != 200: #if we do not get a 200 response
                functionURL = get_FunctionPath(functionOperator+'2') #re-route to the backup address


            if 'y' in request.args: #if we have a function which uses two inputs get y and pass it through
                y = request.args.get('y')
                reply = requests.get(functionURL + '?x=' + x + '&y=' + y)
            else: #else pass in just x (e.g. for squaring)
                reply = requests.get(functionURL + '?x=' + x)

        r = Response(response=reply, status=200, mimetype="application/json")
        r.headers["Content-Type"]="application/json"
        r.headers["Access-Control-Allow-Origin"]="*"

        return r

    except: #if error, return generic error
        z = 0

        jdata = {
            "answer": z,
            "error": True
        }

        reply = json.dumps(jdata)
        r = Response(response=reply, status=200, mimetype="application/json")
        r.headers["Content-Type"]="application/json"
        r.headers["Access-Control-Allow-Origin"]="*"

        return r


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
