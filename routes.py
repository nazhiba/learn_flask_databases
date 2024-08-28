from flask import render_template, request, redirect, url_for
# from models import Orang
from models import User
from flask_login import login_user, logout_user, current_user, login_required

def register_routes(app,db,bcrypt):
     
     @app.route('/')
     def index():
          return render_template('index.html')

     @app.route('/signup',methods=['GET','POST'])
     def signup():
          if request.method == 'GET':
               return render_template('signup.html')
          elif request.method == 'POST':
               username = request.form.get('username')
               password = request.form.get('password')
               hashed_password = bcrypt.generate_password_hash(password)
               user = User(Username=username, Password=hashed_password)
               db.session.add(user)
               db.session.commit()
               return redirect(url_for('index'))

     @app.route('/login',methods=['GET','POST'])
     def login():
          if request.method == 'GET':
               return render_template('login.html')
          elif request.method == 'POST':
               username = request.form.get('username')
               password = request.form.get('password')

               user = User.query.filter(User.Username == username).first()
               if bcrypt.check_password_hash(user.Password, password):
                    login_user(user)
                    return render_template('index.html')
               else:
                    return 'Failed!!'


     @app.route('/logout')
     def logout():
          logout_user()
          return redirect(url_for('index'))

     @app.route('/secret')
     @login_required
     def secret():
          return 'BTC-21091471213145010011'


"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
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
          
"""
