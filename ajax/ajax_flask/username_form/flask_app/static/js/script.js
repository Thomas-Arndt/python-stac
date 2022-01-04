display_all_users();

var new_user_form=document.getElementById("new_user_form");
new_user_form.onsubmit = function(e){
    e.preventDefault();
    var form=new FormData(new_user_form);
    fetch("http://localhost:5000/api/users/create", {method:'POST', body:form})
    .then(resp => resp.json())
    .then(data => {
        display_all_users();
    })
}

function display_all_users(){
    fetch("http://localhost:5000/api/users/get_all")
    .then(resp => resp.json())
    .then(data => {
        let context="";
        for(user of data){
            context+=`<tr><td>${user['user_name']}</td><td>${user['email']}</td></tr>`;
        }
        document.getElementById("user_table").innerHTML=context;
    })
}