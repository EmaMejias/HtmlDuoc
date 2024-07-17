function borrar(){
    document.getElementById("pwd").value = "";
}

let flag = true;

function pass(){
    if (flag){
        document.getElementById("pwd").type = "password";
        document.getElementById("pass-icon").src = "{% static 'Imagen/close.png' %}";
        flag = false;
    }else {
        document.getElementById("pwd").type = "text";
        document.getElementById("pass-icon").src = "{% static 'Imagen/open.png' %}";
        flag = true;
    }
}