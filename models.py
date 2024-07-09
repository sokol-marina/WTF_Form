"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

default_image = 'https://images.unsplash.com/photo-1578095551578-e226abbc63e9?q=80&w=2671&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

class Pet(db.Model):
    """Pet model"""
    __tablename__ = "pets"
    def __repr__(self):
        return f"Pet id={self.id} name ={self.name} - {self.species} >"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(225),  nullable=False)
    species = db.Column(db.Text,  nullable=False)
    photo_url = db.Column(db.Text,  nullable=True,default = default_image)
    age = db.Column(db.Integer,  nullable=True)
    notes = db.Column(db.Text,  nullable=True)
    available = db.Column(db.Boolean,  nullable=True, default = True)