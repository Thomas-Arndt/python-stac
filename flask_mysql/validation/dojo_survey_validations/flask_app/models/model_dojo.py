from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comments=data['comments']
        self.created_at=data['created_at']
        self.created_at=data['updated_at']


    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query="INSERT INTO dojos (name, location, language, comments) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query="SELECT * FROM dojos WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query="SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_dojos = []
            for dojo in results:
                all_dojos.append(cls(dojo))
            return all_dojos
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query="UPDATE dojos SET name=%(name)s, location=%(location)s, language=%(language)s, comments=%(comments)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query="DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['name']) < 1:
            flash("You must provide your name.", "err_name")
            is_valid = False
        if data['location'] == "":
            flash("Please choose a location.", "err_location")
            is_valid = False
        if data['language'] == "":
            flash("Please choose a language.", "err_language")
            is_valid = False
        if len(data['comments']) > 255:
            flash("Your comment must be less than 255 characters.", "err_comments")
            is_valid = False
        return is_valid


        
