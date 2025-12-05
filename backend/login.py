'''Importing moduels from to do get and post requests'''
# import sqlite3
from flask import request, jsonify
from sqlite_stubs import execute_sql_command

def login():
    '''
    creating the username and password for the login
    '''
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            raise ValueError("Cannot have nothing in username or password")

        #May change later to turn into one function for modularity
        query = "SELECT * FROM User WHERE username = ?"
        params = (username,)
        user = execute_sql_command(query, params)

        if user and user[2] == password:
            return jsonify({'username' : username, 'message': 'Login successful'}), 200
        raise ValueError("Invalid username or password")

    except ValueError as error:
        return jsonify({'error': str(error)}), 400
