from app import db
class Orang(db.Model):
     __tablename__ = 'people'
     ID = db.Column(db.Integer,primary_key=True)
     Nama = db.Column(db.Text,nullable=False)
     Umur = db.Column(db.Integer)
     Pekerjaan = db.Column(db.Text)

     def __repr__(self):
          return f'Orang dengan Nama {self.Nama} dan umur {self.Umur} dan pekerjaan sebagai {self.Pekerjaan}'
