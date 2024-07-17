$(function(){
    $("#reg_cliente").validate({ 
        rules:{
            nom:{
                required:true
            },
            correo:{
                required:true, 
                email:true
            },
            telefono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            },
            pass1:{
                required:true
            },
            pass2:{
                required:true,
                equalTo:'#pass1'
            },
            email:{
                required:true, 
                email:true
            },
            pwd:{
                required:true
            }
        },//fin rules
        messages:{
            nom:{
                required:'Ingrese su nombre..',
                minlength:'Caracteres insuficientes..(3)'
            },
            correo:{
                required:'Ingrese su correo electronico',
                email:'Formato de correo invalido'
            },
            telefono:{
                required:'Ingrese su telefono',
                number:'Telefono invalido',
                minlength:'Digitos insuficientes',
                maxlength:'Telefono invalido'
            },
            fecha:{
                required:'Seleccione la fecha',
                min:'Fecha de ingreso no valida'
            },
            pass1:{
                required:'Ingrese su contraseña',
                minlength:'Ingrese una password valida'
            },
            pass2:{
                required:'Reingrese su contraseña',
                minlength:'Caracteres insuficientes',
                equalTo:'Contraseñas no coinciden'
            },
            email:{
                required:'Ingrese su correo electronico',
                email:'Formato de correo invalido'
            },
            pwd:{
                required:'Ingrese su contraseña',
                minlength:'Ingrese una password valida'
            }
        }//fin messages
    });
})// fin function