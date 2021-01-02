$(document).ready(function () {
  $("#id_username").on("keyup",function () {

    $.ajax({
      data:$(this).serialize(),
      url: $("form").attr("data-validate-url"),
      //dataType: 'json',
      success:function (data) {
        if (data.user_error){
          $("#user-error").fadeIn(500);
        }
        else {
          $("#user-error").fadeOut(500);
        }
      },
      error:function () {
        console.error("json loading failed");
      }
    });
  });

  $("#id_email").on("keyup",function () {

    $.ajax({
      data:$(this).serialize(),
      url: $("form").attr("data-validate-url"),
      dataType: 'json',
      success: function (data) {
        if (data.mail_error) {
          $("#mail-error").fadeIn(500);
        }
        else{
          $("#mail-error").fadeOut(500);
        }
      },
      error:function () {
        console.error("Json loading failed");
      }
    });
  });
});
