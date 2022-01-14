from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from datetime import datetime
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flask'
db = SQLAlchemy(app)
ma = Marshmallow(app)



#Table
class Employee(db.Model):
   __tablename__ = "employee"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(20))
   email = db.Column(db.String(50), nullable = False)
   mobile = db.Column(db.Integer(13))
   department = db.Column(db.String(20))
   joining_date = db.Column(db.Date)
   designation = db.Column(db.String)
   experience = db.Column(db.String)
   level = db.Column(db.Integer)
   left_date = db.Column(db.date)
   dob = db.Column(db.String)
   created = db.Column(db.DateTime, default=datetime.now)
   updated = db.Column(db.DateTime)
   
   
   def create(self):
       db.session.add(self)
       db.session.commit()
       return self

   def __init__(self, name, email, mobile, department, joining_date, designation, experience, level, left_date, dob):
       self.name = name
       self.email = email
       self.mobile = mobile
       self.department = department
       self.joining_date = joining_date
       self.designation = designation
       self.experience = experience
       self.level = level
       self.left_date = left_date
       self.dob = dob
       

   def __repr__(self):
       return f"{self.id}"


db.create_all()


class employeeSchema(ModelSchema):
   class Meta(ModelSchema.Meta):
       model = Employee
       sqla_session = db.session
   id = fields.Number(dump_only=True)
   name = fields.String(required=True)
   mobile = fields.Integer(required=True)
   department = fields.String(required=True)
   joining_date = fields.Date(required=True)
   designation = fields.String(required=True)
   experience = fields.String(required=True)
   level = fields.Integer(required=True)
   left_date = fields.Date(required=True)
   dob = fields.Date(required=True)
   
   
@app.route('/api/employee', methods=['POST'])
def create_todo():
   data = request.get_json()
   employee_schema = employeeSchema()
   employee = employee_schema.load(data)
   result = employee_schema.dump(employee.create())
   return make_response(jsonify({"employee": result}), 200)


@app.route('/api/employee', methods=['GET'])
def index():
   get_todos = Employee.query.all()
   employee_schema = employeeSchema(many=True)
   employee = employee_schema.dump(get_todos)
   return make_response(jsonify({"employee": employee}))


if __name__ == '__main__':
    app.run(debug=True)
