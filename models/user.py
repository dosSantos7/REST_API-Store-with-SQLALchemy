from db import db


class UserModel(db.Model):
    __tablename__ = 'users'     # defining the table name used in this resource

    # which attribute of the table is to be used, must be same as the instance variables
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # can be used to add or update a row in DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # queries the DB to find a row with the specified name, return an object of UserModel type
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # queries the Db to find a row with the specified id, return an object of UserModel type
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))
        #
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

