function getData(){
    let userCred = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    }
    console.log("Hello world")
    let userCredJson = JSON.stringify(userCred)
    ajaxPostRequest('/receiver', userCredJson, responseHandler)
}

function responseHandler(response){
    console.log("Hello world")
    let userCred = JSON.parse(response)
    console.log(userCred)
}