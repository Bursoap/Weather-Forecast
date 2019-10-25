$(function() {
    $("#autocomplete").autocomplete({
        source:function(request, response) {
            $.getJSON("/api/city/autocomplete",{
                name: request.term, // in flask, "q" will be the argument to look for using request.args
            }, function(data) {
                response(data.matching_results); // matching_results from jsonify
            });
        },
        minLength: 2,
        select: function(event, ui) {
            console.log(ui); // not in your question, but might help later
        }
    });
});
