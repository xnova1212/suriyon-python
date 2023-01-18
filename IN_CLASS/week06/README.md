INTRODUCTION
------------
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#
https://sqliteonline.com/

EXAMPLE
-------------
File: server.py
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"

db = SQLAlchemy()
db.init_app(app)

class Student(db.Model):
    sid = db.Column(db.String, primary_key=True)
    sname = db.Column(db.String, nullable=False)
    smobile = db.Column(db.String, nullable=False)
    sfaculty = db.Column(db.String, nullable=False)

    # orm = object-relational-mapping | รูปแบบการจัดการ Database แบบ orm

    def __str__(self):
        """
        print(Student()) ปกติจะออกมาเป็น 0x00000 แต่ func นี้จะทำให้ได้ผลลัพตามที่เราส่งค่าออกไปภายใน function นี้
        Example: run in python shell
        #create object
        std1 = Student(sid='64122420220', sname='Phumin Maliwan', smobile='0999999999', sfaculty='Computer Science')
        print(std1)
        """
        return self.sname
        
@app.route('/')
def index():
    return render_template("student/index.html", title="Home Page")

if __name__ == "__main__":
    app.run(debug=True)
```

example create database run in python shell
```python
from server import app, db, Student

with app.app_context():
    db.create_all()
```

example add data run in python shell
```python
from server import app, db, Student

#create object
std1 = Student(sid='64122420220', sname='Phumin Maliwan', smobile='0999999999', sfaculty='Computer Science')

with app.app_context():
    db.session.add(std1) # เพิ่มข้อมูล
    db.session.commit() # ยืนยันการเพิ่มข้อมูล
```

example query data run in python shell
```python
from server import app, db, Student

with app.app_context():
    Student.query.all()
```