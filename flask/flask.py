from flask import Flask, request, redirect, render_template, session
import random

app = Flask(__name__)
app.secret_key = '123123123'

@app.route('/users', methods=['GET'])
def get_users():
    random_names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
    return render_template('users.html', names=random_names)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id % 2 == 0:
        return render_template('user.html', user_id=user_id)
    else:
        return 'Not Found', 404

@app.route('/books', methods=['GET'])
def get_books():
    random_books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
    return render_template('books.html', books=random_books)

@app.route('/books/<title>', methods=['GET'])
def get_book(title):
    transformed_title = title.capitalize()
    return render_template('book.html', title=transformed_title)

@app.route('/params', methods=['GET'])
def get_params():
    params = request.args
    return render_template('params.html', params=params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/users')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            session['username'] = username
            return redirect('/users')
        else:
            return 'Bad Request', 400
    else:
        return render_template('login.html')

@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return redirect('/login')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run()
