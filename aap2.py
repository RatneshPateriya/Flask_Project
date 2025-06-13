from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')  # ❌ removed extra space here

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact")  # ❌ fixed typo in route: was "/contcat"
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
