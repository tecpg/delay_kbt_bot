from cmath import cos
from csv import DictReader, writer
import csv
import datetime
from lib2to3.pgen2 import driver
import pprint
from pydoc import stripid
import random
import string
import sys
from unittest import result
from urllib import request
import requests
from bs4 import BeautifulSoup as soup
import time
from wsgiref import headers
# importing webdriver from selenium
import requests
import os
import time
import io
import requests
import mysql.connector
from mysql.connector import errorcode

from lxml import etree
from datetime import datetime
from datetime import timedelta
from datetime import date
from wp_post_api_bot import wp_post
import kbt_load_env
from consts import global_consts as gc
import kbt_funtions



global csv_data
csv_f = gc.VENASBET_BTTS_CSV


session = requests.Session()
my_headers = gc.MY_HEARDER
dt = []

p_date = gc.PRESENT_DAY_DATE
# calculating end date by adding 4 days
x_date =  gc.YESTERDAY_DATE



def get_today_prediction(bs, set_date):
    url = "https://venasbet.com/index.php/handicap?dt="

    try:
        # Request the webpage
        webpage = requests.get(url + str(set_date), headers=my_headers)
        webpage.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.RequestException as e:
        print(f"Failed to fetch the webpage: {e}")
        return

    # Parse the webpage
    bs = bs(webpage.content, "html.parser")
    dom = etree.HTML(str(bs))

    # Get all tables on the page
    tables = bs.findChildren('table')
    if not tables:  # Check if no tables are found
        print("No tables found on the webpage.")
        return

    web_table = tables[0]
    rows = web_table.findChildren(['tr'])
    tr_count = len(rows)

    if tr_count <= 1:  # Check if there are no rows beyond the header
        print("Table has no data rows.")
        return

    print("Table has ", tr_count - 1, " rows")

    # Open CSV file for writing
    try:
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
            dt = []

            for x in range(tr_count - 1):
                i = str(1 + x)

                try:
                    # Extract data using XPath
                    timez = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[1]')[0].text.strip()
                    leagues = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[2]')[0].text
                    home_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[3]/text()[1]')[0].strip()
                    away_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[3]/text()[2]')[0].strip()
                    picks = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[4]')[0].text

                    # Prepare prediction data
                    results = "N/A"
                    odds = kbt_funtions.get_random_odd_2()
                    source = "venasbet_handicap"
                    flag = ""
                    match_date = set_date
                    match_code = kbt_funtions.get_code(8)
                    score = ""

                    prediction = [
                        leagues,
                        kbt_funtions.remove(home_team + " vs " + away_team),
                        picks,
                        odds,
                        kbt_funtions.remove(timez),
                        score,
                        match_date,
                        flag,
                        results,
                        match_code,
                        source,
                    ]
                    dt.append(prediction)
                except IndexError as e:
                    print(f"Failed to process row {i}: {e}")

            # Write all predictions to the CSV
            thewriter.writerows(dt)

        print("Predictions saved to CSV:", dt)
    except Exception as e:
        print(f"Failed to write to the CSV file: {e}")

def get_previous_prediction(nbs, set_previous_date):
    url = "https://venasbet.com/index.php/handicap?dt="

    try:
        # Request the webpage
        webpage = requests.get(url + str(set_previous_date), headers=my_headers)
        webpage.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.RequestException as e:
        print(f"Failed to fetch the webpage: {e}")
        return

    # Parse the webpage
    nbs = nbs(webpage.content, "html.parser")
    dom = etree.HTML(str(nbs))

    # Get all tables on the page
    tables = nbs.findChildren('table')
    if not tables:  # Check if no tables are found
        print("No tables found on the webpage.")
        return

    web_table = tables[0]
    rows = web_table.findChildren(['tr'])
    tr_count = len(rows)

    if tr_count <= 1:  # Check if there are no rows beyond the header
        print("Table has no data rows.")
        return

    print("Table has ", tr_count - 1, " rows")

    # Open CSV file for writing
    try:
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
            dt = []

            for x in range(tr_count - 1):
                i = str(1 + x)

                try:
                    # Extract data using XPath
                    timez = "N/A"  # Default value if not available
                    leagues = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[1]')[0].text
                    home_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[2]/text()[1]')[0].strip()
                    away_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[2]/text()[2]')[0].strip()
                    picks = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[3]')[0].text
                    score = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[4]/strong')[0].text

                    # Prepare result and prediction data
                    results = kbt_funtions.get_result(picks, score)
                    odds = kbt_funtions.get_random_odd()
                    source = "venasbet_handicap"
                    flag = ""
                    match_date = set_previous_date
                    match_code = kbt_funtions.get_code(8)

                    prediction = [
                        leagues,
                        kbt_funtions.remove(home_team + " vs " + away_team),
                        picks,
                        odds,
                        kbt_funtions.remove(timez),
                        score,
                        match_date,
                        flag,
                        results,
                        match_code,
                        source,
                    ]
                    dt.append(prediction)
                except IndexError as e:
                    print(f"Failed to process row {i}: {e}")

            # Write all predictions to the CSV
            thewriter.writerows(dt)

        print("Predictions saved to CSV:", dt)
    except Exception as e:
        print(f"Failed to write to the CSV file: {e}")
   


#csv_f = "venasbet_data.csv"
def connect_server():
    #NOTE::::::::::::when i experience bad connection: 10458 (28000) in ip i browse my ip address and paste it inside cpanel add host then copy my cpanel sharedhost ip
    #and paste here as my host ip address
    try:
        connection =  kbt_funtions.db_connection()
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()

            print("You're connected to database: ", record)

        
            
        with open(csv_f, "r") as f:
        
            csv_data = csv.reader(f)
            for row in csv_data:
                print(row)
                cursor.execute('INSERT INTO soccerpunt(league,fixtures,tip,odd,match_time,score,date,flag,result,code,source)'\
                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)

        print("Inserting tips now... ", time.ctime())
        print(cursor.rowcount," record(s) created==============", time.ctime())

        
        time.sleep(6) 
        print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
        print("============Bot deleting previous tips from  database:=============== ")


        cursor.execute('DELETE t1 FROM soccerpunt AS t1 INNER JOIN soccerpunt AS t2 WHERE t1.id < t2.id AND t1.fixtures = t2.fixtures AND t1.source = t2.source')

            
        print(cursor.rowcount," record(s) deleted==============", time.ctime()) 

    

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password ", err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("Error while connecting to MySQL", err)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.commit()
            connection.close()
                
            print("MySQL connection is closed")




def run():
    get_today_prediction(soup,p_date)
    #time.sleep(6) 
    #print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
    get_previous_prediction(soup,x_date)
    #print(get_result("2X","2:2"))
    # #insert into db
    connect_server()


if __name__ == "__main__":
    run()