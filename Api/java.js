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