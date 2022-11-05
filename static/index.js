function pullUser(){
    let userCredentials = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
    }
    let userCredentialsAsJson = JSON.stringify(userCredentials);
    console.log(userCredentials)
    // ajaxPostRequest(something in python, userCredentialsAsJson, some function in js that plots it);
}

//have to prevent sqlinjection
