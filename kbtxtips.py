import datetime
import requests
import json
import base64
from cmath import cos
from csv import DictReader, writer
import csv
from lib2to3.pgen2 import driver
import random
import string
import requests
import time
import io
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from datetime import timedelta
from datetime import date
import kbt_load_env
from consts import global_consts as gc
import kbt_funtions


sql_date = gc.PRESENT_DAY_YMD
sql_date2 = gc.PRESENT_DAY_DMY


post_title = '1x2 Betting Tips For Today - Daily Free Betting Tips'
previous_post_title = '1x2 Betting Tips Results - Daily Free Betting Tips'
tip_category = 'Over 1.5 goals'
category_note = """  """
source_name = ''

tips_link = 'category/1x2-betting-tips-for-today/'
previous_tips_link = 'https://kingsbettingtips.com/category/1x2-betting-tips-for-today/'


def connect_server():
  csv_f = "1x2bet-code.csv"
  try:
      connection =  kbt_funtions.db_connection()

      if connection.is_connected():
          db_Info = connection.get_server_info()
          print("Connected to MySQL Server version ", db_Info)
          cursor = connection.cursor()
          cursor.execute("select database();")
          record = cursor.fetchone()
          print("You're connected to database: ", record)
        
    
          print("Getting today predictions", record)
          cursor.execute(f"""SELECT * FROM (
                              (SELECT league, fixtures, tip, date, code, source FROM soccerpunt WHERE source = "protips_acca" AND date = "{sql_date}" ORDER BY RAND() LIMIT 1)
                              UNION
                              (SELECT league, fixtures, tip, date, code, source FROM soccerpunt WHERE source = "venasbet_o_1_5" AND date = "{sql_date}" ORDER BY RAND() LIMIT 2)
                              UNION
                              (SELECT league, fixtures, tip, date, code, source FROM soccerpunt WHERE source = "vip_tips" AND date = "{sql_date2}" ORDER BY RAND() LIMIT 2))
                              AS results ORDER BY RAND() """)

          my_results = cursor.fetchall()
          today_html = ''
          codes = []
          
          for key, value in enumerate(my_results):

              today_html += f'<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td></tr>'

              #open csv file
              with open(csv_f, "w", encoding="utf8", newline="") as f:
                  thewriter = writer(f)
                  league = value[0]
                  fixtures = value[1]
                  match_tip = value[2]
                  
                  match_date = value[3]
                  code = [league, fixtures, match_tip, match_date]
                  codes.append(code)
                  print(code)

                  thewriter.writerows(codes)
          
          print(today_html)
          print("here are the fixtures: " + fixtures)
        
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


  post = {
  'title'    : f'{post_title}',
  'status'   : 'publish', 
  'content'  : f'{gc.WP_WELCOME_NOTE}'      
        '<div class="card text-center ">'
    '<div class="card-header" style="background-color:#010832">'
      '<ul class="nav nav-pills card-header-pills">'
      '<li class="nav-item">'
        f'<a class="nav-link disabled" href="#">Date: {value[3]}</a>'
        '</li>'
        '<li class="nav-item">'
          f'<a class="nav-link" href="{previous_tips_link}">Previous Tips</a>'
      ' </li>'
      
      '</ul>'
  ' </div>'
    '<div class="card-body">'
      f'<h5 class="card-title">{post_title}</h5>'
      # '<p class="card-text">With supporting text below as a natural lead-in to additional content.</p>'
  '<div class="col-lg-10 col-md-6">'
                      '<div class="table-responsive single-intro-inner style-2 text-center">'
                          '<table class="table table-striped">'
    '<thead>'
      '<tr>'
      '<th>League</th>'
      '<th>Fixtures</th>'
      '<th>Tip</th>'
      '</tr>'
    '</thead>'
    f'<tbody>{today_html}'
    '</tbody>'
  '</table>'
  '</div>'
  '</div>'
  f'{gc.WP_JOIN_TELEGRAM_NOTE}'
      '<a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Join our Telegram Group<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>'
  ' </div>'
  '</div><br>'
  f'{gc.WP_COMMENT_NOTE}',
                                      'date'   : f'{gc.PRESENT_DAY_DATE}',
                                  'categories' : ['192'],
                                  'tags' : ['63', '7', '66', '125', '127','53', '54', '153', '4', '16','14', '15', '51', '6', '11','52', '56', '58', '59', '57']
  }

  r = requests.post(gc.WP_LIVE_URL, headers=gc.WP_HEADER, json=post)
  print(r)

def run():
    connect_server()


if __name__ == "__main__":
    run()
