from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/bataan")
def bataan():
   return render_template("bataan.html")

@app.route("/bulacan")
def bulacan():
   return render_template("bulacan.html")

@app.route("/nuevaecija")
def nuevaecija():
   return render_template("nuevaecija.html")

@app.route("/pampanga")
def pampanga():
   return render_template("pampanga.html")

@app.route("/tarlac")
def tarlac():
   return render_template("tarlac.html")

@app.route("/zambales")
def zambales():
   return render_template("zambales.html")


if __name__ == "__main__":
   app.run()