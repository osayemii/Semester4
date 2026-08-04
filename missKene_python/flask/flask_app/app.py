from flask import Flask

app = Flask(__name__)

@app.route('/<sch_name>')
def fun_print(sch_name):
    return 'Welcome to our %s school' %sch_name

@app.route('/courses')
def course():
    return '<h1>Our Courses</h1> <ul><li>Python</li><li>Data Analytics</li>'

@app.route('/courses/<course_name>')
def classes(course_name):
    return 'Welcome to %s Lab' %course_name

if __name__ == '__main__':
    app.run(debug=True)