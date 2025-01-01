from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("https://github.com/Karthikkuncha45/HousePricePrediction/blob/main/original%20mini%20project/index.html")

if __name__ == "__main__":
    app.run(debug=True)
