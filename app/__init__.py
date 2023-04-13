"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqb6o2qv2dcb94bo9g-a.oregon-postgres.render.com",
        database="todo_sdhm",
        user="todo_sdhm_user",
        password="qWtoOKqOGRwNygc4zpehgwjZiVB3Epwp")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
