from flask import Flask, render_template,jsonify, request, url_for, flash, redirect
import model.package_model.aspirantes as aspirantes
import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso

import model.package_model.Empresa as Empresa
import model.package_model.Curso as Curso

import model.package_model.AspirantesCursos as AspirantesCursos

#import metodos static
from model.package_model.aspirantes import Aspirantes
from model.package_model.AspirantesCursos import AspirantesCursos
from datetime import datetime,date,time
#import metodos static
#from model.package_model.Curso import Curso
import jsonpickle
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j\x86\x14\xcc:\x99\xb3\x91\xf8/Bv\r\xaa"\xf1\x8a\xfa(A\xa1\xe2\x85\xd6'

@app.route("/delete_curso",methods=['POST'])
def delete_curso():
    _curso_id=request.form['id']
    cuantos_cursos=AspirantesCursos.existe_curso(_curso_id)
    if cuantos_cursos == 0:
        obj_cur= Curso.Curso()
        datos_curso=obj_cur.eliminar_curso(_curso_id)
        return str(datos_curso)
    else:
        return "-1"
    


@app.route("/ver_detalle_curso",methods=['POST'])
def ver_detalle_curso():
    _curso_id=request.form['curso_id']
    obj_cur= Curso.Curso()
    datos_curso=obj_cur.obtener_curso_por_id(_curso_id)
    return render_template('ver_detalle_curso.html',datos_curso=datos_curso)
    #return str(res_cur)
    
@app.route("/ver_detalle_curso_data",methods=['POST'])
def ver_detalle_curso_data():
    _curso_id=request.form['curso_id']
    obj_cur= Curso.Curso()
    datos_curso=obj_cur.obtener_curso_por_id(_curso_id)
    data = { 
            "id" : datos_curso[0], 
            "nombre" : datos_curso[1],
            "fecha" : datos_curso[2], 
        } 
    return jsonify(data)
    #return str(datos_curso)    

@app.route("/add_curso",methods=['POST'])
def add_curso():
    _f_id=request.form['f_id']
    _f_nombre=request.form['f_nombre'].upper()
    _fec=datetime.now()
    if _f_id=='':
        obj_cur= Curso.Curso(_f_id,_f_nombre,_fec)
        res_cur=obj_cur.insertar_cursos(obj_cur)
        return str(res_cur)
    else:
        obj_cur= Curso.Curso(_f_id,_f_nombre,_fec)
        res_cur=obj_cur.update_cursos(obj_cur)
        return str(res_cur)
        
def datetime_handler(obj):
    if isinstance(obj, (datetime, date, time)):
        return str(obj)

@app.route("/valida_existe", methods=['GET','POST'])
def valida_aspirante():
    rfc=request.form['f_rfc'].upper()
    cuantos_aspiran=Aspirantes.existe_aspirante(rfc)
    return jsonpickle.encode(cuantos_aspiran)

@app.route("/get_aspirante", methods=['GET','POST'])
def get_aspirante():
    rfc=request.form['f_rfc'].upper()
    dato_aspirante=Aspirantes.obtener_aspirante_por_rfc(rfc)
    return json.dumps(dato_aspirante,default=datetime_handler)

@app.route("/valida_existe_rfc_curso", methods=['GET','POST'])
def valida_aspirante_rfc_curso():
    rfc=request.form['f_rfc'].upper()
    curso=request.form['f_id_curso']
    cuantos_aspirancursos=AspirantesCursos.existe_aspirantecursos(curso,rfc)
    return jsonpickle.encode(cuantos_aspirancursos)


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

@app.route("/registra",methods=['POST'])
def registra_aspirante():
    _rfc=request.form['f_rfc'].upper()
    _cur=request.form['f_id_curso']
    _fec=datetime.now()
    
    cuantos_aspiran=Aspirantes.existe_aspirante(_rfc)
    cuantos_aspirancursos=AspirantesCursos.existe_aspirantecursos(_cur,_rfc)
    if cuantos_aspiran==1:
        if cuantos_aspirancursos==1:
            flash(f"Aspirante y curso ya registrado","Error")
            return redirect(url_for('add_aspirante'))
        else:
            obj_aspcur=AspirantesCursos(_cur,_rfc,_fec)
            res_aspcur=obj_aspcur.insertar_aspirantecursos(obj_aspcur)
            flash(f"Curso agregado correctamente","success")
            return redirect(url_for('add_aspirante'))
    else:
        _nom=request.form['f_nombre'].upper()    
        _pat=request.form['f_paterno'].upper()    
        _mat=request.form['f_materno'].upper()    
        _emp=request.form['f_id_empresa']    
        _tel=request.form['f_telefono']    
        _ema=request.form['f_email']    
        _cur=request.form['f_id_curso']
        _fec=datetime.now()
        obj_asp= aspirantes.Aspirantes(_rfc,_nom,_pat,_mat,_emp,_tel,_ema,_fec)
        res=obj_asp.insertar_aspirante(obj_asp)
        
        obj_aspcur=AspirantesCursos(_cur,_rfc,_fec)
        res_aspcur=obj_aspcur.insertar_aspirantecursos(obj_aspcur)

        #return _rfc+'-'+_nom+'-'+_pat+'-'+_mat+'-'+_emp+'-'+_tel+'-'+_ema+'-'+_cur
        flash(f"Aspirante y curso registrado correctamente","success")
        return redirect(url_for('add_aspirante'))  
        #return render_template('aspirante.html')
        #return res
        
@app.route("/lista_cursos")
def lista_cursos():
    obj_cur= Curso.Curso()
    lista_cursos = obj_cur.obtener_cursos()
    return render_template('lista_cursos.html',lista_cursos=lista_cursos)

if __name__ == "__main__":
    app.run(debug=True)