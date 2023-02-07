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


sql_date = date.today().strftime('%Y-%m-%d')
# sql_date = '28-10-2022'
print(sql_date)


# post_title = ''
# tip_category = 'Over 1.5 goals'
# category_note = """  """
# source_name = ''

# more_tips_link = ''

# wp_post_contents = {
#     'post_title' : post_title,
#     'tips_category' : tip_category,
#     'category_note' : category_note,
#     'source_name'  : source_name,
#     'more_tips_link' : more_tips_link

# }


welcome_note = """ Hello Kings!

We have just released a new set of football prediction tips for the upcoming matches. Our team of experts have analyzed the data and have come up with some highly accurate predictions.

Whether you are a casual fan or a serious bettor, these tips will help you make informed decisions about your bets. Be sure to check them out and let us know what you think.
<blockquote>
<small>As always, it is important to remember that these tips are not guaranteed and that there is always a risk of losing money when betting.</small> <strong>Please gamble responsibly.</strong></blockquote>

Thank you for your support and happy betting!<br> """

join_telegram_content = """ We have recently started a new Telegram group for sports fans to discuss and share their thoughts on the latest events and games.
If you are interested in joining, please click on the link below to request access. We look forward to having you as a member of our community.
See you in the group!<br> 
<div class="media single-contact-info">
<a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Join our Telegram Group<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>
        </div>  
"""

comment_note = """ <p>
We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
Your feedback is always valuable to us. Thank you!</p> """



#posting into wp
def wp_post(**post_dict):
   
    tip_category = post_dict["tips_category"]
    tip_note = post_dict["category_note"]
    source_name = post_dict["source_name"]
    more_tips_link = post_dict["more_tips_link"]
    post_title = post_dict["post_title"]
    
    
    # print(tip_category)
    # print(tip_note)


    try:
        connection = mysql.connector.connect(host='131.226.5.7',
                                            database='kingsbet_KBTdb',
                                            user='kingsbet_mycomp',
                                            password='mycomp007')

        # connection = mysql.connector.connect(host='localhost',
        #                                  database='kingsbet_KBTdb',
        #                                  user='root',
        #                                  password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            cursor.execute(f'SELECT league, fixtures, tip, date FROM soccerpunt WHERE source = "{source_name}" AND date = "{sql_date}" ORDER BY id DESC LIMIT 4')
            my_results = cursor.fetchall()
            html = ''

            for key, value in enumerate(my_results):

                html += f'<tr><td>{value[3]}</td><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td></tr>'
            
            print(html)
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
    
    '<div class="col-lg-10 col-md-6">'
                    '<div class="table-responsive single-intro-inner style-2 text-center">'
                        '<table class="table table-striped">'
                        f'<h4 class="title">{post_title}</h4>'
                                    '<thead>'
                                    '<tr>'
                                    
                                        '<th>Date/Time</th>'
                                        '<th>League</th>'
                                        '<th>Fixtures</th>'
                                        '<th>Tip</th>'

                                    '</tr>'
                                    '</thead>'
                                    f'<tbody>{html}'
                                        
                                    '</tbody>'
                                    '</table>'
                                    f'<a class="btn btn-base" href="{more_tips_link}">Load more...<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>'
                                            '</div>'
                                        '</div>'
                                        f'{join_telegram_content}'
                                        f'{tip_note}'
                                        f'{comment_note}',
                                     'date'   : f'{p_date}',
                                    'categories' : ['4', '185', f'{tip_category}'],
                                    'tags' : ['63', '7', '66', '125', '127','53', '54', '153', '4', '16','14', '15', '51', '6', '11','52', '56', '58', '59', '57']
    }

    r = requests.post(url, headers=header, json=post)
    print(r)