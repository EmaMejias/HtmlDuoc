$(function(){
    $("#login").validate({ 
        rules:{
            email:{
                required:true, 
                email:true
            },
            pwd:{
                required:true
            }
        },
        messages:{
            email:{
                required:'Ingrese su correo electronico',
                email:'Formato de correo invalido'
            },
            pwd:{
                required:'Ingrese su contraseña',
                minlength:'Ingrese una password valida'
            }
        }
    });
})// fin function