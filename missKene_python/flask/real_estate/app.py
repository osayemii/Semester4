from flask import Flask

app = Flask(__name__)

@app.route('/<company_name>')
def home(company_name):
    return "Welcome to my Real %s Marketing" % company_name

if __name__ == '__main__':
    app.run(host='localhost', port=2207, debug=True)