function pullUser(){
    let userCredentials = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
    }

    $.ajax({
        url: '/receiver',
        type: 'POST',
        data: JSON.stringify(userCredentials),
        success: function (response) {
            let data = JSON.parse(response)
            document.getElementById("test").innerHTML = data["hello"];
            console.log("hello, world!");
        },
        error: function(response){alert("something is wrong")}
    });
}

//have to prevent sqlinjection
