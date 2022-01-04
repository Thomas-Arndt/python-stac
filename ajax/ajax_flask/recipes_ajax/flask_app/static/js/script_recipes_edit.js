const recipe_form=document.getElementById("recipe_form");
recipe_form.onsubmit = function(e){
    e.preventDefault();
    var form=new FormData(recipe_form);
    fetch("http://localhost:5000/recipes/update", {method:"POST", body:form})
    .then(resp => resp.json())
    .then(data => {
        // console.log(data);
        if(data.is_valid){
            let name=document.getElementById("info_name");
            name.innerText=data.name;
            let description=document.getElementById("info_description");
            description.innerText=data.description;
            let instructions=document.getElementById("info_instructions");
            instructions.innerText=data.instructions;
            let made_on=document.getElementById("info_made_on");
            made_on.innerText=data.made_on;
            let under_thirty=document.getElementById("info_under_thirty");
            under_thirty.innerText=data.under_thirty;
        }
        else{
            let name_alert=""
            let description_alert=""
            let instructions_alert=""
            let made_on_alert=""
            let under_thirty_alert=""
            for(error of data){
                if(error[0]=="err_name"){
                    name_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_description"){
                    description_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_instructions"){
                    instructions_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_made_on"){
                    made_on_alert=`<p class="mb-0">${error[1]}</p>`
                }
                else if(error[0]=="err_under_thirty"){
                    under_thirty_alert=`<p class="mb-0">${error[1]}</p>`
                }
            }
            if(name_alert){
                document.getElementById("err_name").classList.remove("collapse");
                document.getElementById("err_name").innerHTML=name_alert;
            }
            else{
                document.getElementById("err_name").classList.add("collapse");
                document.getElementById("err_name").innerHTML="";
            }
            if(description_alert){
                document.getElementById("err_description").classList.remove("collapse");
                document.getElementById("err_description").innerHTML=description_alert;
            }
            else{
                document.getElementById("err_description").classList.add("collapse");
                document.getElementById("err_description").innerHTML="";
            }
            if(instructions_alert){
                document.getElementById("err_instructions").classList.remove("collapse");
                document.getElementById("err_instructions").innerHTML=instructions_alert;
            }
            else{
                document.getElementById("err_instructions").classList.add("collapse");
                document.getElementById("err_instructions").innerHTML="";
            }
            if(made_on_alert){
                document.getElementById("err_made_on").classList.remove("collapse");
                document.getElementById("err_made_on").innerHTML=made_on_alert;
            }
            else{
                document.getElementById("err_made_on").classList.add("collapse");
                document.getElementById("err_made_on").innerHTML="";
            }
            if(under_thirty_alert){
                document.getElementById("err_under_thirty").classList.remove("collapse");
                document.getElementById("err_under_thirty").innerHTML=under_thirty_alert;
            }
            else{
                document.getElementById("err_under_thirty").classList.add("collapse");
                document.getElementById("err_under_thirty").innerHTML="";
            }
        }
    })
}