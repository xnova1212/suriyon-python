from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = b"mantvmass"
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
    return render_template("index.html", title="Home Page")


@app.route('/students')
def students():
    stds = Student.query.all()
    return render_template("student/index.html", students=stds, title="Student List")


@app.route('/student/new', methods=["GET", "POST"])
def new():

    if request.method == "POST":
        #create object
        std = Student(
            sid=request.form["id"],
            sname=request.form["name"],
            smobile=request.form["mobile"],
            sfaculty=request.form["faculty"]
        )

        db.session.add(std) # เพิ่มข้อมูล
        db.session.commit() # ยืนยันการเพิ่มข้อมูล
        
        flash('add new success', 'success')
        return redirect(url_for("students"))


    return render_template("student/new.html", title="New Student")



if __name__ == "__main__":
    app.run(debug=True)