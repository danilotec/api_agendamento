from app import create_app
from app.models import init_db


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    init_db(app)