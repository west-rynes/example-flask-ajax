from flask import Flask, jsonify, render_template, request
import time
import numpy as np
app = Flask(__name__)

# See http://flask.pocoo.org/docs/0.10/patterns/jquery/

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/ctime')
def ctime():
    #print "got ctime request"
    return jsonify(result=time.asctime(), array=list(np.random.randint(0,100, size=50)))
    #return time.ctime()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(threaded=True)

