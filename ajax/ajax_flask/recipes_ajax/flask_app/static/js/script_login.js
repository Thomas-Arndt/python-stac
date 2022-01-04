const login_form=document.getElementById("login_form");
login_form.onsubmit = function(e){
    e.preventDefault();
    var form=new FormData(login_form);
    fetch("http://localhost:5000/users/login", {method:"POST", body:form})
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        if(data.redirect){
            window.location.href=data.redirect;
        }
        else{
            let email_alert=""
            let login_alert=""
            for(error of data){
                if(error[0]=="err_email"){
                    email_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_login"){
                    login_alert=`<p class="mb-0">${error[1]}</p>`
                }
            }
            if(email_alert){
                document.getElementById("err_email").classList.remove("collapse");
                document.getElementById("err_email").innerHTML=email_alert;
            }
            else{
                document.getElementById("err_email").classList.add("collapse");
                document.getElementById("err_email").innerHTML="";
            }
            if(login_alert){
                document.getElementById("err_login").classList.remove("collapse");
                document.getElementById("err_login").innerHTML=login_alert;
            }
            else{
                document.getElementById("err_login").classList.add("collapse");
                document.getElementById("err_login").innerHTML="";
            }
        }
    })
}