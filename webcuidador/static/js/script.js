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
});


