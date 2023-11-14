from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/aspirante")
def add_aspirante():
    return "agrega aspirante"

@app.route("/lista_cursos")
def lista_cursos():
    return "lista de cursos"

if __name__ == "__main__":
    app.run(debug=True)