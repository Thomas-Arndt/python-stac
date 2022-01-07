from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
import os
import requests

@app.route('/api/weather/get')
def api_weather_get():
    r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=44.636784&lon=-124.053452&appid={os.environ.get('FLASK_APP_API_KEY')}&units=imperial")

    return jsonify(r.json())

@app.route('/table_name/create', methods=['POST'])
def table_name_create():
    return redirect('/')

@app.route('/table_name/<int:id>')
def table_name_show(id):
    return render_template("table_name_show.html")

@app.route('/table_name/<int:id>/edit')
def table_name_edit(id):
    return render_template("table_name_edit.html")

@app.route('/table_name/<int:id>/update', methods=['POST'])
def table_name_update(id):
    return redirect('/')

@app.route('/table_name/<int:id>/delete')
def table_name_delete(id):
    return redirect('/')