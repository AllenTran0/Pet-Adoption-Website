"""Updated Vizualization"""
from flask import request, jsonify
from sqlite_stubs import get_db_connection
from signup import check_if_bool

def settings():
    """Retrieves Settings and sends back a JSON with the settings."""

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dark_mode, text_size, image_size, high_contrast"+
                       " FROM Settings ORDER BY id DESC LIMIT 1")
        latest_settings = cursor.fetchone()

        if latest_settings:
            dark_mode, text_size, image_size, high_contrast = latest_settings
            return jsonify({
                'dark_mode': dark_mode,
                'text_size': text_size,
                'image_size': image_size,
                'high_contrast': high_contrast
            }), 200
        return jsonify({"Error": "No settings found in the database."}), 404
    except TypeError as error:
        return jsonify({"Error": str(error)}), 500
def post_settings():
    """Get The settings"""
    error_msg = "text_size and image_size must be between 0 and 2"
    try:
        dark_mode = check_if_bool(request.json.get("dark_mode"), error_msg)
        text_size = int(request.json.get("text_size"))
        image_size = int(request.json.get("image_size"))
        high_contrast = check_if_bool(request.json.get("high_contrast"), error_msg)

        # Validate ranges for text_size and image_size
        if text_size not in range(3) or image_size not in range(3):
            raise ValueError(error_msg)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
        """INSERT INTO
        Settings (dark_mode, text_size, image_size, high_contrast)
        VALUES (?, ?, ?, ?)""",
        (dark_mode, text_size, image_size, high_contrast)
        )
        conn.commit()


        return jsonify({
            'message': "200. Succeeded in getting the settings",
            'dark_mode': dark_mode,
            'text_size': text_size,
            'image_size': image_size,
            'high_contrast': high_contrast
        }), 200
    except (TypeError, ValueError) as error_msg:
        return jsonify({"Error": str(error_msg)}), 400
