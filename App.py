from flask import Flask, render_template, request, url_for, flash, redirect
import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/aspirante")
def add_aspirante():
        obj_emp= Empresa.Empresa()
        obj_cur= Curso.Curso()
        lista_empresas = obj_emp.obtener_empresas()
        lista_cursos = obj_cur.obtener_cursos()
        return render_template('aspirante.html',lista_empresas=lista_empresas,lista_cursos=lista_cursos)

@app.route("/lista_cursos")
def lista_cursos():
    return "lista de cursos"

if __name__ == "__main__":
    app.run(debug=True)