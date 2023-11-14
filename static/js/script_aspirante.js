$(document).ready(function() {
    $("#f_rfc").blur(function(){
        let f_rfc=document.getElementById("f_rfc").value.trim().toUpperCase();
        //alert(f_rfc);
        if(f_rfc!= '')  
        {  
             $.ajax({  
                  url:'/valida_existe',  
                  method:'POST',  
                  data:{f_rfc:f_rfc},
                  success:function(response){
                         //alert(response);
                         //console.log(response)
                         if (response==1){
                            mensaje('warning','Aviso','El Aspirante ya tiene a menos 1 curso registrado!',null);
                         
                            /*BEGIN ajax para trae los datos del aspirante*/ 
                            /*END ajax para trae los datos del aspirante*/ 
                            $.ajax({  
                                url:'/get_aspirante',  
                                method:'POST',  
                                data:{f_rfc:f_rfc},
                                dataType: "json",
                                success:function(response){
                                        console.log(response);
                                        $('#f_nombre').val(response[2]);
                                        $('#f_paterno').val(response[3]);
                                        $('#f_materno').val(response[4]);
                                        $('#f_id_empresa').val(response[1]);
                                        $('#f_telefono').val(response[5]);
                                        $('#f_email').val(response[6]);
                                        $("#f_rfc ").attr("readonly", true); 
                                },
                               error : function(request, status, error) {
              
                                       var val = request.responseText;
                                       alert("error"+val);
                               }  
                           });  
                        
                        }  
                       
                  },
                 error : function(request, status, error) {

                         var val = request.responseText;
                         alert("error"+val);
                 }  
             });  
        }
        else{
            mensaje('error','No  llegó RFC','verificar RFC!',null);
        } 
        
      });


      $("#f_id_curso").change(function(){
        let f_id_curso=document.getElementById("f_id_curso").value;
        let f_rfc=document.getElementById("f_rfc").value.trim().toUpperCase();
        //alert(f_id_curso+'-'+f_rfc);
        
        if(f_rfc!= '' && f_id_curso!= '')  
        {  
             $.ajax({  
                  url:'/valida_existe_rfc_curso',  
                  method:'POST',  
                  data:{f_id_curso:f_id_curso,f_rfc:f_rfc},
                  success:function(response){
                         //alert(response);
                         //console.log(response)
                         if (response==1){
                            mensaje('warning','Aviso','El Aspirante ya tiene asignado el curso seleccionado!',null);
                         }  
                       
                  },
                 error : function(request, status, error) {

                         var val = request.responseText;
                         alert("error"+val);
                 }  
             });  
        }
        else{
            mensaje('error','No  llegó RFC ni ID_CURSO','verificar Datos!',null);
        } 
        
      });      
});