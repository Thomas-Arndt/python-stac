from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    

    @classmethod
    def create_ninja(cls, data):
        query="INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data) 

    @classmethod
    def get_all_ninjas(cls, dojo_id):
        query=f"SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id WHERE dojos.id={dojo_id};"
        print(query)
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        ninjas=[]

        for ninja in results:
            ninjas.append(cls(ninja))
        
        return ninjas

