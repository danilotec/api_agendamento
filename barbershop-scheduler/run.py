from app import create_app
from app.models import db

def init_db(app):
    with app.app_context():
        db.create_all()

app = create_app()

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)
