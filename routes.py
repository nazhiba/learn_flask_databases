from flask import render_template, request
# from models import Orang
from models import User
from flask_login import login_user, logout_user, current_user, login_required

def register_routes(app,db,bcrypt):
     @app.route('/',methods=['GET','POST'])
     def index():
          if  current_user.is_authenticated:
               return str(current_user.Username)
          else:
               return 'No users logged in'

     @app.route('/login/<id>')
     def login(id):
          user = User.query.get(id)
          login_user(user)
          return 'SUKSUES'

     @app.route('/logout')
     def logout():
          logout_user()
          return 'SUKSUES'

     #      if request.method == 'GET':
     #           orang = Orang.query.all()
     #           return render_template('index.html',people=orang)
     #      elif request.method == 'POST':
     #           nama = request.form.get('nama')
     #           umur = int(request.form.get('umur'))
     #           pekerjaan = request.form.get('pekerjaan')

     #           person = Orang(Nama=nama,Umur=umur,Pekerjaan=pekerjaan)

     #           db.session.add(person)
     #           db.session.commit()

     #           orang = Orang.query.all()
     #           return render_template('index.html',people=orang)

     # @app.route('/delete/<ID>',methods=['DELETE'])
     # def delete(ID):
     #      Orang.query.filter(Orang.ID == ID).delete()
     #      db.session.commit()
     #      orang = Orang.query.all()
     #      return render_template('index.html',people=orang)

     # @app.route('/detail/<pid>')
     # def detail(pid):
     #      orang = Orang.query.filter(Orang.ID == pid).first()
     #      return render_template('details.html',person=orang)
          