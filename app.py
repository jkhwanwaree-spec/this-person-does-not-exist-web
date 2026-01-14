from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    image_url = "https://thispersondoesnotexist.com/image"
    return render_template("index.html", image_url=image_url)
