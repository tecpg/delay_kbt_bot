import requests
from bs4 import BeautifulSoup
from cmath import cos
from csv import DictReader, DictWriter, writer
import csv
import datetime
from lib2to3.pgen2 import driver
import pprint
from pydoc import stripid
import random
import string
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
csv_f = gc.BETNUM_CSV

session = requests.Session()
my_headers = gc.MY_HEARDER
dt = []

p_date = gc.PRESENT_DAY_DATE
# calculating end date by adding 4 days
x_date = gc.YESTERDAY_DATE


def get_today_prediction(set_date, csv_f):
    """
    Fetches predictions from the website and writes them to a CSV file.

    :param set_date: Date for the predictions
    :param csv_f: Path to the output CSV file
    """
    # Define the URL and headers
    url = "https://betinum.com/en/tips/privews-and-analysis/"

    try:
        # Fetch the webpage content
        response = requests.get(url, headers=my_headers)
        response.raise_for_status()

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all prediction containers
        predictions = soup.find_all('div', class_='mrbara-freetips')

        # Initialize a list to hold scraped data
        dt = []

        # Loop through each prediction block and extract information
        for prediction in predictions[:7]:
            # Match date and time
            date_col = prediction.find('div', class_='mrbara-freetips-date-col')
            date = date_col.find('div', class_='mrbara-d-block-md').get_text(strip=True)
            match_time = date_col.find('span').get_text(strip=True)

            # League and flag
            league_col = prediction.find('div', class_='mrbara-freetips-champ-col')
            league = league_col.get_text(strip=True)
            comp_logo = league_col.find('img')['src']

     # Teams and their flags
            teams_col = prediction.find('div', class_='mrbara-freetips-teams')
            home = teams_col.find_all('div')[0].get_text(strip=True)
            away = teams_col.find_all('div')[2].get_text(strip=True)
            try:
                home_logo = (
                    teams_col.find_all('img')[0].get('data-lazy-src')
                    or teams_col.find_all('img')[0].get('src', '')
                )
                away_logo = (
                    teams_col.find_all('img')[2].get('data-lazy-src')
                    or teams_col.find_all('img')[2].get('src', '')
                )
            except IndexError:
                print("Error: Missing image elements for flags.")
                home_flag, away_flag = '', ''


            # Prediction details
            prediction_col = prediction.find('div', class_='mrbara-freetips-end-col')
            tip = prediction_col.find('div', class_='betinum-tiny-box').get_text(strip=True)
            odd = prediction_col.find_all('div', class_='betinum-tiny-box')[1].get_text(strip=True)
            rate = prediction_col.find_all('div', class_='betinum-tiny-box')[2].get_text(strip=True)

             # Short reason (betinum-expandable class)
            expandable = prediction.find('div', class_='betinum-expandable')
            review  = expandable.get_text(strip=True) if expandable else "No reason provided."
            # String to be removed
            string_to_remove = "Short reason"

            # Removing the string
            review = review.replace(string_to_remove, "", 1)

            # Prepare other fields
            fixtures = f"{home} vs {away}"
            score = ''
            result = ''
            source = 'betnum'
            match_date = set_date
            match_code = kbt_funtions.get_code(8)

            # Append the prediction to the list
            dt.append([league,fixtures,tip,odd,score,result,match_time,match_date,comp_logo, home_logo, away_logo,rate,review, source, match_code])

        # Write predictions to the CSV file
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
            thewriter.writerows(dt)

        print(f"Data successfully written to {csv_f}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

        
def connect_server():
    #NOTE::::::::::::when i experience bad connection: 10458 (28000) in ip i browse my ip address and paste it inside cpanel add host then copy my cpanel sharedhost ip
    # and paste here as my host ip address
    try:
        connection = kbt_funtions.db_connection()

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

                cursor.execute('INSERT INTO betnum(league,fixtures,tip,odd,score,result,match_time,match_date,comp_logo, home_logo, away_logo,rate,review, source, code)'\
                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
            

        print("Inserting tips now... ", time.ctime())
        print(cursor.rowcount," record(s) created==============", time.ctime())

        
        time.sleep(6) 
        print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
        print("============Bot deleting previous tips from  database:=============== ")

        cursor.execute('DELETE t1 FROM betnum AS t1 INNER JOIN betnum AS t2 WHERE t1.id < t2.id AND t1.fixtures = t2.fixtures AND t1.source = t2.source')
    
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
    get_today_prediction(p_date, csv_f)
    connect_server()


if __name__ == "__main__":
    run()





