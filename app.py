from flask import Flask, request 
from flask_smorest import abort


app = Flask(__name__)

@app.get("/")
def get_info():
    return "Testing"