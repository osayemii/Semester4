from flask import Flask,render_template,request

app = Flask(__name__, template_folder="template")

@app.route('/')
def homepage():
    return render_template('welcome.html')

@app.route("/sessionDisplay", methods=['POST', 'GET'])
def fun_session():
    if request.method == 'POST':
        cs = request.form.get('cursession')
        return render_template('sessionDisplay.html', csession=cs)
    return render_template('sessionDisplay.html')
    
if __name__ == "__main__":
    app.run(debug=True)