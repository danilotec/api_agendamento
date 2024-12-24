from flask import Blueprint, jsonify, request
from .models import db, Barber, Appointment

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "message": "Bem-vindo ao sistema de agendamento de barbearia!"})

@main.route('/barbers', methods=['GET'])
def get_barbers():
    barbers = Barber.query.all()
    result = [{
        "id": barber.id,
        "name": barber.name,
        "available_hours": barber.available_hours
        } for barber in barbers]
    return jsonify(result)

@main.route('/barbers', methods=['POST'])
def add_barber():
    data = request.get_json()
    new_barber = Barber(
                        name=data['name'], # type: ignore
                        available_hours=data['available_hours']) # type: ignore
    
    db.session.add(new_barber)
    db.session.commit()
    return jsonify({"message": "Barbeiro adicionado com sucesso!"}), 201