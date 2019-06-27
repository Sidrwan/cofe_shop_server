from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Models):
        title = db.Column(db.String, nullable=False)
        composition = db.Column(db.Text, nullable=False)
        price = db.Column(db.Text, nullable=True)
        weight = db.Column(db.Text, nullable=False)
    
        def __repr__(self):
            return '<Products {} {}>'.format(self.title,)