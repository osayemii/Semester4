from flask import Flask, redirect, url_for
app = Flask(__name__)
welcome = "Welcome to the Department of Computer Science Library. You have logged in as "

@app.route('/guest/<gid>')
def fun_guest(gid):
    return "%s Guest with id: %s" %(welcome, gid)

@app.route('/student/<sid>')
def fun_student(sid):
    return "%s Student with id: %s" %(welcome, sid)

@app.route('/faculty/<fid>')
def fun_faculty(fid):
    return "%s Faculty with id: %s" %(welcome, fid)

@app.route('/library/<login>/<id>')
def fun_library(login, id):
    if login == 'guest':
        return redirect(url_for('fun_gue', gid=id))
    elif login == 'student':
        return redirect(url_for('fun_stud', sid=id))
    elif login == 'faculty':
        return redirect(url_for('fun_fac', fid=id))
    else:
        return "Invalid login type"
if __name__ == '__main__':
    app.run(port=2207, debug = True)