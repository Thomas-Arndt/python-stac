const buttons = document.querySelectorAll(".button")
for (button of buttons){
    button.addEventListener("click", function(){
        getUserInfo();
    })
}

dataSelect=document.getElementById("user_input").value

function setDataSelect(element){
    dataSelect=element.value
    console.log(dataSelect);
}


function getUserInfo(){
    fetch('https://api.github.com/users/Thomas-Arndt')
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        console.log(dataSelect);
        document.getElementById("display").innerText = data[dataSelect];
    })
    .catch(err => console.log(err))
}