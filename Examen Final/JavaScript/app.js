var nombre = document.getElementById("nombre");
var password = document.getElementById("password");
var error = document.getElementById("error");

    // URL de la api

const apiUrl = 'https://api.thedogapi.com/v1/images/search'

    //Obtener el boton y contenedor
    
    const btnCat = document.querySelector('#btn-cat');
    const catImgContainer = document.querySelector('#cat-img-container');
    
    //Escuchar el click del boton
    
    btnCat.addEventListener('click', () => {
        //Llamar api
        fetch(apiUrl)
        //Convertir la respuesta a json
        .then(response => response.json())
        .then(data => {
            //Obtener urlde la imagen de la mascota
            const catImgUrl = data[0].url;
    
            //Agregar la imagen como backgroud del contenedor
    
            catImgContainer.style.backgroundImage =`url('${catImgUrl}')`;
    
        })
        .catch(error => console.log(error));
    })

//METODO 2
var form = document.getElementById('formulario');
    form.addEventListener('submit', function(evt){
        evt.preventDefault();
        var mensajesError = [];
        if(rut.value === null || rut.value === ''){
            mensajesError.push('Ingresa tu rut');
        }
    
        if(apellidos.value === null || apellidos.value === ''){
            mensajesError.push('Ingresa tus apellidos');
        }

        if(nombre.value === null || nombre.value === ''){
            mensajesError.push('Ingresa tu nombre');
        }
    
        if(email.value === null || email.value === ''){
            mensajesError.push('Ingresa un correo');
        }

        if(celular.value === null || celular.value === ''){
            mensajesError.push('Ingresa un numero de celular');
        }
    
    
        error.innerHTML = mensajesError.join(', ');
    });


// Funcion para mantener navbar fija
    window.onscroll = function() {navbarTop()};

    var navbar = document.getElementById('navbar');
    var navbarPlaceholder = document.getElementById('navbar-placeholder');

// Obtén la altura de la barra de navegación
    var navbarHeight = navbar.offsetHeight;

// Establece la altura del placeholder
    navbarPlaceholder.style.height = navbarHeight + 'px';

// Obtén la posición offset de la barra de navegación
    var sticky = navbar.offsetTop;

// Agrega o quita la clase sticky y muestra/oculta el placeholder
    function navbarTop() {
    if (window.scrollY >= sticky) {
        navbar.classList.add("sticky");
        navbarPlaceholder.style.display = 'block'; // Muestra el placeholder
    } else {
        navbar.classList.remove("sticky");
        navbarPlaceholder.style.display = 'none'; // Oculta el placeholder
    }
    }


