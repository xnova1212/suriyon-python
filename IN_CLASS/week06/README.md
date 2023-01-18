INTRODUCTION
------------
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#
https://sqliteonline.com/

EXAMPLE INTERACTION
-------------
Example create database. run in python shell only
```python
from server import app, db, Studentonly

with app.app_context():
    db.create_all() # ถ้าทำครั้งแรกจะได้โฟลเดอร์ instance มา
```

Example add data. run in python shell 
```python
from server import app, db, Student

#create object
std1 = Student(sid='64122420220', sname='Phumin Maliwan', smobile='0999999999', sfaculty='Computer Science')

with app.app_context():
    db.session.add(std1) # เพิ่มข้อมูล
    db.session.commit() # ยืนยันการเพิ่มข้อมูล
```

Example query data. run in python shell only
```python
from server import app, db, Student

with app.app_context():

    stds = Student.query.all() # no condition
    for i in stds:
        print(i.sid, i.sname, i.smobile, i.sfaculty)


    std1 = Student.query.filter(Student.sid=="64122420220").first() # use condition 1 ==, >, <, other| .first() = chain function ทำงานโดนการเอามาคนเดียว


    std2 = Student.query.filter_by(sid="64122420220").first() # use condition 2 | .first() = chain function ทำงานโดนการเอามาคนเดียว
```


Example update data. run in python shell only
```python
from server import app, db, Student

with app.app_context():
    std = Student.query.filter_by(sid="64122420220").first()
    std.sname = "Hello World"
    db.session.commit()
```