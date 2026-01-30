from flask import Flask
from flask import request
from flask import Response
import json
import multiply

app = Flask(__name__)

@app.route('/')
def index():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        z = multiply.multiply(x,y)

        jdata = {
            "x" : x,
            "y" : y,
            "answer": z,
            "error": False
        }
        reply = json.dumps(jdata)

        r = Response(response=reply, status=200, mimetype="application/json")
        r.headers["Content-Type"]="application/json"
        r.headers["Access-Control-Allow-Origin"]="*"

        return r
    except:
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
