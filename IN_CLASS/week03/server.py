from flask import Flask, render_template


app = Flask(__name__)


my_contacts = [
  { "id": "64122420216", "name": "Pongpisut Sishuloed1", "mobile": "0666666666" },
  { "id": "64122420217", "name": "Pongpisut Sishuloed2", "mobile": "0666666666" },
  { "id": "64122420218", "name": "Pongpisut Sishuloed3", "mobile": "0666666666" },
  { "id": "64122420219", "name": "Pongpisut Sishuloed4", "mobile": "0666666666" },
  { "id": "64122420220", "name": "Pongpisut Sishuloed5", "mobile": "0666666666" }
]


@app.route("/") # decorator
def index():
  return render_template("index.html")



@app.route("/contacts") # decorator
def contacts():
  return render_template("contacts.html", contacts = my_contacts)


@app.route("/contacts/<id>/detail")
def contact_detail(id):
  friend = None
  for c in my_contacts:
    if c["id"] == id:
      friend = c
      break
  return render_template("detail.html", contact = friend)



if __name__ == "__main__":
  app.run(debug=True)
