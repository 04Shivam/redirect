from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://localhost')

if __name__ == '__main__':
    app.run(debug=True)
