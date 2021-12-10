from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    

    # CREATE
    @classmethod
    def create(cls, data):
        query="INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)
    

    # READ
    @classmethod
    def get_all(cls):
        query="SELECT * FROM books;"
        return connectToMySQL('books_schema').query_db(query)
    

    @classmethod
    def get_one(cls, book_id):
        query=f"SELECT * FROM books WHERE books.id={book_id};"
        return connectToMySQL('books_schema').query_db(query)
    

