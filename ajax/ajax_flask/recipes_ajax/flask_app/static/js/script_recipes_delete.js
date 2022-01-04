function delete_recipe(recipe_id){
    // console.log(recipe_id);
    fetch(`http://localhost:5000/api/recipes/${recipe_id}/delete`)
    .then(resp => resp.json())
    .then(data => {
        console.log(data);
        let content="";
        for(recipe of data){
            content+=`<tr><td>${recipe.name}</td><td>${recipe.under_thirty}</td><td>`
            if(recipe.user_id==recipe.session_id){
                content+=`<a href="/recipes/${recipe.id}" class="text-decoration-none">view/edit</a>`;
                content+=`| <p onclick="delete_recipe( ${recipe.id} )" class="d-inline-block text-primary cursor-pointer">delete</p>`;
            }
            else{
                content+=`<a href="/recipes/${recipe.id}" class="text-decoration-none">view</a>`
            }
            content+="</td></tr>";
        }
        let recipe_table=document.getElementById("recipe_table");
        recipe_table.innerHTML=content;
    })
}