from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data):
        self.id=data['id']
        self.user_name=data['user_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query="INSERT INTO users (user_name, email) VALUES (%(user_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query="SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query="SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False

    @classmethod
    def api_get_all(cls) -> list:
        query="SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            return results
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query="UPDATE users SET user_name=%(user_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query="DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)