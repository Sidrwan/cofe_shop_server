from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        image = db.Column(db.String, unique=True, nullable=False)
        price = db.Column(db.Text, nullable=True)
        def __repr__(self):
            return '<Products {} {}>'.format(self.title,)