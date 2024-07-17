function mostrarProductos(){
    let url='http://localhost:3000/tienda';
    fetch(url)
    .then(response => response.json())
    .then(data => ProductosData(data))
    .catch(error => console.log(error))

    const ProductosData=(data)=>{
        console.log(data)
        let texto=""

        for (i=0; i<data.length; i++)
        {
            texto+=`<tr>
            <td>${data[i].id}</td>
            <td>${data[i].nombre}</td>
            <td>${data[i].tipo}</td>
            <td>${data[i].desc}</td>
            </tr>`
        }//for
        document.getElementById('tienda').innerHTML=texto;
    }
}

function buscarTipo(){
    let url='http://localhost:3000/tienda';
    fetch(url)
    .then(response => response.json())
    .then(data => buscarData(data))
    .catch(error => console.log(error))

    const buscarData=(data)=>{
        console.log(data)
        let texto=""
        let tipo=document.getElementById('tipo').value;

        if(document.getElementById('tipo').selectedIndex==0){
            mostrarProductos();
        }
        else{
            for (i=0; i<data.length; i++)
        {
            if(tipo==data[i].tipo){
            texto+=`<tr>
            <td>${data[i].id}</td>
            <td>${data[i].nombre}</td>
            <td>${data[i].tipo}</td>
            <td>${data[i].desc}</td>
            </tr>`
            }
        }//for
        document.getElementById('tienda').innerHTML=texto;
        }//else
        


}//mostrar data
}
