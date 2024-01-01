document.addEventListener('DOMContentLoaded', function() {

    
    // Hacer una solicitud AJAX para obtener el listado de clientes
    fetch('/obtener_clientes/')
    .then(response => response.json())
    .then(data => {
        const selectClientes = document.createElement('select');
        selectClientes.setAttribute('id', 'selectClientes');
        
        data.forEach(cliente => {
            const option = document.createElement('option');
            option.value = cliente.id;
            option.textContent = cliente.nombre;
            selectClientes.appendChild(option);
        });

        // Busca el elemento con id "contenedorClientes" en el DOM
        const contenedor = document.getElementById('contenedorClientes');

        // Añade el combobox al elemento "contenedorClientes"
        if (contenedor) {
            contenedor.appendChild(selectClientes);
        } else {
            console.error('El elemento contenedorClientes no fue encontrado en el DOM.');
        }
    })
    .catch(error => {
        console.error('Error al obtener el listado de clientes:', error);
    });
});