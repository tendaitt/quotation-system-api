from src import create_app
from src.database import db

# create the database and tables
app = create_app()
db.init_app(app)

with app.app_context():
    db.create_all()
