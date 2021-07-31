"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app_tstr import db #had to change to new file because email validation dependcy not working
from models import User, Message, Follows, Likes


db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    db.session.bulk_insert_mappings(Follows, DictReader(follows))


db.session.commit()

# make sure no spaces between name of column listings in csv.file
with open('generator/likes.csv') as likes:
    db.session.bulk_insert_mappings(Likes, DictReader(likes))


db.session.commit()