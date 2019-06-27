from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Models):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<Products {} {}>'.format(self.title, self.url)