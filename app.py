from flask import Flask, render_template, request, redirect
import _thread
import time
from SendEmail import Mail
import json

app = Flask(__name__)

email = Mail('smtp.163.com', 'xl20210613@163.com', 'YLCYZGMGFZBTLTWH', 'xl20210613@163.com', ['xl20210613@163.com'])

def sendEmail():
    cnt = 0
    while cnt < 5:
        cnt += 1
        email.send('This is a test Email', 'lalala')
        time.sleep(10)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/<args>', methods=['POST', 'PUT'])
def api(args):
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return json.dumps(data)
    elif request.method == 'GET':
        return redirect('error')

app.run(debug=True)