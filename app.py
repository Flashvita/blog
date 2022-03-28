from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/lk')
def base():
    return render_template('base.html')


@app.route('/lk/<string:name>/<int:id>')
def user(name, id):
    return "Personal lk: " + name + " :" + str(id) + "old"


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
