$("form[name=login_form").submit(function (e) {
   var $form = $(this);
   var $error = $form.find(".error");
   var data = $form.serialize();

   $.ajax({
      url: "/user/login",
      type: "POST",
      data: data,
      dataType: "json",
      beforeSend: function () {
         $("*").css("cursor", "progress");
      },
      success: function (resp) {
         window.location.href = "/dashboard/";
      },
      error: function (resp) {
         $error.text(resp.responseJSON.error).removeClass("error--hidden");
      },
   });

   e.preventDefault();
});
