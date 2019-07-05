from flask import Flask, request
app = Flask(__name__)

@app.route('/data', methods=['POST'])
def upload_new_file_on_warehouse():
    """Insert into database, move the raw data file from Temp folder to DB folder"""
    # Insert into database
    return

@app.route('/data', methods=['GET'])
def fetch():
    return
    