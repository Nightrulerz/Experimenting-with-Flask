from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
'''
For using a session, one must set a secret key
'''
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
greetings = [
    "Hello",
    "Hi",
    "Hey",
    "Good day",
    "Welcome"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_name', methods=["GET"])
def get_name():
    if request.method == 'GET':
        name = request.args['username']
        if not 'message' in session:
            session['message'] = greetings[0]
        message = random_greetings(session)
        return render_template('greeting.html', greetings=f"{message} {name}")
    else:
        return render_template('index.html')

def random_greetings(session):
    random.shuffle(greetings)
    raw_greeting = greetings[0]
    if session['message'] != raw_greeting:
        session['message'] = raw_greeting
    else:
        raw_greeting = greetings[1]
        session['message'] = raw_greeting
    return raw_greeting


if __name__ == "__main__":
    app.run(debug=True)