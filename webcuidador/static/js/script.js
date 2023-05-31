function togglePassword(idBtn, idPassword ) {
  var showPasswordBtn = idBtn;
  var password = idPassword;
  if (password.type === "password") {
    password.type = "text";
    showPasswordBtn.innerHTML = '<i class="fa fa-eye-slash"></i>';

  } else {
    password.type = "password";
    showPasswordBtn.innerHTML = '<i class="fa fa-eye"></i>';
  }
}
//script registrar_evento.html
function toggleCampo(fieldName, radio) {
  var campo = document.querySelector('input[name="' + fieldName + '"]');
  campo.readOnly = radio.value === 'si' ? false : true;
  if (fieldName === 'animo') {
    campo.disabled = radio.value !== 'si';
  }
}
function validarFormulario() {
  var pregunta1 = document.querySelector('input[name="frecuencia_baño_afectada"]:checked');
  var pregunta2 = document.querySelector('input[name="frecuencia_alimentacion_afectada"]:checked');
  var pregunta3 = document.querySelector('input[name="horas_sueño_afectadas"]:checked');
  var pregunta4 = document.querySelector('input[name="estado_animo_afectado"]:checked');

  if (!pregunta1 || !pregunta2 || !pregunta3 || !pregunta4) {
    alert('Por favor, responda todas las preguntas.');
    return false;
  }

  return true;
}

$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip({
      placement: 'right',
      html: true,
      template: '<div class="tooltip" role="tooltip"><div class="arrow"></div><div class="tooltip-inner custom-tooltip"></div></div>',
      container: 'body'
  });
  $('[data-toggle="tooltip_error"]').tooltip({
    template: '<div class="tooltip" role="tooltip"><div class="tooltip-inner custom-tooltip-error"></div><div class="arrow"></div></div>',
    trigger: 'manual',

  }).tooltip('show');
  $('#tablaCuidadoresMedico').DataTable({
    "responsive": true,
    "bAutoWidth": false,
    "lengthChange": false,
    
    "language": {   // Cambiode lenguaje a español
        "infoFiltered": "(filtrado de _MAX_ registros totales)",
  
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sSearch": "Buscar:",
        "oPaginate": {
            "sFirst": "Primero",
            "sLast": "Último",
            "sNext": "Siguiente",
            "sPrevious": "Anterior"
        },
        "oAria": {
            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
    },
    initComplete: function () {
      var searchInput = $('.dataTables_filter input');
      
      searchInput.removeClass('input-sm');
      searchInput.addClass('input-lg');
      $('.dataTables_filter').addClass('float-left');
      
    }
  });
  $('#tablaCuidadores').DataTable({
    "responsive": true,
    "bAutoWidth": false,
    "aLengthMenu": [[5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todos"]],
    "iDisplayLength": 5,
    "language": {   // Cambiode lenguaje a español
      "infoFiltered": "(filtrado de _MAX_ registros totales)",
      "sLengthMenu": "Mostrar _MENU_  registros",
      "sZeroRecords": "No se encontraron resultados",
      "sEmptyTable": "Ningún dato disponible en esta tabla",
      "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
      "sSearch": "Buscar:",
      "oPaginate": {
        "sFirst": "Primero",
        "sLast": "Último",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
      },
      "oAria": {
        "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
      }
    },
    
  });
  $('#tablaTest').DataTable({
    "responsive": true,
    "bAutoWidth": false,
    "aLengthMenu": [[5,10, 25, 50, 100, -1], [5,10, 25, 50, 100, "Todos"]],
    "iDisplayLength": 5,
    "language": {   // Cambiode lenguaje a español
        "infoFiltered": "(filtrado de _MAX_ registros totales)",
        "sLengthMenu": "Mostrar _MENU_  registros",
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sSearch": "Buscar:",
        "oPaginate": {
            "sFirst": "Primero",
            "sLast": "Último",
            "sNext": "Siguiente",
            "sPrevious": "Anterior"
        },
        "oAria": {
            "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
    }
  });
  $('#verModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botón que activó el modal
    var eventId = button.data('evento-id'); // Obtener el ID del evento
    var fecha = button.data('fecha'); // Obtener la fecha del evento
    var fBaño = button.data('f-baño'); // Obtener el valor de f_baño
    var fAlimentacion = button.data('f-alimentacion'); // Obtener el valor de f_alimentacion
    var fSueño = button.data('f-sueño'); // Obtener el valor de f_sueño
    var animo = button.data('animo'); // Obtener el valor de animo
    var otro = button.data('otro');
    // Asignar los valores a los elementos del modal
    var modal = $(this);
    modal.find('#modal-fecha').text(fecha);
    modal.find('#modal-f-baño').text(fBaño);
    modal.find('#modal-f-alimentacion').text(fAlimentacion);
    modal.find('#modal-f-sueño').text(fSueño);
    modal.find('#modal-animo').text(animo);
    modal.find('#modal-otro').text(otro);
});
});


