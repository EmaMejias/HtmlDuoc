$(function(){ 
    $("#formulario").validate({ 
        rules:{
            idProducto: "required",
            nombreProducto: "required",
            precio: "required",
            stock: "required",
            categoria: "required",
            imagen: "required",
        },
        messages:{
            idProducto:{
                required: 'Ingrese un ID para este producto'
            },
            nombreProducto:{
                required:'Ingrese un nombre para este producto'
            },
            precio:{
                required:'Ingrese un precio para este producto'
            },
            stock:{
                required:'Ingrese el stock actual del producto'
            },
            categoria:{
                required:'Ingrese una categoria para este producto'
            },
            imagen:{
                required:'Seleccione una imagen para este producto'
            }

        }

    })



});