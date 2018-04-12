from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

DBURI = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DBURI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    level = db.Column(db.Integer)
    rank = db.Column(db.String(50))

@app.route("/")
def index():

    return "Hello World!"

@app.route("/api/users")
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            "name": user.name,
            "level": user.level,
            "rank": user.rank
            })

    return jsonify(users_list)

@app.route("/api/users/<string:name>")
def get_user_by_name(name):
    user = User.query.filter_by(name=name).first_or_404()
    user_dicc = {
            "name": user.name,
            "level": user.level,
            "rank": user.rank
            }

    return jsonify(user_dicc)

@app.route("/api/users", methods=["POST"])
def add_user():
    new_user = User(name=request.json["name"], level=request.json["level"], rank=request.json["rank"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "ok"})

@app.route("/api/users/<string:name>", methods=["PUT"])
def edit_user(name):
    user = User.query.filter_by(name=name).first_or_404()
    user.name = request.json["name"]
    user.level = request.json["level"]
    user.rank = request.json["rank"]

    db.session.commit()

    return jsonify({"message": "ok"})

@app.route("/api/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "ok"})

    return jsonify({"message": "error"})

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
