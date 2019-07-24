from flask import Flask, request, jsonify
app = Flask(__name__)

"""App Warehouse moves raw-data files in TEMP folder to proper directory, and add the statics on database

While insertion, 
Warehouse-client moves raw-data files from a client to the designated TEMP folder. 
If client moves the raw-data file successfully, client sends HTTP request signal to server
Receiving request, Warehouse-server checks the raw-data file, move to proper directory, inserting on database. 
After all, server responds whether all actions are successful or not(ajax, socket)

While fetch
Warehouse-client requests the raw-data file with specific conditions. Conditions is sent via HTTP request
Warehouse-server responds with JSON format, or the header file.
"""

@app.route('/data', methods=['POST'])
def upload_file():
    """Insert into database, move the raw data file from Temp folder to DB folder"""
    # Parse the raw-data file. Calculate the entity
    try: 
      parser = Parser()
      meas = parser.read(header_only=True)  # give an database column entity 
    except:
      print("[error]unable to parse the raw data")
      sys.exit(1)

    # Move the file from pre-defined temporary folder to designated database folder
    try:
      filepath = request.args['filename']
      dst_dir = hash(entity)
      path.move(filepath, dst_dir)
    except:

    # Insert into database
    try:
      database = Database(config)
      database.connect()
      meas['filepath'] = 
      database.insert(meas)
    except:
      print("[error]unable to insert on database")
      sys.exit(1)

    # Post-process
    pipeline = Pipeline(config['POSTPROCESS'])
    postprocess_result = pipeline.execute(filepath)

    return jsonify({'postprocess': postprocess_result})

@app.route('/data', methods=['GET'])
def fetch():
    """Fetch headers' info from database, optionally download the raw data file"""
    # Lookup the matched entities from the MRdata table
    
    
    # If nothing matches, return empty object

    # If there's something matches, return the headers, and filepath
    return
    