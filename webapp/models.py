from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        price = db.Column(db.Text, nullable=True)
        image = db.Column(db.String, unique=True, nullable=False)
    
        def __repr__(self):
            return '<Products {} {}>'.format(self.title,)