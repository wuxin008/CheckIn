from flask import Flask, render_template, request, redirect
import _thread
import time
from SendEmail import Mail
import json
import checkin_self

app = Flask(__name__)
Email = Mail('smtp.163.com', 'xl20210613@163.com', 'YLCYZGMGFZBTLTWH', 'xl20210613@163.com', ['xl20210613@163.com'])

def sendEmail():
    print('start to send')
    cnt = 0
    while cnt < 5:
        cnt += 1
        Email.send('This is a test Email', 'lalala')
        time.sleep(10)
        print('has sended')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/<args>', methods=['POST', 'PUT'])
def api(args):
    if request.method == 'POST':
        data = request.form.to_dict()

        if args == 'SendEmail':
            _thread.start_new_thread(sendEmail, ())
        if args == 'CheckInSelf':
            cookies = checkin_self.getCookies()
            return json.dumps(checkin_self.checkin(cookies))

        return json.dumps('button has been clicked.')
    elif request.method == 'GET':
        return redirect('error')

if __name__ == "__main__":
    app.run(debug=True)