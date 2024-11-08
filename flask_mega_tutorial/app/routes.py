from app import app
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit
import sqlalchemy as sa
from app import db
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    return "HELLO BRO"

@app.route('/login', methods=['POST',])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = db.session.scalar(
        sa.select(User).where(User.username == 'add the json handling from the body of request here')
    )
    if user is None or not user.check_password('add the json handling from the body of the request here'):
        flash('Invalid username or password')
        return redirect(url_for('login'))
    #TODO pull remember me flag from json request body
    login_user(user, remember=True)
    next_page = request.args.get('next')
    if not next_page or urlsplit(next_page).netloc != '':
        next_page = url_for('index')
    return redirect(next_page)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return user
