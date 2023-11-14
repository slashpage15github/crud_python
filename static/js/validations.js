var pattern=/^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;
var pattern2=/^[a-zA-Z ]{3,30}?$/;
var pattern3=/^[0-9]{10}?$/;
var emailPattern =/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

let valida_aspirante = () =>{


    let js_rfc=getTextInputById("f_rfc");
	  let js_nom=getTextInputById("f_nombre");
	  let js_pat=getTextInputById("f_paterno");
	  let js_mat=getTextInputById("f_materno");
	  let js_emp=getTextInputById("f_id_empresa");
	  let js_tel=getTextInputById("f_telefono");
	  let js_ema=getTextInputById("f_email");
	  let js_cur=getTextInputById("f_id_curso");



    if (js_rfc.length==0){
        mensaje('error','Error en RFC','El dato RFC no puede is vacío!','<a href="">Necesita ayuda?</a>');
        return false;
    }
    else if (!pattern.test(js_rfc)){
        mensaje('error','Error en RFC','El dato RFC no cumple el formato! ejemplo:PETD741512R45','<a href="https://www.sat.gob.mx/home">Necesita ayuda?</a>');
      return false;
    }
    else if (js_nom.length==0){
      mensaje('error','Error en Nombre','El dato Nombre no puede is vacío!',null);
      return false;
    }
    else if (js_nom.length<3){
      mensaje('error','Error en Nombre','El dato Nombre no cumple el formato, pocos caracteres!','<a href="">Necesita ayuda?</a>');
      return false;
    }    
    else if (js_pat.length==0){
      mensaje('error','Error en Paterno','El dato Paterno no puede is vacío!',null);
      return false;
    }
    else if (js_pat.length<3){
      mensaje('error','Error en Paterno','El dato Paterno no cumple el formato, pocos caracteres!','<a href="">Necesita ayuda?</a>');
      return false;
    }    
    else if (js_mat.length==0){
      mensaje('error','Error en Materno','El dato Materno no puede is vacío!',null);
      return false;
    }
    else if (js_mat.length<3){
      mensaje('error','Error en Materno','El dato Materno no cumple el formato, pocos caracteres!','<a href="">Necesita ayuda?</a>');
      return false;
    }    
    else if (js_emp==0){
      mensaje('error','Error en Empresa','Seleccione una empresa de la lista!',null);
      return false;
  }
  else if (js_tel==0){
    mensaje('error','Error en Telefono','Telefono no pude ir vacio!',null);
    return false;
  }
  else if (js_ema==0){
    mensaje('error','Error en Email','Email no pude ir vacio!',null);
    return false;
  }
  else if (js_cur==0){
    mensaje('error','Error en curso','Seleccione un curso de la lista!',null);
    return false;
  }
  else if (!pattern3.test(js_tel)){
    mensaje('error','Error en Telefono','Telefono solo acepta números! ejemplo:8442722698',null);
    return false;
  }
  else if (!pattern2.test(js_nom) || !pattern2.test(js_pat) || !pattern2.test(js_mat)){
    mensaje('error','Error en Nombre completo','Nombre, paterno y materno, no acepta números',null);
    return false;    
  }
  else if(!emailPattern.test(js_ema)){
    mensaje('error','Error en email','email no cumple el formato, ejemplo:algo@dominio.edu.mx',null);
    return false;    
  }
}

/* function mensaje(tipo,titulo,texto,liga){
  Swal.fire({
    type: tipo,
    title: titulo,
    text: texto,
    footer: liga
  });
} */

let mensaje = (tipo,titulo,texto,liga) =>{
  Swal.fire({
    type: tipo,
    title: titulo,
    text: texto,
    footer: liga
  });
}


let getTextInputById = (id) => {
  return document.getElementById(id).value.trim();
}

function valida_login(){
	var js_us=document.getElementById("f_user").value.trim();
	var js_pw=document.getElementById("f_pwd").value.trim();

	//alert(js_us+' -  '+js_pw);
	if (js_us.length==0 || js_pw.length==0){
		Swal.fire({
  			type: 'error',
  			title: 'Usuario y password',
  			text: 'El usuario y password no debe ir vacios'
			}); 
		return  false;
	}
	else if(js_us.length<8 || js_pw.length<8){
		Swal.fire({
  			typen: 'error',
  			title: 'Usuario y password',
  			text: 'El usuario y password deben contener al menos 8 caracteres'
			}); 
		return  false;

	}
	else if (!pwdpattern.test(js_pw)){
			Swal.fire({
  			type: 'error',
  			title: 'Password Inseguro',
            html: 'Condiciones: <br>1] Min 1 special character.<br>2] Min 1 number.<br>3] Min 8 characters or More'
			});	        
        return false;
    }

}
