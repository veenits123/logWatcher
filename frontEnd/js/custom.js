
// connecting to WebSocket Server
var connection = new WebSocket("ws://localhost:1337");

// listening to Events
connection.onopen = function () {
    $(".card-header").html(
        '<div class="alert alert-success" role="alert">' +
        "<strong> Success! </strong> WebSocket Connected..." +
        "</div>"
    );
};

connection.onerror = function (error) {
    $(".card-header").html(
        '<div class="alert alert-danger" role="alert">' +
        "<strong> Failed! </strong> Try Again..." +
        "</div>"
    );
};

// extracting the message recieved from WS event
connection.onmessage = function (message) {
    try {
        var json = JSON.parse(message.data);
    } catch (e) {
        console.log("Doesn't seems like valid json....", message.data);
        return;
    }
    console.log(json.data);

    // appending the message recieved to HTML
    for (var key in json) {
        var value = json[key];

        $("tbody").append("<tr><td>" + value + "</td></tr>");
    }
};