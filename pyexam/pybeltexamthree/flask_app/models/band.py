from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, band

class Band:
    db_name="bands_usersdb"
    def __init__(self,data):
        self.id = data["id"]
        self.band_name=data["band_name"]
        self.music_genre=data["music_genre"]
        self.home_city=data["home_city"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.user_id=data['user_id']
        self.user = None

    @classmethod
    def save(cls, data): 
        query = "INSERT INTO bands (band_name, music_genre, home_city, user_id) VALUES (%(band_name)s, %(music_genre)s, %(home_city)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_bands(cls):
            query = "SELECT * FROM bands JOIN users on user_id = users.id;" #deleted left JOIN
            results= connectToMySQL(cls.db_name).query_db(query)
            bands = []
            for row in results:
                band = cls(row)
                user_data ={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at':row['created_at'],
                    'updated_at': row['updated_at'],
                }
                band.user = user.User(user_data)
                bands.append(band)
            return bands

    @classmethod
    def get_oneband(cls, data):
            query = "SELECT * FROM bands JOIN users ON bands.user_id = users.id WHERE bands.id = %(id)s;"
            results= connectToMySQL(cls.db_name).query_db(query, data)
            print (results)
            bands = []
            for row in results:
                band = cls(results[0])
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
                band.user = user.User(user_data)
            return band

    @classmethod
    def edit_band(cls, data):
        query = "UPDATE bands SET band_name = %(band_name)s, music_genre = %(music_genre)s, home_city = %(home_city)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete_band(cls, id):
        data={
            'id':id
        }
        query = "DELETE FROM bands WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod #validations
    def validate_newband(form_data):
            is_valid = True
            print(form_data)
            if len (form_data ["band_name"]) < 2:
                is_valid =False
                flash("Band name is required and has to be at least 2 characters", "band")
            if len (form_data ["music_genre"]) < 2:
                is_valid =False
                flash("Music genre of band is required and has to be at least 2 characters", "band")
            if len (form_data ["home_city"]) < 1:
                is_valid =False
                flash("Home city required", "band")
            return is_valid
