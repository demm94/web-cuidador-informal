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
});


