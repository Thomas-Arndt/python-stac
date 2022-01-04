from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify, get_flashed_messages

from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User
from flask_app.models.model_like import Like

@app.route('/recipes/new')
def recipes_new():
    if not "uuid" in session:
        return redirect('/')
    return render_template("recipes_new.html")

@app.route('/recipes/create', methods=['POST'])
def recipes_create():
    data = {
        **request.form,
        "user_id": session['uuid']
    }
    print(data)
    if not Recipe.validate_recipe(data):
        messages = get_flashed_messages(with_categories=True)
        session.pop('_flashes', None)
        if messages:
            return jsonify(messages)
    
    new_recipe=Recipe.create(data)
    data['id']=new_recipe
    data['is_valid']=True
    return jsonify(data)

@app.route('/recipes/<int:id>')
def recipes_show(id):
    if not "uuid" in session:
        return redirect('/')
        
    recipe = Recipe.get_one({"id":id})
    user = User.get_one({"id":session['uuid']})
    all_likes = Like.get_all_likes_by_recipe({"recipe_id":id})
    user_recipe_like = Like.get_likes_by_recipe_and_user({"user_id": session['uuid'], "recipe_id":id})
    return render_template("recipes_show.html", recipe=recipe, user=user, all_likes=all_likes, user_recipe_like=user_recipe_like)

@app.route('/recipes/<int:id>/edit')
def recipes_edit(id):
    if not "uuid" in session:
        return redirect('/')
    
    recipe = Recipe.get_one({"id":id})
    return render_template("recipes_edit.html", recipe=recipe)

@app.route('/recipes/update', methods=['POST'])
def recipes_update():
    if not "uuid" in session:
        return redirect ('/')
    
    data = {
        **request.form
    }

    if not Recipe.validate_recipe(data):
        messages = get_flashed_messages(with_categories=True)
        session.pop('_flashes', None)
        if messages:
            return jsonify(messages)

    Recipe.update_one(data)
    data['is_valid']=True
    return jsonify(data)

@app.route('/api/recipes/<int:id>/delete')
def recipes_delete(id):
    recipe = Recipe.get_one({"id":id})

    if "uuid" not in session or not recipe.user_id == session['uuid']:
        return redirect('/')
    Like.delete_all_by_recipe({"recipe_id":id})
    Recipe.delete_one({"id":id})
    results = Recipe.get_all()
    all_recipes=[]
    for recipe in results:
        data={
            "id":recipe.id,
            "name":recipe.name,
            "description":recipe.description,
            "instructions":recipe.instructions,
            "under_thirty":recipe.under_thirty,
            "made_on":recipe.made_on,
            "user_id":recipe.user_id,
            "session_id":session['uuid']
        }
        all_recipes.append(data)
    return jsonify(all_recipes)