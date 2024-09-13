import csv
import requests
import configparser
from consts import global_consts as gc
import kbt_funtions
from cmath import cos
from csv import DictReader, writer
import csv

import datetime
from lib2to3.pgen2 import driver
import pprint
from pydoc import stripid

import traceback
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

import time
import mysql.connector
from mysql.connector import errorcode
from consts import global_consts as gc
import kbt_funtions
import csv

csv_f = gc.TELEGRAM_BOT_CSV

def connect_server():
    try:
        # Establishing database connection
        connection = kbt_funtions.db_connection()

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version:", db_Info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database:", record)

            # Define your SQL query
            query = """
            (SELECT *
            FROM soccerpunt
            WHERE source = 'venasbet_o_1_5' AND result = 'N/A'
            ORDER BY id DESC
            LIMIT 2)
            UNION ALL
            (SELECT *
            FROM soccerpunt
            WHERE source = 'venasbet_acca'  AND result = 'N/A'
            ORDER BY id DESC
            LIMIT 1)
            UNION ALL
            (SELECT *
            FROM soccerpunt
            WHERE source = 'tipsbet_combo_tips'  AND result = 'N/A'
            ORDER BY id DESC
            LIMIT 1);
            """

            # Execute the query
            cursor.execute(query)

            # Fetch all results from the executed query
            results = cursor.fetchall()

            # Get column headers from the cursor description
            headers = [i[0] for i in cursor.description]

            # Write results to CSV file
            with open(csv_f, "w", newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(headers)  # Write column headers
                csv_writer.writerows(results)  # Write data rows

            print("Query results written to CSV file:", csv_f)

            
    except mysql.connector.Error as err:
        # Handle MySQL errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password:", err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist:", err)
        else:
            print("Error while connecting to MySQL:", err)

    finally:
        # Ensure the connection is closed properly
        if connection and connection.is_connected():
            cursor.close()
            connection.commit()  # Commit changes if any
            connection.close()
            print("MySQL connection is closed")

# Call the function to test
if __name__ == "__main__":
    connect_server()


def post():

    
    tips = []

    # Read tips from CSV file
    with open(csv_f, "r") as f:
        csv_data = csv.reader(f)
        next(csv_data)  # Skip header row if it exists
        for row in csv_data:
            # Extract only the values for fixtures, league, odd, tip, match_time, and date
            tips.append([row[2], row[1], row[4], row[3], row[5], row[6]])

    # Select first 6 predictions
    predictions = tips[:6]

    # Extract the date from the first row and format it (assuming all rows have the same date)
    date_str = predictions[0][5]  # Extracting the date from the first prediction
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Convert string to datetime object
    formatted_date = date_obj.strftime("%d")  # Day with leading zero
    # Add the suffix (st, nd, rd, th) to the day
    if 4 <= int(formatted_date) <= 20 or 24 <= int(formatted_date) <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][int(formatted_date) % 10 - 1]

    formatted_date = f"{date_obj.strftime('%d')}{suffix} {date_obj.strftime('%B %Y')}"  # Format the date

    # Prepare tips in plain text format with the formatted date as the header
    post_tips = f"Date: {formatted_date}\n\n"  # Set the formatted date as the header

    for x in predictions:
        league = f"League: {x[1]}\n"  # League as the header
        fixture = f"Fixture: {x[0]}\n"  # Fixtures below the league
        odd = f"Odd: {x[2]}"  # Odd with a label
        tip = f"Tip: {x[3]}"  # Tip with a label
        match_time = f"Time: {x[4]}"  # Match time with a label

        # Combine all the parts and add to the post_tips string
        post_tips += f"{league}{fixture}{odd}, {tip}, {match_time}\n\n"

    print(post_tips)   # Print the formatted tips with league above fixtures

    # Text and links to post
    message_text = "Winning KBT free telegram tips for today! Do not miss the cash!"
    link_url = "Subscribe now to view all tips https://kingsbettingtips.com/vip-subscriptions/ or get the our app for free! https://kingsbettingtips.com/download-app/"
    link_url2 = "Last prediction results:- https://kingsbettingtips.com/hot-odd-betting-tips/"

    # Combine all text parts into a single message
    full_message = f"{message_text}\n\n{post_tips}\n{link_url}\n{link_url2}"

    # Construct the payload for sending the message
    payload = {
        "chat_id": gc.CHANNEL_CHAT_ID,
        "text": full_message
    }

    # Send the POST request to Telegram API to send the message
    response = requests.post(gc.TELEGRAM_BASE_URL + 'sendMessage', data=payload)

    # Check the response status
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

def run():
    connect_server()

    post()

if __name__ == "__main__":
    run()
