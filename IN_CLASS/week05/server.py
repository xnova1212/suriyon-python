from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

my_contacts = [
    {'id':'64122420220', 'name':'Phumin maliwan1','mobile':'095264971'},
    {'id':'64122420221', 'name':'Phumin maliwan2','mobile':'095264972'},
    {'id':'64122420222', 'name':'Phumin maliwan3','mobile':'095264973'},
    {'id':'64122420223', 'name':'Phumin maliwan4','mobile':'095264974'},
    {'id':'64122420224', 'name':'Phumin maliwan5','mobile':'095264975'},
]

@app.context_processor
def get_current_year():
    return {'date': datetime.utcnow()}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html", contacts=my_contacts)


@app.route('/contacts/<id>/detail')
def contact_detail(id):
    friend = None
    for c in my_contacts:
        if c['id'] == id:
            friend = c 
            break
    return render_template("detail.html", contacts=friend)


@app.route('/contacts/new_contact', methods=['GET','POST'])
def new_contact():
    if request.method == 'POST':
        contact = {'id': request.form['id'], 'name': request.form['name'], 'mobile': request.form['mobile']}
        my_contacts.append(contact)
        return redirect(url_for('contacts'))
    return render_template('new_contact.html', title='New Contact')


@app.route('/contacts/<id>/update', methods=['GET','POST'])
def update_contact(id):
    if request.method == 'POST':
        for c in my_contacts:
            if c['id'] == id:
                c['name'], c['mobile'] = request.form['name'], request.form['mobile']
                break
        return redirect(url_for('contacts'))    
    contact = None
    for c in my_contacts:
        if c['id'] == id:
            contact = c
            break
    return render_template('update_contact.html', contact=contact, title='Update Contact')


@app.route('/contacts/<id>/delete', methods=["GET", "POST"])
def delete_contact(id):
    for c in my_contacts:
        if c["id"] == id:
            my_contacts.remove(c)
            break
    return redirect(url_for("contacts"))


@app.route('/contacts/search', methods=["POST"])
def search_contact():
    search = request.form["search"]
    friend = []
    for c in my_contacts:
        if search.lower() in c["name"].lower():
            friend.append(c)
    return render_template('contacts.html', contacts = friend)

if __name__== '__main__':
    app.run(debug=True)
