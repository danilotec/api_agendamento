from . import db
import sqlalchemy as sa

class Barber(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    available_hours = sa.Column(sa.String(200), nullable=False)

class Appointment(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    client_name = sa.Column(sa.String(100), nullable=False)
    barber_id = sa.Column(sa.Integer, sa.ForeignKey('barber.id'), nullable=False)
    appointment_time = sa.Column(sa.String(100), nullable=False)

def init_db(app):
    with app.app_context():
        sa.create_all()