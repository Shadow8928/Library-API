from flask import Flask, jsonify, request
app = Flask(__name__)
books = [
    {'id': '978-0132350884', 'title': 'Clean Code', 'author': 'Robert C. Martin', 'status': "Available"},
    {'id': '978-1491901416', 'title': 'Eloquent JavaScript', 'author': 'Marijn Haverbeke', 'status': "Unavailable"},
    {'id': '978-0596007422', 'title': 'Code Complete', 'author': 'Steve McConnell', 'status': "Available"}
]
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)
@app.route('/books/available', methods=['GET'])
def available_books():
    av_book = []
    for book in books:
        if book['status'] == "Available":
            av_book.append(book)
    return (av_book)
@app.route('/books/unavailable', methods=['GET'])
def unavailable_books():
    av_book = []
    for book in books:
        if book['status'] == "Unavailable":
            av_book.append(book)
    return (av_book)
@app.route('/books/add', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': data['id'],
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201
if __name__ == '__main__':
    app.run(debug=True)
