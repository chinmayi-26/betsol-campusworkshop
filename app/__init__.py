"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaadc3hp8u791gtisfg-a.oregon-postgres.render.com",
        database="todo_he8j",
        user="root",
        password="TFyaXGTjanYg9O0Wn6hUOMw84jqUQzy5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
