// Ejemplo de JavaScript inicial para deshabilitar el envío de formularios si hay campos no válidos
(function () {
    'use strict'
  
    // Obtener todos los formularios a los que queremos aplicar estilos de validación de Bootstrap personalizados
    var forms = document.querySelectorAll('.needs-validation')
  
    // Bucle sobre ellos y evitar el envío
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add('was-validated')
          Swal.fire({
            title: 'Error',
            text: 'Campos Vacios',
            imageUrl: 'https://cdn.pixabay.com/photo/2023/05/23/20/29/rayo-makween-8013448_150.png',
            icon: 'error',
            width: 400,
            imageAlt: 'Custom image',
            }
        );
        }, false)
      })
  })()

  