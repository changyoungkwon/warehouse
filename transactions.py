from pathlib import Path
from os import sys
import psycopg2
import configparser
from rawdatarinator import raw as rparser

config_path = Path("./config.ini")

class Database:
    """Database wrapper"""
    def __init__(self, config_path):
        try:
            parser = configparser.ConfigParser()
            parser.read(config_path)
            self.config = dict(parser['DATABASE'])
            self.config['tablename'] = 'RawData'
        except configparser.Error:
            print("[error]db config file error")
            sys.exit(1)

    def upload(self, filepath): 
        """insert parsed database"""
        try:
            # parse raw data, move to ismrmrd config
            
        
        try:
            connection = psycopg2.connect(self.config)
            cursor = connection.cursor()
            cursor.execute("")
        except psycopg2.Error:
            print("[error]db insert error")
        
        

def database_test(config_path): 
    """Connect to database, return the cursor"""
    try:
        parser = configparser.ConfigParser()
        parser.read(config_path)
        db_config = dict(parser['DATABASE'])
    except configparser.Error:
        print("error looking for database config file") 
        return -1
    # define transaction
    db_name = db_config['dbname']
    table_name = 'RawData'
    try:
        connection = psycopg2.connect(db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM {}.{}".format(db_name, table_name))
        print(cursor.fetchone())
    except psycopg2.Error:
        print("error interacting withj to database")
    finally:
        cursor.close()
        connection.close()
    print("db_test done")
    return 0

def upload_mrdata(filepath) : 
    """

    """
    return

def download_mrdata(filename) : 
    return

def fetch_mrdata(header_only=False) : 
    return
