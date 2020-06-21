$(function () {
  var btn
  $(".js-create-book").click(function () {
    $.ajax({
      url: '/books/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  });

  $("#modal-book").on("submit", ".js-book-create-form", function () {
    var form = $(this);
    $.ajax({

      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      // dataType: 'json',
      success: function (data) {
        // alert("hello")
        // alert(data)
        if (data) {

          $('.table_class').html(data)
          $("#modal-book").modal("hide");
          $(".js-update-book").click(function () {

            btn = $(this);
             console.log("sa")
            $.ajax({
              url: btn.attr("data-url"),
              type: 'get',
              // dataType: 'json',
              beforeSend: function () {
                $("#modal-update").modal("show");
              },
              success: function (data) {
                $("#modal-update .modal-content").html(data);
              }
            });
          });

        // window.location.href = "http://127.0.0.1:8000/books/";
        // window.location.reload(true)
            // <-- This is just a placeholder for now for testing
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

  $(".js-update-book").click(function () {

    btn = $(this);
     console.log("sa")
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      // dataType: 'json',
      beforeSend: function () {
        $("#modal-update").modal("show");
      },
      success: function (data) {
        $("#modal-update .modal-content").html(data);
      }
    });
  });
    $("#modal-update").on("submit", ".js-book-update-form", function () {
    var form = $(this);
    $.ajax({
       url: btn.attr("data-url"),
       data: form.serialize(),
       type: form.attr("method"),
      //  dataType: 'json',

       success: function (data) {
         if (data) {
          $('.table_class').html(data)
           $("#modal-update").modal("hide");
           $(".js-update-book").click(function () {

             btn = $(this);
              console.log("sa")
             $.ajax({
               url: btn.attr("data-url"),
               type: 'get',
               // dataType: 'json',
               beforeSend: function () {
                 $("#modal-update").modal("show");
               },
               success: function (data) {
                 $("#modal-update .modal-content").html(data);
               }
             });
           });
         }
         else {
           $("#modal-book .modal-content").html(data.html_form);
         }
       }
     });
     return false;
});

});
