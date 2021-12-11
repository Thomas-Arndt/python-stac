from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self, data):
        self.author_id=data['author_id']
        self.book_id=data['book_id']
    

    # CREATE
    @classmethod
    def create(cls, data):
        query="INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query, data)

    # READ
    @classmethod
    def get_favorite_books(cls, author_id):
        query=f"SELECT * FROM books JOIN favorites ON favorites.book_id=books.id JOIN authors ON favorites.author_id=authors.id WHERE authors.id={author_id};"
        return connectToMySQL('books_schema').query_db(query)
    
    @classmethod
    def get_favorited_by(cls, book_id):
        query=f"SELECT * FROM authors JOIN favorites ON favorites.author_id=authors.id JOIN books ON favorites.book_id=books.id WHERE books.id={book_id};"
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def get_unfavorited_author_by_book(cls, book_id):
        data={"id":book_id}
        query="SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        return connectToMySQL('books_schema').query_db(query, data)
