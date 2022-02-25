from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://your_mysql_user:@your_mysql_host/your_mysql_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True)
    content = db.Column(db.String(100))

    def __init__(self, title, content):
        self.title = title
        self.content = content
db.create_all()

class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

@app.route('/notes', methods=['POST'])
def create_note():
  title = request.json['title']
  content = request.json['content']
  new_note = Note(title, content)
  db.session.add(new_note)
  db.session.commit()
  return note_schema.jsonify(new_note)

@app.route('/notes', methods=['GET'])
def get_notes():
  all_notes = Note.query.all()
  result = notes_schema.dump(all_notes)
  return jsonify(result)

@app.route('/notes/<id>', methods=['GET'])
def get_note(id):
  note = Note.query.get(id)
  return note_schema.jsonify(note)

@app.route('/notes/<id>', methods=['PUT'])
def update_note(id):
  note = Note.query.get(id)
  title = request.json['title']
  content = request.json['content']
  note.title = title
  note.content = content
  db.session.commit()
  return note_schema.jsonify(note)

@app.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
  note = Note.query.get(id)
  db.session.delete(note)
  db.session.commit()
  return note_schema.jsonify(note)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to fms-restapi-1'})

if __name__ == "__main__":
    app.run(debug=True)
