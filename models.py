from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # Changed from ID to id
    Username = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Role = db.Column(db.String)
    deskripsi = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.Username}, Role: {self.Role}>'

    def get_id(self):
        return str(self.id)  # Flask-Login expects this method to return a string


# class Orang(db.Model):
#      __tablename__ = 'people'
#      ID = db.Column(db.Integer,primary_key=True)
#      Nama = db.Column(db.Text,nullable=False)
#      Umur = db.Column(db.Integer)
#      Pekerjaan = db.Column(db.Text)

#      def __repr__(self):
#           return f'Orang dengan Nama {self.Nama} dan umur {self.Umur} dan pekerjaan sebagai {self.Pekerjaan}'
