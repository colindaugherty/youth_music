from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

Flask.secret_key = "random"

class UserNotFoundError(Exception):
    pass

# Simple user class base on UserMixin
# http://flask-login.readthedocs.org/en/latest/_modules/flask/ext/login.html#UserMixin
class User(UserMixin):
    '''Simple User class'''
    USERS = {
        'worship-leader':'newsong',
        'newsong':'worship',
        'newsongyouth':'youthworship'
    }

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        '''Return user instance of id, return None if not exist'''
        try:
            return self_class(id)
        except UserNotFoundError:
            return None


# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.get(id)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('worship'))
    else:
        return render_template('login.html')


@app.route('/login/check', methods=['post'])
def login_check():
    # validate username and password
    user = User.get(request.form['username'])
    if (user and user.password == request.form['password']):
        login_user(user)
        return redirect(url_for('admin'))
    else:
        flash('Username or password incorrect')

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/worship")
def worship():
    pass

@app.route("/help")
def help():
    pass

if __name__ == "__main__":
    app.run()
