from flask import Flask , render_template
app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("first.html")

@app.route("/ram")
def rp():
        name="brajendra pateriya"
        return render_template("index.html",name2=name)
app.run(debug=True)