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
csv_f = gc.FEATURED_TEJMATCH

session = requests.Session()
my_headers = gc.MY_HEARDER
dt = []

p_date = gc.PRESENT_DAY_DATE
# calculating end date by adding 4 days
x_date = gc.YESTERDAY_DATE



# Set up logging to capture errors
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')



import requests
from bs4 import BeautifulSoup as soup
from csv import writer
import logging
from consts import global_consts as gc

def post():
    url = "https://tejtips.com/en/upcoming-matches/"
    csv_f 
    fixtures = []

     # Step 1: Get today's date in "DD Mon" format
    today = datetime.today().strftime("%d %b")  # e.g., "25 Jun"


    try:
        webpage = requests.get(url, headers=gc.MY_HEARDER)
        webpage.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch the webpage: {e}")
        return

    try:
        bs = soup(webpage.content, "html.parser")
    except Exception as e:
        logging.error(f"Failed to parse the webpage content: {e}")
        return

    for match in bs.select(".next-match-fixtures"):
        try:
            team_tags = match.select(".match-teams-vs .team-logo")
            if len(team_tags) != 2:
                continue

            home_team = team_tags[0].select_one("strong").text.strip()
            home_flag = team_tags[0].select_one("img")["src"]

            away_team = team_tags[1].select_one("strong").text.strip()
            away_flag = team_tags[1].select_one("img")["src"]

            match_info_tag = match.select_one(".mvs p")
            league_name = match_info_tag.select_one("strong").text.strip()
            match_date = match_info_tag.get_text(strip=True).replace(league_name, "").strip()

# ✅ Step 2: Skip if match_date doesn't match today
            if today != match_date:
                continue

            tips_list = [li.get_text(strip=True) for li in match.select(".nmf-loc li")]
            match_tip = " ".join(tips_list)

            odd = ""

            match_time = ""  # not available on the source
            league_flag = ""  # not provided in HTML

            source = "tj_tips"

            prediction = [
                league_name,     # league_name
                home_team,       # home_team
                away_team,       # away_team
                match_tip,       # match_tip
                odd,             # odd
                match_time,      # match_time
                match_date,      # match_date
                home_flag,       # home_flag
                away_flag,       # away_flag
                league_flag,     # league_flag
                source           # source
            ]

            fixtures.append(prediction)

        except Exception as e:
            logging.warning(f"Error parsing match: {e}")
            continue

    # ✅ Write to CSV
    try:
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
            thewriter.writerow([
                "league_name", "home_team", "away_team", "match_tip", "odd",
                "match_time", "match_date", "home_flag", "away_flag", "league_flag", "source"
            ])
            for row in fixtures:
                thewriter.writerow(row)
    except Exception as e:
        logging.error(f"Error writing to CSV file: {e}")

    return fixtures


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
                # print(row)
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
    post()
   
    connect_server()


if __name__ == "__main__":
    run()





    