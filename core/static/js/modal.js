$(function () {

    var atr_url;
  
    var loadForm = function () {
      var btn = $(this);
      atr_url = btn.attr("data-url");
      $.ajax({
        url: atr_url,
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal_form .modal-content").html("");
          $("#modal_form").modal("show");
        },
        success: function (data) {
          $("#modal_form .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      var data = new FormData($(this).get(0));
      $.ajax({
        url: atr_url,
        data: data,
        type: form.attr("method"),
        cache: false,
        contentType: false,
        processData: false,
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#modal_form").modal("hide");
            if (data.url_redirect){
              window.location = data.url_redirect
            }
          }
          else {
            $("#modal_form .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
    //Create service
    $(".js-create").click(loadForm);
    $("#modal_form").on("submit", ".create-form", saveForm);
  });