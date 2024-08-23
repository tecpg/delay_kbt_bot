from cmath import cos
from csv import DictReader, writer
import csv
import datetime
from lib2to3.pgen2 import driver
import pprint
from pydoc import stripid
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
import requests
from bs4 import BeautifulSoup as soup
from csv import writer
import logging


global csv_data
csv_f = gc.FEATURED_MATCH

session = requests.Session()
my_headers = gc.MY_HEARDER
dt = []

p_date = gc.PRESENT_DAY_DATE
# calculating end date by adding 4 days
x_date = gc.YESTERDAY_DATE



# Set up logging to capture errors
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def post(bs):
    url = "https://kingsolomonbet.com"
    dt = []
    csv_f = 'output.csv'

    try:
        webpage = requests.get(url, headers=gc.MY_HEARDER)
        webpage.raise_for_status()  # This will raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch the webpage: {e}")
        return  # Exit the function if we can't fetch the webpage
    
    try:
        bs = soup(webpage.content, "html.parser")
    except Exception as e:
        logging.error(f"Failed to parse the webpage content: {e}")
        return  # Exit the function if parsing fails

    match_list = []

    try:
        matches = bs.find_all('div', class_='single-match')
    except Exception as e:
        logging.error(f"Failed to find match elements on the page: {e}")
        return  # Exit the function if we can't find match elements
    
    try:
        # Open csv file
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)

            for match in matches:
                try:
                    match_title = match.find('h5', class_='match-title').text

                    team_names = match.find_all('span', class_='team-name')
                    team1_name = team_names[0].text if team_names else None
                    team2_name = team_names[1].text if len(team_names) > 1 else None

                    flag_links = match.find_all('div', class_='logo')

                    home_flag = flag_links[0].find('img')['src'] if flag_links else None
                    away_flag = flag_links[1].find('img')['src'] if len(flag_links) > 1 else None

                    match_time = match.find('span', class_='date').text if match.find('span', class_='date') else None
                    match_tip = match.find('span', class_='time').text if match.find('span', class_='time') else None

                    league_name = match_title
                    home_team = team1_name
                    away_team = team2_name
                    odd = ''
                    match_date = ''
                    league_flag = ''
                    results = ''
                    source = 'ksb_tips'

                    try:
                        if 'O 1.5' in match_tip:
                            match_tip = 'Over 1.5 goals'
                        elif match_tip.find("1X") != -1:
                            match_tip = f'{home_team} to win or draw'
                        elif match_tip.find("1") != -1:
                            match_tip = f'{home_team} to win'
                        elif match_tip.find("2X") != -1:
                            match_tip = f'{away_team} to win or draw'
                        elif match_tip.find("2") != -1:
                            match_tip = f'{away_team} to win'
                        else:
                            match_tip = match_tip
                    except Exception as e:
                        logging.error(f"Error processing match tip: {e}")

                    prediction = [league_name, home_team, away_team, match_tip, odd, match_time, match_date, home_flag, away_flag, league_flag, source]
                    dt.append(prediction)

                except Exception as e:
                    logging.error(f"Error processing match data: {e}")

            thewriter.writerows(dt)
    except Exception as e:
        logging.error(f"Error writing to CSV file: {e}")

    print(dt)


#csv_f = "venasbet_data.csv"

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
                cursor.execute('INSERT INTO featured_tips(league, home, away, tip, odd, time, date,home_flag_link, away_flag_link, league_flag_link, source)'\
                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
            

        print("Inserting tips now... ", time.ctime())
        print(cursor.rowcount," record(s) created==============", time.ctime())

        
        time.sleep(6) 
        print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
        print("============Bot deleting previous tips from  database:=============== ")


        cursor.execute('DELETE t1 FROM featured_tips AS t1 INNER JOIN featured_tips AS t2 WHERE t1.id < t2.id AND t1.home = t2.home AND t1.away = t2.away AND t1.source = t2.source')

            
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
    post(soup)
   
    connect_server()


if __name__ == "__main__":
    run()