# flask --app main run

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:chetan@localhost:5432/Flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} -> {self.title}"


@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method=='POST':
        title=request.form["title"]
        desc=request.form["title"]
        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
    
    todoData = Todo.query.all()
    return render_template('index.html', allTodo=todoData)
        # return "Hello, World"

@app.route("/delete/<int:sno>")
def delete_todo(sno):
    deleteTodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(deleteTodo)
    db.session.commit()
    return redirect("/")



@app.route("/update/<int:sno>")
def update_data():
    
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)