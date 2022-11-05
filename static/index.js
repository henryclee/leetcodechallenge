function pullUser(){
    //have to prevent sqlinjection
    let userCredentials = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
    }

    $.ajax({
        url: '/receiver',
        type: 'POST',
        data: JSON.stringify(userCredentials),
        success: function(response){responseHandler(response)},
        error: function(response){alert("something is wrong")}
    });
}

function responseHandler(response){
    let data = JSON.parse(response);
    document.getElementById("test").innerHTML = data["hello"];
}
