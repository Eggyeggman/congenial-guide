from flask import Flask, render_template
app = Flask(__name__)
@app.route("/index")
def first_page():
    return render_template('type.html')
app.run(debug = True)