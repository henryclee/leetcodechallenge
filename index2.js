"use strict"

function pullUser(){
    let userCred = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    }
    //console.log("Hello world")
    let userCredJson = JSON.stringify(userCred)
    ajaxPostRequest('/receiver', userCredJson, responseHandler)
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
