from flask import Flask, render_template, request

app = Flask(__name__)

@app.route(rule=str("/"), methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    else:
        return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template('success.html', result=res)


if __name__=="__main__":
    app.run(debug=True) # to restart the server automatically on saving the changes, just like nodemon