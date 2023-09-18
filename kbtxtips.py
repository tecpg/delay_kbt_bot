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
import kdb_config


local_url = 'http://localhost:8080/wordpress/wp-json/wp/v2/posts/?post_type=predictions'
live_url = 'https://kingsbettingtips.com/wp-json/wp/v2/posts'

url = live_url

live_user = 'adminKBT'
local_user = 'root'

user = live_user

live_pwd = 'auoN LBS4 pdzK 8nG7 A4je 78vY'
local_pwd = 'WZvU hI89 7oxZ FtVj T7XQ OSW4'

password = live_pwd

creds = user + ':' + password

p_time = datetime.now() + timedelta(minutes=5)
p_date = p_time.strftime("%Y-%m-%dT%H:%M:%S")
yesterday_date = date.today()
# calculating end date by adding 4 days
x_date = yesterday_date - timedelta(days=1)


sql_date = date.today().strftime('%Y-%m-%d')
sql_date2 = date.today().strftime('%d-%m-%Y')
# sql_date = '2022-10-28'
print(sql_date)


post_title = '1x2 Betting Tips For Today - Daily Free Betting Tips'
previous_post_title = '1x2 Betting Tips Results - Daily Free Betting Tips'
tip_category = 'Over 1.5 goals'
category_note = """  """
source_name = ''

tips_link = 'category/1x2-betting-tips-for-today/'
previous_tips_link = 'https://kingsbettingtips.com/category/1x2-betting-tips-for-today/'


welcome_note = """ <blockquote>
<small>As always, it is important to remember that these tips are not guaranteed and that there is always a risk of losing money when betting.</small> <strong>Please gamble responsibly.</strong></blockquote>
<br> """

join_telegram_content = """<p class="card-text"> We have recently started a new Telegram group for sports fans to discuss and share their thoughts on the latest events and games.
If you are interested in joining, please click on the link below to request access. We look forward to having you as a member of our community.
See you in the group!<br> 
"""

comment_note = """ <p>
We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
Your feedback is always valuable to us. Thank you!</p> """




def connect_server():
  csv_f = "1x2bet-code.csv"
  try:
      connection = mysql.connector.connect(host=kdb_config.db_host,
                                          database=kdb_config.db_dbname,
                                          user=kdb_config.db_user,
                                          password=kdb_config.db_pwd)

      # connection = mysql.connector.connect(host='localhost',
      #                                     database='kingsbet_KBTdb',
      #                                     user='root',
      #                                     password='')
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


  token = base64.b64encode(creds.encode())
  header = {'Authorization': 'Basic ' + token.decode('utf-8')}

  token = base64.b64encode(creds.encode())
  header = {'Authorization': 'Basic ' + token.decode('utf-8')}

  # media = {
  #     'file' : open('imager.png', 'rb'),
  #     'caption' : 'First api image',
  #     'description' : 'image api'
  # }

  # image = requests.post(url + '/media', headers=header, files= media )
  # imageURL = str(json.loads(image.content['source_url']))


  post = {
  'title'    : f'{post_title}',
  'status'   : 'publish', 
  'content'  : f'{welcome_note}'      
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
  f'{join_telegram_content}'
      '<a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Join our Telegram Group<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>'
  ' </div>'
  '</div><br>'
  f'{comment_note}',
                                      'date'   : f'{p_date}',
                                  'categories' : ['192'],
                                  'tags' : ['63', '7', '66', '125', '127','53', '54', '153', '4', '16','14', '15', '51', '6', '11','52', '56', '58', '59', '57']
  }

  r = requests.post(url, headers=header, json=post)
  print(r)

def run():
    connect_server()


if __name__ == "__main__":
    run()
