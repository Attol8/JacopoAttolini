from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
