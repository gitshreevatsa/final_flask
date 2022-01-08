from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment.db'
db = SQLAlchemy(app)
meta = db.MetaData()


entrepreneur = db.Table(
    'faculty', meta,
    db.Column('Faculty_Id', db.String, primary_key=True),
    db.Column('Faculty_Name', db.String),
    db.Column('Gender', db.String),
    db.Column('Program', db.String),
    db.Column('Employment_type',db.String),
    db.Column('Highest_degree',db.String),
    db.Column('University_Name',db.String),
    db.Column('Passed_out_year',db.Integer),
    db.Column('Joining_date',db.Integer),
    db.Column('Designation',db.String),
    db.Column('Department',db.String),
    db.Column('No_of_students_mentored',db.Integer)
)
meta.create_all(db.engine)

def create(body):
    Faculty_Id = str(body['Faculty_Id'])
    Faculty_Name = str(body['Faculty_Name'])
    Gender = str(body['Gender'])
    Program = str(body['Program'])
    Employment_type = str(body['Employment_type'])
    Highest_degree = str(body['Highest_degree '])
    University_Name = str(body['University_Name'])
    Passed_out_year = str(body['Passed_out_year'])
    Joining_date = str(body['Joining_date'])
    Designation = str(body['Designation'])
    Department = str(body['Department'])
    No_of_students_mentored = str(body['No_of_students_mentored'])
    formation = db.engine.execute(entrepreneur.insert(),[{
        'Faculty_Id' : Faculty_Id, 'Faculty_Name' : Faculty_Name, 'Gender' : Gender, 'Program' : Program, 'Employment_type' : Employment_type,
        'Highest_degree' : Highest_degree, 'University_Name' : University_Name, 'Passed_out_year' : Passed_out_year, 'Joining_date' : Joining_date,
        'Designation' : Designation, 'Department' : Department, 'No_of_students_mentored' : No_of_students_mentored
    }])
    result = db.engine.execute('SELECT * FROM College WHERE USN = :val', {'val' : Faculty_Id})
    db.session.commit()


def read():
    dataview = entrepreneur.select()
    result = db.engine.execute(dataview)
    row_list = [] 
    for row in result.fetchall():
        row_list.append(dict(row))
    return jsonify(row_list)


def update(body):
    dict_input = dict(body)
    match = dict_input['Faculty_Id']
    for key, value in dict_input.items():
        updated = entrepreneur.update().where(entrepreneur.c.Faculty_Id_ID==match).values({key:value})
        result = db.engine.execute(updated)

def delete(body):
    option = body['Faculty_Id']
    deleted = entrepreneur.delete().where(entrepreneur.c.Faculty_Id == option)
    result = db.engine.execute(deleted)