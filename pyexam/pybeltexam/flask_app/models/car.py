from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user, car

class Car:
    db_name="cars_usersdb"
    def __init__(self,data):
        self.id = data["id"]
        self.price=data["price"]
        self.model=data["model"]
        self.make=data["make"]
        self.year=data["year"]
        self.description=data["description"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.user_id=data['user_id']
        self.user = None

    @classmethod
    def save(cls, data): 
        query = "INSERT INTO cars (price, model, make, year, description, user_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_cars(cls):
            query = "SELECT * FROM cars LEFT JOIN users on user_id = users.id;"
            results= connectToMySQL(cls.db_name).query_db(query)
            cars = []
            for row in results:
                car = cls(row)
                user_data ={
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at':row['created_at'],
                    'updated_at': row['updated_at'],
                }
                car.user = user.User(user_data)
                cars.append(car)
            return cars

    @classmethod
    def edit(cls, data):
        query = "UPDATE cars SET price=%(price)s, model=%(model)s, make=%(make)s, year=%(year)s, description=%(description)s, WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def delete_car(cls, id):
        data={
            'id':id
        }
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    # @classmethod
    # def delete_car(cls,data):
    #     query = "DELETE FROM cars WHERE user_id = %(user_id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod #validations
    def validate_newcar(form_data):
            is_valid = True
            print(form_data)
            if len (form_data["price"]) < 1:
                is_valid =False
                flash("Please enter a price point", "car")
            if len (form_data ["model"]) < 3:
                is_valid =False
                flash("Model of car required", "car")
            if len (form_data ["make"]) < 3:
                is_valid =False
                flash("Make of car required", "car")
                is_valid = False
            if len (form_data["year"]) < 4:
                is_valid =False
                flash("Must input a year", "car")
            if len (form_data ["description"]) < 1:
                is_valid =False
                flash("Description of car required", "car")
            return is_valid
