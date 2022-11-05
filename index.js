function pullUser(){
    //have to prevent sqlinjection
    let userCredentials = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
    }

    userCredJSON = JSON.stringify(userCredentials)
    ajaxPostRequest('/receiver', userCredJSON, responseHandler)
}

function responseHandler(response){
    let data = JSON.parse(response);
}
