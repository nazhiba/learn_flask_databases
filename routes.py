from flask import render_template, request
from models import Orang

def register_routes(app,db):
     @app.route('/',methods=['GET','POST'])
     def index():
          if request.method == 'GET':
               orang = Orang.query.all()
               return render_template('index.html',people=orang)
          elif request.method == 'POST':
               nama = request.form.get('nama')
               umur = int(request.form.get('umur'))
               pekerjaan = request.form.get('pekerjaan')

               person = Orang(Nama=nama,Umur=umur,Pekerjaan=pekerjaan)

               db.session.add(person)
               db.session.commit()

               orang = Orang.query.all()
               return render_template('index.html',people=orang)

     @app.route('/delete/<ID>',methods=['DELETE'])
     def delete(ID):
          Orang.query.filter(Orang.ID == ID).delete()
          db.session.commit()
          orang = Orang.query.all()
          return render_template('index.html',people=orang)
