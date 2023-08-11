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

live_pwd = kdb_config.live_pwd
local_pwd = kdb_config.local_pwd

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




comment_note = """ <p>
We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
Your feedback is always valuable to us. Thank you!</p> """



#posting into wp
def featured_match_wp_post(**post_dict):
   
    tip_category = post_dict["tips_category"]
    tip_note = post_dict["category_note"]
    telegram_content = post_dict["telegram_content"]
    content = post_dict["post_content"]
    post_title = post_dict["post_title"]
    

    token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}

    token = base64.b64encode(creds.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}

    post = {
    'title'    : f'{post_title}',
    'status'   : 'publish', 
    'content'  : f'{content}'
    
   
                                       
                                        f'{tip_note}'
                                        f'{telegram_content}'
                                        f'{comment_note}',
                                     'date'   : f'{p_date}',
                                    'categories' : ['4', '185', f'{tip_category}'],
                                    'tags' : ['63', '7', '66', '125', '127','53', '54', '153', '4', '16','14', '15', '51', '6', '11','52', '56', '58', '59', '57']
    }

    r = requests.post(url, headers=header, json=post)
    print(r)