from flask import Flask, render_template

'''
It creates an instances of the Flask class,
which will be our WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route(rule=str("/"), methods=["GET", "POST"])
def index():
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True) # to restart the server automatically on saving the changes, just like nodemon