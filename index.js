function pullUser(){
    //have to prevent sqlinjection
    user = document.getElementById("username")
    pass = document.getElementById("password")
    let userCredentials = {
        username: user['value'],
        password: pass['value'],
    }

    $.ajax({
        url: '/receiver',
        type: 'POST',
        data: JSON.stringify(userCredentials),
        success: function (response) {responseHandler(response)},
        error: function(response){alert("something is wrong")}
    });
}

function responseHandler(response){
    let data = JSON.parse(response);
}
