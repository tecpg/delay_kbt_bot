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
csv_f = gc.BET99_DRAWS_CSV

session = requests.Session()
my_headers = gc.MY_HEARDER
dt = []

p_date = gc.PRESENT_DAY_DATE
# calculating end date by adding 4 days
x_date = gc.YESTERDAY_DATE


def get_today_prediction(set_date):
   
    # Define the URL
    url = "https://99predict.com/draws?dt="

    try:
        # Fetch the webpage content
        response = requests.get(url + str(set_date), headers=my_headers)
        response.raise_for_status()

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all div elements with the class "tips-box"
        tips_boxes = soup.find_all("div", {"class": "tips-box"})

        # Open CSV file
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            # Create a DictWriter object
            thewriter = writer(f)

            # Extract the relevant text from each tips-box
            for box in tips_boxes:
                # Extract league name
                league = box.find("div", {"class": "league-box"}).get_text(strip=True)

                # Extract match time
                time = box.find("div", {"class": "time-box"}).get_text(strip=True)

                # Extract teams
                teams = box.find_all("div", {"class": "match-box"})
                home_team = teams[0].get_text(strip=True)
                away_team = teams[2].get_text(strip=True)
                fixture = f"{home_team} vs {away_team}"

                
                # Extract tips
                tips = box.find("span", {"class": "tips"}).get_text(strip=True).replace("Tips:", "").strip()


                # Other data
                odds= kbt_funtions.get_random_odd_draws()
                score = ''
                result = 'N/A'
                flag = ""
                source = 'bet99_draws'
                match_date = set_date
                match_code = kbt_funtions.get_code(8)

                prediction = [league,fixture, tips, odds,time, score, match_date, flag, result, match_code, source ]
                dt.append(prediction)

            # Write the row to CSV
            thewriter.writerows(dt)
               

        print(f"Data successfully written to {csv_f}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
def get_previous_prediction(set_date):
    # Define the URL
    url = "https://99predict.com/draws?dt="

    try:
        # Fetch the webpage content
        response = requests.get(url + str(set_date), headers=my_headers)
        response.raise_for_status()

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all div elements with the class "tips-box"
        tips_boxes = soup.find_all("div", {"class": "tips-box"})

        # Open CSV file
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            # Create a DictWriter object
            thewriter = writer(f)

            # Extract the relevant text from each tips-box
            for box in tips_boxes:
                # Extract league name
                league = box.find("div", {"class": "league-box"}).get_text(strip=True)

                # Extract match time
                time = box.find("div", {"class": "time-box"}).get_text(strip=True)

                # Extract teams
                teams = box.find_all("div", {"class": "match-box"})
                home_team = teams[0].get_text(strip=True)
                away_team = teams[2].get_text(strip=True)
                fixture = f"{home_team} vs {away_team}"

                # Extract tips
                tips = box.find("span", {"class": "tips"}).get_text(strip=True).replace("Tips:", "").strip()

                # Other data
                odds= kbt_funtions.get_random_odd()
                scores = box.find_all("span", {"class": "score"})
                home_score = scores[0].get_text(strip=True)
                away_score = scores[1].get_text(strip=True)
                
                score = f"{home_score}:{away_score}"
                # Determine match result
                if box.find("span", {"class": "fa fa-check-circle text-success"}):
                    result = "Won"
                elif box.find("span", {"class": "fa fa-times-circle"}):
                    result = "Lost"
                else:
                    result = "N/A"
                source = 'bet99_draws'
                flag = ''
                match_date = set_date
                match_code = kbt_funtions.get_code(8)

                prediction = [league,fixture, tips, odds,time, score, match_date, flag, result, match_code, source ]
                dt.append(prediction)
                
                # Write the row to CSV
            thewriter.writerows(dt)

        print(f"Data successfully written to {csv_f}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



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
    get_today_prediction(p_date)
    get_previous_prediction(x_date)
    connect_server()


if __name__ == "__main__":
    run()





