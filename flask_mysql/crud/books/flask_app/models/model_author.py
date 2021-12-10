from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    

    # CREATE
    @classmethod
    def create(cls, data):
        query="INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)


    # READ
    @classmethod
    def get_all(cls):
        query="SELECT * FROM authors;"
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def get_one(cls, author_id):
        query=f"SELECT * FROM authors WHERE authors.id={author_id};"
        return connectToMySQL('books_schema').query_db(query)
    
