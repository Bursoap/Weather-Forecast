$( function() {
  $("#autocomplete").autocomplete({
    minLength: 2,
    source: function(request, response) {
          $.getJSON("/api/city/autocomplete",{ name: request.term,
              }, function(data) {
                  data.forEach(function (item) {
                      item.value = item.name;
                  });
                  response(data);
                  });
              },
    focus: function(event, ui) {
      $(this).val(ui.item.value);
      return false;
    },
    select: function(event, ui) {
      $(this).attr('city_id', ui.item.id);
      $(this).val(ui.item.value);
      return false;
    }
  }).autocomplete("instance")._renderItem = function(ul, item) {
      return $("<li>").append(`${item.value} (${item.country})`).appendTo(ul)
  };
});
