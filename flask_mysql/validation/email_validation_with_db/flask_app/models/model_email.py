from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.created_at=data['updated_at']


    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query="INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query="SELECT * FROM emails WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query="SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_emails = []
            for email in results:
                all_emails.append(cls(email))
            return all_emails
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query="UPDATE emails SET email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query="DELETE FROM emails WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_email(data):
        is_valid=True

        # Check if email field is empty or email is improperly formatted
        if not data['email'] or not EMAIL_REGEX.match(data['email']):
            flash("Please enter a valid email.", "err_email")
            is_valid=False

        # Check if email already exists in database
        query="SELECT email FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        for email in results:
            print(email)
            if data['email'] == email['email']:
                flash("Email already exists.", "err_email")
                is_valid=False

        return is_valid