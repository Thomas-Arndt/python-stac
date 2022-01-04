const registration_form=document.getElementById("registration_form");
registration_form.onsubmit = function(e){
    e.preventDefault();
    var form=new FormData(registration_form);
    fetch("http://localhost:5000/users/create", {method:"POST", body:form})
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        if(data.redirect){
            window.location.href=data.redirect;
        }
        else{
            let first_name_alert=""
            let last_name_alert=""
            let email_alert=""
            let password_alert=""
            let password_confirm_alert=""
            for(error of data){
                if(error[0]=="err_first_name"){
                    first_name_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_last_name"){
                    last_name_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_email"){
                    email_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_password"){
                    password_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_password_confirm"){
                    password_confirm_alert=`<p class="mb-0">${error[1]}</p>`
                }
            }
            if(first_name_alert){
                document.getElementById("err_first_name").classList.remove("collapse");
                document.getElementById("err_first_name").innerHTML=first_name_alert;
            }
            else{
                document.getElementById("err_first_name").classList.add("collapse");
                document.getElementById("err_first_name").innerHTML="";
            }
            if(last_name_alert){
                document.getElementById("err_last_name").classList.remove("collapse");
                document.getElementById("err_last_name").innerHTML=last_name_alert;
            }
            else{
                document.getElementById("err_last_name").classList.add("collapse");
                document.getElementById("err_last_name").innerHTML="";
            }
            if(email_alert){
                document.getElementById("err_email").classList.remove("collapse");
                document.getElementById("err_email").innerHTML=email_alert;
            }
            else{
                document.getElementById("err_email").classList.add("collapse");
                document.getElementById("err_email").innerHTML="";
            }
            if(password_alert){
                document.getElementById("err_password").classList.remove("collapse");
                document.getElementById("err_password").innerHTML=password_alert;
            }
            else{
                document.getElementById("err_password").classList.add("collapse");
                document.getElementById("err_password").innerHTML="";
            }
            if(password_confirm_alert){
                document.getElementById("err_password_confirm").classList.remove("collapse");
                document.getElementById("err_password_confirm").innerHTML=password_confirm_alert;
            }
            else{
                document.getElementById("err_password_confirm").classList.add("collapse");
                document.getElementById("err_password_confirm").innerHTML="";
            }
        }
    })
}