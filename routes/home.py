from flask import Blueprint, render_template, session, redirect

from models import Post
from db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  return render_template(
    'homepage.html',
    posts=posts,
    loggedIn = session.get('loggedIn')
    )

@bp.route('/login')
def login():
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()
  return render_template(
    'single-post.html',
    post=post,
    loggedIn = session.get('loggedIn')
    )