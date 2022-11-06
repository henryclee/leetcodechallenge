"use strict"

function pullUser(){
    //have to prevent sqlinjection
    let userObj = document.getElementById("username");
    let passObj = document.getElementById("password");
    let user = userObj.value;
    let pass = passObj.value;
    let userCredentials = {
        username: user,
        password: pass,
    }

    console.log(user);
    console.log(pass);

}

function leaderboard(response) {
    let data = JSON.parse(response)
    let layout = {"title":"leetcode LeaderBoard", "xaxis":{"title":"username"},"yaxis":{"title":"number solved"}};
    Plotly.newPlot("leaderboard",data,layout);
}

function getData(){
    ajaxGetRequest("/leaderboard",leaderboard);
}

function responseHandler(response){
    let data = JSON.parse(response);
}
