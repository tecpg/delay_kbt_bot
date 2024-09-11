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
csv_f = gc.HIGHODDS_CSV

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

# Define headers for the request (ensure this is correctly set in your environment)
MY_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

import requests
from bs4 import BeautifulSoup as soup
import logging
from csv import writer

# Set your headers and CSV file name here
MY_HEADER = {"User-Agent": "Mozilla/5.0"}
csv_f = "today_predictions.csv"

def get_today_prediction(set_date):
    url = "https://typersi.com/"
 

    try:
        # Fetch the webpage content
        webpage = requests.get(url, headers=MY_HEADER)
        webpage.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch the webpage: {e}")
        return  # Exit the function if we can't fetch the webpage

    try:
        # Parse the webpage content with BeautifulSoup
        bs = soup(webpage.content, "html.parser")
    except Exception as e:
        logging.error(f"Failed to parse the webpage content: {e}")
        return  # Exit the function if parsing fails

    try:
        # Find all div elements with class 'tableBox'
        tables = bs.find_all("div", {"class": "tableBox"})
        limited_tables = tables[:4]  # Limit to first four divs containing tables

        # Check if any tables were found
        if not limited_tables:
            print("No 'tableBox' divs found.")
            return

        # Loop through the first four 'tableBox' divs
        for index, table_box in enumerate(limited_tables):
            print(f"\nExtracting data from table {index + 1}:")

            # Find the table within the div
            table = table_box.find('table')

            # Check if a table is found inside the current div
            if not table:
                print("No table found within this tableBox.")
                continue

            # Find all rows in the table
            rows = table.find_all('tr')

            # Loop through each row and extract specific columns
            for row_index, row in enumerate(rows[1:]):
                # Find all cells in the current row (both <td> and <th>)
                cells = row.find_all(['td', 'th'])

                # Check if the row contains the expected number of cells (at least 7)
                if len(cells) >= 7:
                    # Extract the specific columns by index
                    time = cells[1].get_text(strip=True)
                    fixtures = cells[2].get_text(strip=True)
                    tip = cells[3].get_text(strip=True)
                    odd_text = cells[4].get_text(strip=True)
                    bookmaker = cells[6].get_text(strip=True)

                    try:
                        odd = float(odd_text)  # Convert odds to a float
                    except ValueError:
                        continue  # Skip if odds can't be converted to float

                    # Check if odds are within the desired range and if bookmaker is 'Soccer'
                    if 1.5 <= odd <= 1.60 and bookmaker in ['Soccer', 'Handball', 'Tennis']:
                        score = ''
                        result = ''
                        source = 'typersi'
                        match_date = set_date

                        # Print the extracted data
                        print(f"{time}  {fixtures} | {tip}  {odd} {bookmaker}")

                        # Append the data to the list
                        prediction = [time, bookmaker, fixtures, tip, odd, score, result, source, match_date]
                        dt.append(prediction)
    except Exception as e:
        logging.error(f"Failed to find match elements on the page: {e}")
        return  # Exit the function if we can't find match elements

    try:
        # Write the extracted data to a CSV file
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
            thewriter.writerows(dt)
    except Exception as e:
        logging.error(f"Error writing to CSV file: {e}")

    # Print the collected data
    print(dt)

def get_yesterday_prediction(set_date):
    url = "https://typersi.com/wczoraj,yesterday.html"
  

    try:
        # Fetch the webpage content
        webpage = requests.get(url, headers=MY_HEADER)
        webpage.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch the webpage: {e}")
        return  # Exit the function if we can't fetch the webpage

    try:
        # Parse the webpage content with BeautifulSoup
        bs = soup(webpage.content, "html.parser")
    except Exception as e:
        logging.error(f"Failed to parse the webpage content: {e}")
        return  # Exit the function if parsing fails

    try:
        # Find all div elements with class 'tableBox'
        tables = bs.find_all("div", {"class": "tableBox"})
        limited_tables = tables[:4]  # Limit to first three divs containing tables

        # Check if any tables were found
        if not limited_tables:
            print("No 'tableBox' divs found.")
            return

        # Loop through the first three 'tableBox' divs
        for index, table_box in enumerate(limited_tables):
            print(f"\nExtracting data from table {index + 1}:")

            # Find the table within the div
            table = table_box.find('table')

            # Check if a table is found inside the current div
            if not table:
                print("No table found within this tableBox.")
                continue

            # Find all rows in the table
            rows = table.find_all('tr')

            # Loop through each row and extract specific columns
            for row_index, row in enumerate(rows[1:]):
                # Find all cells in the current row (both <td> and <th>)
                cells = row.find_all(['td', 'th'])

                # Check if the row contains the expected number of cells (at least 6)
                if len(cells) >= 6:
                    # Extract the specific columns by index
                    time = cells[1].get_text(strip=True)
                    fixtures = cells[2].get_text(strip=True)
                    tip = cells[3].get_text(strip=True)
                    odd_text = cells[5].get_text(strip=True)

                    try:
                        odd = float(odd_text)  # Convert odds to a float
                    except ValueError:
                        continue  # Skip if odds can't be converted to float

                    # Check if odds are within the desired range
                    if 1.5 <= odd <= 1.60:
                        score = cells[7].get_text(strip=True)
                        result_class = cells[7].get('class', [])  # Adjust the index based on where the score is located
                        check_result = ' '.join(result_class)  # Convert the class list to a string

                        # Check the class for result status
                        if '_tloss' in check_result:
                            result = 'Lost'
                        elif '_twin' in check_result:
                            result = 'Won'
                        else:
                            result = ''  # Handle any other cases

                        source = 'typersi'
                        match_date = set_date
                        bookmaker = ''

                        # Print the extracted data
                        print(f" {time}  {fixtures} | {tip}  {odd}")

                        # Append the data to the list
                        prediction = [time, bookmaker, fixtures, tip, odd, score, result, source, match_date]
                        dt.append(prediction)
    except Exception as e:
        logging.error(f"Failed to find match elements on the page: {e}")
        return  # Exit the function if we can't find match elements

    try:
        # Write the extracted data to a CSV file
        with open(csv_f, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
            thewriter.writerows(dt)
    except Exception as e:
        logging.error(f"Error writing to CSV file: {e}")

    # Print the collected data
    print(dt)




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
                cursor.execute('INSERT INTO highodds(time, sports, fixtures, tip, odd, score, result, source, match_date)'\
                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
            

        print("Inserting tips now... ", time.ctime())
        print(cursor.rowcount," record(s) created==============", time.ctime())

        
        time.sleep(6) 
        print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
        print("============Bot deleting previous tips from  database:=============== ")


        cursor.execute('DELETE t1 FROM highodds AS t1 INNER JOIN highodds AS t2 WHERE t1.id < t2.id AND t1.fixtures = t2.fixtures AND t1.tip = t2.tip')

            
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
    get_yesterday_prediction(x_date)
   
    connect_server()


if __name__ == "__main__":
    run()