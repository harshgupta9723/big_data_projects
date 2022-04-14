# The code is to provide data for analysis and visualisation
# The data is provided in json format

import os
import sqlalchemy
from sqlalchemy import create_engine
import pymysql
import random
import time
import json

def get_connection():

    #get environment variable
    user=os.getenv("DBUSER")
    passwd=os.getenv("DBPASS")
    host=os.getenv("DBHOST")
    database=os.getenv("DBNAME")

    #conection string
    con_string="mysql+pymysql://{}:{}@{}/{}".format(user, passwd, host, database)

    #create engine
    sqlEngine = create_engine(con_string, pool_recycle=3600)
    db = sqlEngine.raw_connection()
    return db

def get_jobs():
    db = get_connection()
    cur = db.cursor()
    
    query = "SELECT * FROM Persons"
    cur.execute(query)
    
    job_list = cur.fetchall()
    
    keys = []
    data = []

    for row in job_list:
        keys.append(row[0])
        data.append({"salary":row[1], "expenditure":row[2], "saving":row[3], "investment":row[4]})

    #create a dictionary of keys and values
    data_dict = dict(zip(keys, data))
    
    cur.close()
    db.close()
    
    return json.dumps(data_dict)

def insert_data():
    db = get_connection()
    cur = db.cursor()
    
    salary = random.randint(1,100000)
    investment = int(salary-(salary*20/100))
    expenditure = random.randint(1,salary-investment)
    saving = salary - expenditure
        
    query = "INSERT INTO Persons (salary, expenditure, saving, investemnt)"
    values = "VALUES ({}, {}, {}, {})".format(int(salary), int(expenditure), int(saving), int(investment))
    query = query + values

    cur.execute(query)
    print(values)
    db.commit()
    
    cur.close()
    db.close()
    
if __name__=='__main__':
    insert_data()
    #run insert function to insert data into database endlessly
    while True:
        insert_data()
        time.sleep(1)
