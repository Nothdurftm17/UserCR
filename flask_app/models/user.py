from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__ (self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)

        print(results)

        all_users = [] 

        for one_user in results:
            all_users.append( cls(one_user) )

            print(all_users)
        return all_users

    @classmethod
    def addNew(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        new_id= connectToMySQL('users_schema').query_db(query, data)
        return new_id
    