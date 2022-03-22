from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model_document = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/doc_form', methods=['GET'])
def doc_form():
    return render_template('doc_form.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_document = request.form['id_document']
    title_document = request.form['title_document']
    num_document_pages = request.form['num_document_pages']
    cathegory = request.form['category']
    author = request.form['author']
    p = Document(id_document=id_document, title_document=title_document, num_document_pages=num_document_pages, category=cathegory, author=author)
    model_document.append(p)
    return render_template('document_detail.html', value=p)


@app.route('/document')
def document():
    data_doc = [(i.id_document, i.title_document, i.num_document_pages, i.category, i.author) for i in model_document]
    print(data_doc)
    return render_template('document.html', value=data_doc)


if __name__ == '__main__':
    app.run()
