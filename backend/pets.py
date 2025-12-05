"""gets pets"""
from sqlite_stubs import get_db_connection
from flask import jsonify

def get_pets():
    """Retrieves all pets and sends back a JSON with the pet data."""

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, name, breed, specific_breed,
                        service_type, hyper_allergenic, house_trained, 
                       img_src, animal_type FROM Pets""")
        all_pets = cursor.fetchall()

        if all_pets:
            pets_list = {
                "dogs": [],
                "cats": []
            }
            # Convert the list of tuples into a list of dictionaries
            for pet in all_pets:
                pet_data = {
                        'id': pet[0],
                        'name': pet[1],
                        'breed': pet[2],
                        'specific_breed': pet[3],
                        'service_type': pet[4],
                        'hyper_allergenic': pet[5],
                        'house_trained': pet[6],
                        'img_src': pet[7],
                }
                if pet[8] == "dog":
                    pets_list["dogs"].append(pet_data)
                else:
                    pets_list["cats"].append(pet_data)
            return jsonify(pets_list), 200

        return jsonify({"Error": "No pets found in the database."}), 404
    except TypeError as error:
        return jsonify({"Error": str(error)}), 500
