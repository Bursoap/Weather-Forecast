function get_forecast(form) {
    $.ajax({
        type: 'GET',
        url: '/api/forecast/'
    })
}

$(function () {
    $("<form>").onsubmit(function (event) {
        get_forecast(this);
        event.preventDefault()
    })
});