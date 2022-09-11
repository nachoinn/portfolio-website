from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aVRIrQqYWjCh7qdBns6df6EDpsW3pckp'


@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)