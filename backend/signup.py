"""Signup file that uses get requests for the application,
also obtains get and posts requests for the quiz"""
from flask import request, jsonify
from sqlite_stubs import insert_customer_data, execute_sql_command

#Stub data to test post request
quiz_answer_valid = [
    {
        'specific_breed': "False",
        'service_type': "True",
        'hyper_allergenic': "False",
        'house_trained': "True"
    },
    {
        'specific_breed': "True",
        'service_type': "False",
        'hyper_allergenic': "True",
        'house_trained': "False",
    }
]
quiz_answer_invalid = {
        'specific_breed': "what",
        'service_type': "1",
        'hyper_allergenic': "3",
        'house_trained': "none"
}
pets_invalid = [
    {
        'name': 'Bobby',
        'breed': 'Golden Retriever',
        'specific_breed': 1,
        'service_type': 5,
        'hyper_allergenic': False,
        'house_trained': False
    },
    {
        'name': 'Sally',
        'breed': 'Labrador',
        'specific_breed': 'yes',
        'service_type': 'no',
        'hyper_allergenic': 'maybe',
        'house_trained': 'pizza'
    }
]
pets_valid = [
    {
        'name': 'Gronk',
        'breed': 'Pitbull',
        'specific_breed': "True",
        'service_type': "True",
        'hyper_allergenic': "False",
        'house_trained': "False"
    },
    {
        'name': 'Matt',
        'breed': 'Beagle',
        'specific_breed': "False",
        'service_type': "False",
        'hyper_allergenic': "True",
        'house_trained': "True"
    }
]

#Create the get request for the application
def application():
    """Signs the user up and adds to database"""
    try:
        user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'phone_no': request.form['phone_no'],
            'email_address': request.form['email_address'],
            'address': request.form['address'],
            'postal_code': request.form['postal_code'],
            'animal_type': request.form['animal_type']
        }
        # Insert user_data into database
        insert_customer_data([user_data])

        return jsonify({'message': 'Signup successful'}), 201
    except KeyError as error:
        return jsonify({'error': f'Missing Field: {str(error)}'}), 400

def check_if_bool(value, error):
    """Helper function to identify bools which accepts True and False only"""
    if value is None:
        return False  # Consider None as False
    if value == "True":
        return True
    if value == "False":
        return False

    raise ValueError(error)

#Create the get and post request for the quiz
def get_questionnarie():
    """Get information from quiz and then post
    information depending on what they selected"""
    error_msg = "Invalid boolean value"
    try:
        specific_breed = check_if_bool(request.args.get('specific_breed'), error_msg)
        service_type = check_if_bool(request.args.get('service_type'), error_msg)
        hyper_allergenic = check_if_bool(request.args.get('hyper_allergenic'), error_msg)
        house_trained = check_if_bool(request.args.get('house_trained'), error_msg)

        return jsonify({'specific_breed': specific_breed,
                 'service_type': service_type,
                 'hyper_allergenic': hyper_allergenic,
                 'house_trained': house_trained})

    except ValueError as error:
        return jsonify({"Error": str(error)})

def post_questionnarie():
    """Gets data from database and checks if its successful in obtaining the information"""
    error_msg = "Invalid boolean value"
    try:
        specific_breed = check_if_bool(request.json['specific_breed'], error_msg)
        service = check_if_bool(request.json['service_type'], error_msg)
        hyper_allergenic = check_if_bool(request.json['hyper_allergenic'], error_msg)
        house_trained = check_if_bool(request.json['house_trained'], error_msg)

        return jsonify({'message': "200. Succeeded in getting the information",
                        'specific_breed': specific_breed,
                        'service_type': service,
                        'hyper_allergenic': hyper_allergenic,
                        'house_trained': house_trained})

    except ValueError as error:
        return jsonify({"Error": str(error)})

def get_user(email_address):
    """Fetches user data from the database based on the email address."""
    query = "SELECT * FROM Customer WHERE email_address = ?"
    params = (email_address,)
    is_user = execute_sql_command(query, params)
    if is_user:
        return {
            'first_name': is_user[0],
            'last_name': is_user[1],
            'phone_no': is_user[2],
            'email_address': is_user[3],
            'address': is_user[4],
            'postal_code': is_user[5],
            'animal_type': is_user[6]
        }
    return None

def user():
    """Endpoint to fetch user data based on email address"""
    email_address = request.args.get('email_address')
    if not email_address:
        return jsonify({"Error": "Email address is required"}), 400

    is_user = get_user(email_address)
    if is_user:
        return jsonify(is_user)
    return jsonify({"Error": "User not found"}, 404)
