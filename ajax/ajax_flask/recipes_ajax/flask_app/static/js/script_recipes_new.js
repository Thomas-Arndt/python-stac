const recipe_form=document.getElementById("recipe_form");
recipe_form.onsubmit = function(e){
    e.preventDefault();
    var form=new FormData(recipe_form);
    fetch("http://localhost:5000/recipes/create", {method:"POST", body:form})
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        if(data.is_valid){
            let table=document.getElementById("recipe_table");
            let context=table.innerHTML;
            context+=`<tr><td>${data.name}</td><td>${data.under_thirty}</td><td>`;
            context+=`<a href="/recipes/${data.id}" class="text-decoration-none">view/edit</a>`;
            context+=`| <p onclick="delete_recipe( ${data.id} )" class="d-inline-block text-primary cursor-pointer">delete</p>`;
            context+=`</td></tr>`;
            table.innerHTML=context;

            document.getElementById("name").value="";
            document.getElementById("description").value="";
            document.getElementById("instructions").value="";
            document.getElementById("made_on").value="";
            document.getElementById("under_thirty_yes").checked=false;
            document.getElementById("under_thirty_no").checked=false;
        }
        else{
            let name_alert="";
            let description_alert="";
            let instructions_alert="";
            let made_on_alert="";
            let under_thirty_alert="";
            for(error of data){
                if(error[0]=="err_name"){
                    name_alert=`<p class="mb-0">${error[1]}</p>`;
                }
                else if(error[0]=="err_description"){
                    description_alert=`<p class="mb-0">${error[1]}</p>`;
                }
                else if(error[0]=="err_instructions"){
                    instructions_alert=`<p class="mb-0">${error[1]}</p>`;
                }
                else if(error[0]=="err_made_on"){
                    made_on_alert=`<p class="mb-0">${error[1]}</p>`;
                }
                else if(error[0]=="err_under_thirty"){
                    under_thirty_alert=`<p class="mb-0">${error[1]}</p>`;
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