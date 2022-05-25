from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, show

class Show:
    db_name="shows_usersdb"
    def __init__(self,data):
        self.id = data["id"]
        self.title=data["title"]
        self.network=data["network"]
        self.release_date=data["release_date"]
        self.description=data["description"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.user_id=data['user_id']
        self.user = None

    @classmethod
    def save(cls, data): 
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_shows(cls):
            query = "SELECT * FROM shows JOIN users on user_id = users.id;" #deleted left JOIN
            results= connectToMySQL(cls.db_name).query_db(query)
            shows = []
            for row in results:
                show = cls(row)
                user_data ={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at':row['created_at'],
                    'updated_at': row['updated_at'],
                }
                show.user = user.User(user_data)
                shows.append(show)
            return shows

    @classmethod
    def get_oneshow(cls, data):
            query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s;"
            results= connectToMySQL(cls.db_name).query_db(query, data)
            print (results)
            shows = []
            for row in results:
                show = cls(results[0])
                print (results[0]['users.id'])
                user_data ={
                    'id': results[0]['users.id'],
                    'first_name': results[0]['first_name'],
                    'last_name': results[0]['last_name'],
                    'email': results[0]['email'],
                    'password': results[0]['password'],
                    'created_at':results[0]['created_at'],
                    'updated_at': results[0]['updated_at'],
                }
                show.user = user.User(user_data)
            return show

    @classmethod
    def edit_show(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete_show(cls, id):
        data={
            'id':id
        }
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod #validations
    def validate_newshow(form_data):
            is_valid = True
            print(form_data)
            if len (form_data["title"]) < 3:
                is_valid =False
                flash("Title of show is required", "show")
            if len (form_data ["network"]) < 3:
                is_valid =False
                flash("Network of show required", "show")
            if len (form_data["release_date"]) < 4:
                is_valid =False
                flash("Release date required", "show")
            if len (form_data ["description"]) < 3:
                is_valid =False
                flash("Description of show required", "show")
            return is_valid
