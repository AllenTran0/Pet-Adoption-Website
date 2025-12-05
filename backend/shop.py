"""Get items in shop"""
from sqlite_stubs import get_db_connection
from flask import jsonify

def get_items():
    """Retrieves the shop data from database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT id, name, description, cost, stock, category FROM Items")
        all_items = cursor.fetchall()

        if all_items:
            item_list = {
                "Toys": [],
                "Food": [],
                "Beds": [],
                "Accessories": []
            }
            # Convert the list of tuples into a list of dictionaries
            for item in all_items:
                item_data = {
                        'id': item[0],
                        'name': item[1],
                        'description': item[2],
                        'cost': item[3],
                        'stock': item[4],
                        'category': item[5]
                }
                if item[5] == "Toys":
                    item_list["Toys"].append(item_data)
                elif item[5] == "Food":
                    item_list["Food"].append(item_data)
                elif item[5] == "Beds":
                    item_list["Beds"].append(item_data)
                elif item[5] == "Accessories":
                    item_list["Accessories"].append(item_data)
            return jsonify(item_list), 200

        return jsonify({"Error": "No items found in the database."}), 404
    except TypeError as error:
        return jsonify({"Error": str(error)}), 500
