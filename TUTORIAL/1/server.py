from flask import Flask, request, jsonify
from database import Database
from time import time
import bcrypt



server = Flask("mantvmass")
database = Database("accounts.json")


def hashing(data):
    bytes = data.encode('utf-8') # converting password to array of bytes
    salt = bcrypt.gensalt() # generating the salt
    hash = bcrypt.hashpw(bytes, salt) # Hashing the password
    return hash


def verifyHashing(data, hash) -> bool:
    # print(hash)
    data_endcode = data.encode('utf-8') # encoding user password
    return bcrypt.checkpw(data_endcode, hash) # checking password | boolean


def getLastIndex(data, table) -> int:
    # print(data)
    last_index = data[table][-1] # last account
    return last_index["id"] # id last account


@server.route("/", methods=["GET", "POST"])
def index():
    return "HI"


@server.route("/signin", methods=["GET", "POST"])
def signin():
    username, password = request.form["username"], request.form["password"]
    data = database.select()[1]["accounts"]
    for i in data:
        if i["username"] == username and verifyHashing(password, i["password"].encode('utf-8')):
            return jsonify({"status": "success", "message": None, "data": i}), 200
    return jsonify({"status": "error", "message": "invalid username or password", "data": None}), 200


@server.route("/signup", methods=["GET", "POST"])
def signup():
    try:
        username, password, fullname = request.form["username"], request.form["password"], request.form["fullname"]
    except Exception as err:
        # print(str(err))
        return jsonify({"status": "error", "message": "parameter in wrong!?. type: form, parameter: username, password, fullname", "data": None}), 200
    data = database.select() # return tuple (boolean, data)
    for i in data[1]["accounts"]:
        if i["username"] == username:
            return jsonify({"status": "error", "message": "username is already", "data": None}), 200
    index = getLastIndex(data[1], "accounts")+1
    pass_hash = hashing(password)
    # print(pass_hash)
    new_ac = { "id": index, "username": username, "password": pass_hash.decode("utf-8"), "timestamp": int(time()) }
    new_cu = { "account_id": index, "fullname": fullname, "balance": 0.00 }
    data[1]["accounts"].append(new_ac)
    data[1]["customers"].append(new_cu)
    result = database.insert(data[1])
    if result[0]:
        return jsonify({"status": "success", "message": None, "data": [new_ac, new_cu]}), 200
    return jsonify({"status": "error", "message": result[1], "data": None}), 200
    
@server.route("/lists", methods=["GET", "POST"])
def lists():
    return jsonify(database.select()[1]), 200


@server.errorhandler(405)
def method_not_allow(error):
    return jsonify({"status": "error", "message": error, "data": None}), 405


@server.errorhandler(404)
def page_not_found(error):
    return jsonify({"status": "error", "message": error, "data": None}), 404


if __name__ == "__main__":
    server.run(debug=True)