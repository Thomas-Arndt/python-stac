from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Message:
    def __init__(self, data):
        self.id=data['id']
        self.message=data['message']
        self.sender_id=data['sender_id']
        self.receiver_id=data['receiver_id']
        if "sender_name" in data:
            self.sender_name=data['sender_name']
        if "message_id" in data:
            self.message_id=data['message_id']
        self.created_at=data['created_at']
        self.created_at=data['updated_at']


    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query="INSERT INTO messages (message, sender_id, receiver_id) VALUES (%(message)s, %(sender_id)s, %(receiver_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query="SELECT * FROM messages WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query="SELECT * FROM messages;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_messages = []
            for message in results:
                all_messages.append(cls(message))
            return all_messages
        return False

    @classmethod
    def get_all_by_receiver_id(cls, data:dict) -> list:
        query="SELECT *, sender.first_name as sender_name, messages.id as message_id FROM users as receiver LEFT JOIN messages ON receiver_id=receiver.id LEFT JOIN users as sender ON sender_id=sender.id WHERE receiver_id=%(receiver_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            all_messages = []
            for message in results:
                all_messages.append(cls(message))
            return all_messages
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query="UPDATE messages SET message=%(message)s, sender_id=%(sender_id)s, receiver_id=%(receiver_id)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query="DELETE FROM messages WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)