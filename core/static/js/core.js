$(document).ready(function() {

    /* LOAD MODAL FORM */
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-box .modal-content").html("");
          $("#modal-box").modal("show");
        },
        success: function (data) {
          $("#modal-box .modal-content").html(data.html_form);
        }
      });
      return false;
    };
  
    /* DELETE MODAL CLICK*/
    $(".table_list").on("click", ".js-view-delete", function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        success: function (data) {
          $("#modal-box .modal-content").html(data.html_delete);
          $("#modal-box").modal("show");
        }
      });
    });
    /* CONFIRM MODAL CLICK*/
    $(".table_list").on("click", ".js-view-confirm", function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        success: function (data) {
          $("#modal-box .modal-content").html(data.html_confirm);
          $("#modal-box").modal("show");
        }
      });
    });
  
    /* SENDMAIL MODAL CLICK*/
    $(".table_list").on("click", ".js-send-activation", function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-box").modal("show");
        },
        success: function (data) {
          $("#modal-box .modal-content").html(data.html_sendmail);
        }
      });
    });
  
    /* SENDMAIL MODAL FORM */
    $("#modal-box").on("submit", ".js-sendmail-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            toastr.success("Correo enviado correctamente");
            $("#modal-box").modal("hide");  // <-- Close the modal
            if (data.url_redirect){
              window.location = data.url_redirect
            }
          }
          else {
            $("#modal-box .modal-content").html(data.html_sendmail);
          }
        }
      });
      return false;
    });
  
    /* DELETE MODAL FORM */
    $("#modal-box").on("submit", ".js-delete-form", function () {
        var form = $(this);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              $("#modal-box").modal("hide");  // <-- Close the modal
              if (data.url_redirect){
                window.location = data.url_redirect
              }else{
                $("#box_"+data.obj_pk+"").remove();
              }
            }
            else {
              $("#modal-box .modal-content").html(data.html_delete);
            }
          }
        });
        return false;
      });
  
      /* CONFIRM MODAL FORM */
    $("#modal-box").on("submit", ".js-confirm-form", function () {
        var form = $(this);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              $("#modal-box").modal("hide");  // <-- Close the modal
              if (data.url_redirect){
                window.location = data.url_redirect
              }else{
                $("#box_"+data.obj.pk+"").remove();
              }
            }
            else {
              $("#modal-box .modal-content").html(data.html_confirm);
            }
          }
        });
        return false;
      });
  
      /* ITEM MODAL CLICK */ 
      $(".js-item-delete").click(function (e) {
        e.preventDefault();
        var btn = $(this);
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-box .modal-content").html("");
            $("#modal-box").modal("show");
          },
          success: function (data) {
            $("#modal-box .modal-content").html(data.html_delete);
          }
        });
      });
   
    /* SAVE MODAL EDIT FORM */
    var saveEditForm = function () {
      var form = $(this);
      var formData = new FormData(this);
      $.ajax({
        url: form.attr("action"),
        data: formData,
        type: form.attr("method"),
        processData: false,
        contentType: false,
        success:function(data, textStatus, jqXHR){
          if (data.form_is_valid) {
            $("#modal-box").modal("hide");  // <-- Close the modal
            if (data.url_redirect){
              window.location = data.url_redirect
            }else{
              $("#box_"+data.obj_pk+"").fadeIn();
            }
          }else {
            $("#modal-box .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
    /* DELETE ITEM IN FORMSET FROM THE DOM */
    /*
    $(".table-formset").on('click', '.js-field-delete', function(){
      prefix = $(this).attr("prefix");
      forms = $(".table-formset");
      form_count = parseInt($("#id_"+prefix+"-TOTAL_FORMS").val())
      if(form_count-1 > 0) {
        $("#id_"+prefix+"-TOTAL_FORMS").val(form_count - 1);
        $(this).closest("tr").remove();
        c = 0
        $.each(forms, function(i, form) {
          if($(form).is(":visible")) {
            $(form).find(':input').each(function() {
              if ($(this).attr('name')) updateElementIndex($(this), prefix, c);
            });
            c++;
          }
        });
      }

      if($.isFunction(window.calculatePurchaseTotal)) {
        calculatePurchaseTotal();
      }
    });
    */
  
    updateElementIndex = function(elem, prefix, ndx) {
      input_name = elem.attr("name");
      field_name = input_name.substring(input_name.lastIndexOf('-', input_name.length))
      var replacement = prefix + '-' + ndx + field_name;
      if (elem.attr('id')) elem.attr('id', "id_" + replacement);
      if (elem.attr('name')) elem.attr('name', replacement);
    }
  
    /* GALLERY NEW FORM */
    /*
    $('.gallery-formset').formset({
      prefix: 'gallery',
      addText: 'Agregar',
      deleteText: 'Eliminar'
    });
  */

    /* USER ROLE SELECTED*/
    $("#wizard").on("change", "#id_user_type", function () {
      var _value = $(this).val();
      if(_value != ""){
          $.ajax({
            url: $("input[name=usertype_select]").data("url"),
            data: {'user_type':_value},
            type: 'get',
            dataType: 'json',
            success: function (data) {
              $("input[name=usertype_select]").val(data.is_group);
            }
          });
        }else{
          $("input[name=usertype_select]").val("");
        }
    });
  
    // Modal edit click
    $(".js-view-edit").click(loadForm);
    // Modal edit form submit
    $("#modal-box").on("submit", ".js-edit-form", saveEditForm);
  });
  