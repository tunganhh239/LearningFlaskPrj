
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hota:h0tah0ta@localhost:3306/home'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    address= db.Column(db.String(100))
    height= db.Column(db.Float)
    weight= db.Column(db.Float)

    def __init__(self, name, address, height, weight):
        self.name = name
        self.address = address
        self.height = height
        self.weight = weight

db.create_all()

class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'height', 'weight')
person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

# Them nguoi
@app.route('/person', methods=['POST'])
def add_person():
  name = request.json['name']
  address = request.json['address']
  height = request.json['height']
  weight = request.json['weight']

  new_person = Person(name, address, height, weight)

  db.session.add(new_person)
  db.session.commit()

  return person_schema.jsonify(new_person)

# Get danh sach nguoi
@app.route('/person', methods=['GET'])
def getPersons():
  all_persons = Person.query.all()
  result = persons_schema.dump(all_persons)
  return jsonify(result)

#Get thong tin nguoi dung theo id
@app.route('/person/<id>',methods=['GET'])
def getPersonById(id):
      person = Person.query.get(id)
      return person_schema.jsonify(person)

#sua thong tin nguoi dung
@app.route('/person/<id>',methods=['PUT'])
def updatePersonById(id):
      person = Person.query.get(id)
      
      person.name = request.json['name']
      person.address = request.json['address']
      person.height = request.json['height']
      person.weight = request.json['weight']
        
      db.session.commit()
      return person_schema.jsonify(person)

#Xoa nguoi dung theo id
@app.route('/person/<id>',methods=['DELETE'])
def deletePersonById(id):
      person = Person.query.get(id)
      db.session.delete(person)
      db.session.commit()
      return person_schema.jsonify(person)


if __name__ == '__main__':
  app.run(debug=True)