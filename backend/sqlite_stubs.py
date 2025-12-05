"""Creates the stub in the database"""
import sqlite3
import json

def get_db_connection():
    """We get connection to the database"""
    conn = sqlite3.connect('database.db')
    return conn

def execute_sql_command(query, params=()):
    """Gets the database connection then executes a sql statement"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    route = cursor.fetchone()
    conn.commit()
    conn.close()

    return route

def insert_user(user_test):
    """Creates the user table if it does not exist"""
    conn = get_db_connection()
    cursor = conn.cursor()

    for user in user_test:
        cursor.execute('''
             INSERT OR IGNORE INTO User (username, password) VALUES (?, ?)
        ''', user)
    conn.commit()
    conn.close()

def insert_settings_data(data):
    """Inserts settings into data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    for entry in data:
        cursor.execute('''INSERT INTO Settings (dark_mode, text_size, image_size, high_contrast)
                       VALUES (?, ?, ?, ?)''',
                       (entry["dark_mode"],
                       entry["text_size"],
                       entry["image_size"],
                        entry["high_contrast"]))
    conn.commit()
    conn.close()

def insert_customer_data(data):
    """Insert customer date into the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    for entry in data:
        cursor.execute('''INSERT INTO Customer
                         (first_name, last_name, phone_no, email_address, address, postal_code, animal_type)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (entry["first_name"], entry["last_name"], entry["phone_no"],
                          entry["email_address"],
                           entry["address"], entry["postal_code"], entry["animal_type"]))

    conn.commit()
    conn.close()

def insert_pet_data(data):
    """Inserts pet data into the Database"""
    conn = get_db_connection()
    cursor = conn.cursor()

    for entry in data:
        cursor.execute('''INSERT INTO Pets
                          (name, breed, specific_breed, service_type, hyper_allergenic, house_trained, img_src, animal_type)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (entry["name"],
                            entry["breed"],
                            entry["specific_breed"],
                            entry["service_type"],
                            entry["hyper_allergenic"],
                            entry["house_trained"],
                            entry['img_src'],
                            entry["animal_type"]),)
    conn.commit()
    conn.close()

def insert_item_data(data):
    """Inserts items into the Database"""
    conn = get_db_connection()
    cursor = conn.cursor()

    for entry in data:
        cursor.execute('''INSERT INTO Items
                       (name, description, cost, stock, category)
                       VALUES (?, ?, ?, ?, ?)''',
                        (entry["name"],
                        entry["description"],
                        entry["cost"],
                        entry["stock"],
                        entry["category"]),)
    conn.commit()
    conn.close()

def validate_settings(data):
    """Validating Settings"""
    valid_settings = []
    invalid_settings = []
    for entry in data:
        if (entry["text_size"] in ["0", "1", "2"] and entry["image_size"] in ["0", "1", "2"]
                and entry["dark_mode"] in ["True", "False"] and entry["high_contrast"] in
                ["True", "False"]):
            valid_settings.append(entry)
        else:
            invalid_settings.append(entry)
    return valid_settings, invalid_settings

# Main function to populate data
def populate_data():
    """Initialize tables"""
    # Data samples from before
    user_test = [
        ('abc12345', '1234567890'),
        ('testuser', 'password123'),
        ('tay', '093')
    ]
    true_settings = [
        {"dark_mode": "True", "text_size": "2", "image_size": "2", "high_contrast": "False"},
        {"dark_mode": "False", "text_size": "1", "image_size": "1", "high_contrast": "True"},
        {"dark_mode": "True", "text_size": "0", "image_size": "2", "high_contrast": "True"}
    ]
    false_settings = {
        "dark_mode": "Hexagon",
        "text_size": "12",
        "image_size": "42",
        "high_contrast": "Juice"
    }
    customer_data = [
        {
            'first_name': 'Mark',
            'last_name': 'Zuckerberg',
            'phone_no': 1234567890,
            'email_address': 'mark.zuckerberg@facebook.com',
            'address': '123 Main St',
            'postal_code': '12345',
            'animal_type': 'dog'
        },
        {
            'first_name': 'Elon',
            'last_name': 'Musk',
            'phone_no': 9876543210,
            'email_address': 'elon.musk@spacex.com',
            'address': '456 Elm St',
            'postal_code': '54321',
            'animal_type': 'dog'
        },
        {
            'first_name': 'Jeff',
            'last_name': 'Bezos',
            'phone_no': 5555555555,
            'email_address': 'jeff.bezos@amazon.com',
            'address': '789 Oak St',
            'postal_code': '67890',
            'animal_type': 'cat'
        }
    ]
    pets_valid = [
    {
      "name": "Gronk",
      "breed": "Pitbull",
      "specific_breed": "True",
      "service_type": "True",
      "hyper_allergenic": "True",
      "house_trained": "True",
      "img_src": "dog1.png",
      "animal_type": "dog"
    },
    {
      "name": "Bella",
      "breed": "Labrador",
      "specific_breed": "True",
      "service_type": "True",
      "hyper_allergenic": "True",
      "house_trained": "False",
      "img_src": "dog2.png",
      "animal_type": "dog"
    },
    {
      "name": "Max",
      "breed": "Bulldog",
      "specific_breed": "True",
      "service_type": "True",
      "hyper_allergenic": "False",
      "house_trained": "True",
      "img_src": "dog3.png",
      "animal_type": "dog"
    },
    {
      "name": "Sadie",
      "breed": "Poodle",
      "specific_breed": "True",
      "service_type": "True",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "dog4.png",
      "animal_type": "dog"
    },
    {
      "name": "Rocky",
      "breed": "German Shepherd",
      "specific_breed": "True",
      "service_type": "False",
      "hyper_allergenic": "True",
      "house_trained": "True",
      "img_src": "dog5.png",
      "animal_type": "dog"
    },
    {
      "name": "Charlie",
      "breed": "Golden Retriever",
      "specific_breed": "True",
      "service_type": "False",
      "hyper_allergenic": "True",
      "house_trained": "False",
      "img_src": "dog6.png",
      "animal_type": "dog"
    },
    {
      "name": "Luna",
      "breed": "Shih Tzu",
      "specific_breed": "True",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "True",
      "img_src": "dog7.png",
      "animal_type": "dog"
    },
    {
      "name": "Zoe",
      "breed": "Chihuahua",
      "specific_breed": "True",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "dog8.png",
      "animal_type": "dog"
    },
    {
      "name": "Toby",
      "breed": "Beagle",
      "specific_breed": "False",
      "service_type": "True",
      "hyper_allergenic": "True",
      "house_trained": "True",
      "img_src": "dog9.png",
      "animal_type": "dog"
    },
    {
      "name": "Bailey",
      "breed": "Boxer",
      "specific_breed": "False",
      "service_type": "True",
      "hyper_allergenic": "True",
      "house_trained": "False",
      "img_src": "dog10.png",
      "animal_type": "dog"
    },
    {
      "name": "Milo",
      "breed": "Dalmatian",
      "specific_breed": "False",
      "service_type": "True",
      "hyper_allergenic": "False",
      "house_trained": "True",
      "img_src": "dog11.png",
      "animal_type": "dog"
    },
    {
      "name": "Sasha",
      "breed": "Siamese",
      "specific_breed": "False",
      "service_type": "True",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "cat12.png",
      "animal_type": "cat"
    },
    {
      "name": "Samson",
      "breed": "Maine Coon",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "True",
      "house_trained": "True",
      "img_src": "cat13.png",
      "animal_type": "cat"
    },
    {
      "name": "Daisy",
      "breed": "Persian Cat",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "True",
      "house_trained": "False",
      "img_src": "cat14.png",
      "animal_type": "cat"
    },
    {
      "name": "Oscar",
      "breed": "Burmese",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "True",
      "img_src": "cat15.png",
      "animal_type": "cat"
    },
    {
      "name": "Maggie",
      "breed": "British Shorthair",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "cat16.png",
      "animal_type": "cat"
    },
    {
      "name": "Lotus",
      "breed": "British Shorthair",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "cat17.png",
      "animal_type": "cat"
    },
    {
      "name": "Max",
      "breed": "Sphynx",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "cat18.png",
      "animal_type": "cat"
    },
    {
      "name": "Jessica",
      "breed": "British Shorthair",
      "specific_breed": "False",
      "service_type": "False",
      "hyper_allergenic": "False",
      "house_trained": "False",
      "img_src": "cat19.png",
      "animal_type": "cat"
    }
  ]

    pets_invalid = [
        {'name': 'Bobby',
          'breed': 'Golden Retriever',
            'specific_breed': 1,
              'service_type': 5,
                'hyper_allergenic': False,
                  'house_trained': False},
        {'name': 'Sally',
          'breed': 'Labrador',
            'specific_breed': 'yes',
              'service_type': 'no',
                'hyper_allergenic': 'maybe',
                  'house_trained': 'pizza'}
    ]
    items = [
        {'name': 'Wobble Wag Giggle Ball',
        'description': 'Interactive dog toy that giggles when shaken, rolled, or picked up.',
        'cost': 14.99,
        'stock': 20,
        'category': "Toys"},
        {'name' : 'Kibbles n bits',
         'description': '45 Lb Original Savory Beef and chciken Flavors Dry Dog Food.',
         'cost': 46.99,
         'stock': 50,
         'category': "Food"},
        {'name': "HappyCare Textiles Dog Bed",
         'description': 'One side features ocean Blue Micro mink soft and warm in the winter.',
         'cost': 24.89,
         'stock': 20,
         'category': "Beds"},
        {'name': "Waterproof dog collar",
         'description': "Waterproof dog collar made from high-quality PVC-coated webbing.",
         'cost': 7.95,
         'stock': 35,
         'category': 'Accessories'},
         {'name': "Miraculous Treats",
          'description': "Delicious treats for your pet!",
          'cost': 10.99,
          'stock': 18,
          'category': "Food"}
    ]

    valid_settings, invalid_settings = validate_settings(true_settings + [false_settings])
    insert_user(user_test)
    insert_settings_data(valid_settings)
    insert_customer_data(customer_data)
    insert_pet_data(pets_valid)
    insert_item_data(items)
    # I LOVE STACK OVERFLOW!!!!!!!!!
    print("Inserted valid settings:", json.dumps(valid_settings, indent=4))
    print("Skipped invalid settings:", json.dumps(invalid_settings, indent=4))
    print("Inserted customer info:", json.dumps(customer_data, indent=4))
    print("Inserted valid dogs:", json.dumps(pets_valid, indent=4))
    print("Skipped invalid dogs:", json.dumps(pets_invalid, indent=4))
    print("Inserted shop data:", json.dumps(items, indent=4))

if __name__ == "__main__":
    populate_data()
