from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/')
def homepage():
    return render_template('welcome.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/service')
def service():
    return render_template('service.html')

if __name__ == "__main__":
    app.run(debug=True)