from models import User, Post, Comment, Vote
from db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='CesarSig', email='cesar@gmail.com"', password='abcd1234'),
  User(username='Samantha', email='sam@gmail.com"', password='1234abcd'),
  User(username='Anna', email='anna@gmail.com', password='password'),
])
db.commit()

# insert posts
db.add_all([
  Post(title="My first post on my new app!", post_url="https://www.apple.com/", user_id=1),
  Post(title="Fancing new tech coming out soon!", post_url="https://www.macrumors.com/", user_id=2),
  Post(title='Please checkout my portfolio', post_url="https://cesarsiguencia.github.io/my-react-portfolio/", user_id=1),
  Post(title='Anyone know React well and can help me?', post_url='https://www.reactenlightenment.com/', user_id=3),
  Post(title='Some technical interview advice I found!', post_url='https://learntocodewith.me/posts/technical-interview/', user_id=2)
])
db.commit()

# insert comments
db.add_all([
  Comment(comment_text="Congratulations on your first post!", user_id=2, post_id=1),
  Comment(comment_text="Jealous of your portfolio! :)", user_id=2, post_id=3),
  Comment(comment_text="Teach me how to do this!", user_id=3, post_id=3),
  Comment(comment_text='I can help! Message me', user_id=1, post_id=4),
  Comment(comment_text='Thanks for sharing this!', user_id=2, post_id=5)
])
db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=2, post_id=1),
  Vote(user_id=2, post_id=3),
  Vote(user_id=3, post_id=3),
  Vote(user_id=1, post_id=5),
  Vote(user_id=2, post_id=5),
  Vote(user_id=2, post_id=4),
])
db.commit()

db.close()







