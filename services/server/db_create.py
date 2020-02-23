from src import create_app, db

# create the database and tables
app = create_app()

with app.app_context():
    db.create_all()
