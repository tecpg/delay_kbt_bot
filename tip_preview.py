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
from cmath import cos
from csv import DictReader, writer
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
import kdb_config


session = requests.Session()
my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
#my_headers = GET_UA
dt = []

p_date = date.today()
# calculating end date by adding 4 days
x_date = p_date - timedelta(days=1)


url = "https://betinum.com/en/tips"

webpage = requests.get(url, headers = my_headers)
bs = soup(webpage.content, "html.parser")


text_list = []

divs = bs.find_all('div', class_='mrbara-freetips bt-fs-14px mrbara-mb-1p5em mrbara-p-10px mrbara-radius-10px mrbara-bgr-white mrbara-mb-1p5em mrbara-border-sliver betinum-expandable-container')

for div in divs:
    children = div.find_all('div')
    text_list = [child.get_text(strip=True) for child in children]
    # Use the 'text' variable as per your requirement
 
    print('Date ' + text_list[3])
    print('League '+text_list[5])
    print('Home '+text_list[8])
    print('Away '+text_list[10])
    print('Prediction '+text_list[13])
    print('Odd '+text_list[14])
    print('other tip '+text_list[15])
    print('Preview '+text_list[18])
    print('------------------------------')
    # for text in text_list[0]:
    #  print(text)

   



# local_url = 'http://localhost:8080/wordpress/wp-json/wp/v2/posts/?post_type=predictions'
# live_url = 'https://kingsbettingtips.com/wp-json/wp/v2/posts'

# url = live_url

# live_user = 'adminKBT'
# local_user = 'root'

# user = live_user

# live_pwd = kdb_config.live_pwd
# local_pwd = kdb_config.local_pwd

# password = live_pwd

# creds = user + ':' + password

# p_time = datetime.now() + timedelta(minutes=5)
# p_date = p_time.strftime("%Y-%m-%dT%H:%M:%S")


# sql_date = date.today().strftime('%Y-%m-%d')
# # sql_date = '28-10-2022'
# print(sql_date)



# welcome_note = """  """

# join_telegram_content = """ We have recently started a new Telegram group for sports fans to discuss and share their thoughts on the latest events and games.
# If you are interested in joining, please click on the link below to request access. We look forward to having you as a member of our community.
# See you in the group!<br> 
# <div class="media single-contact-info">
# <a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Join our Telegram Group<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>
#         </div>  
# """

# comment_note = """ <p>
# We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
# Your feedback is always valuable to us. Thank you!</p> """



# #posting into wp
# def wp_post(**post_dict):
   
#     tip_category = post_dict["tips_category"]
#     tip_note = post_dict["category_note"]
#     source_name = post_dict["source_name"]
#     more_tips_link = post_dict["more_tips_link"]
#     post_title = post_dict["post_title"]
    
    
#     # print(tip_category)
#     # print(tip_note)


 
#     token = base64.b64encode(creds.encode())
#     header = {'Authorization': 'Basic ' + token.decode('utf-8')}

#     token = base64.b64encode(creds.encode())
#     header = {'Authorization': 'Basic ' + token.decode('utf-8')}

#     # media = {
#     #     'file' : open('imager.png', 'rb'),
#     #     'caption' : 'First api image',
#     #     'description' : 'image api'
#     # }

#     # image = requests.post(url + '/media', headers=header, files= media )
#     # imageURL = str(json.loads(image.content['source_url']))


#     post = {
#     'title'    : f'{post_title}',
#     'status'   : 'publish', 
#     'content'  : f'{welcome_note}'
    
#     '<div class="col-lg-10 col-md-6">'
#                     '<div class="table-responsive single-intro-inner style-2 text-center">'
                      
#                                     f'<a class="btn btn-base" href="{more_tips_link}">Load more...<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>'
#                                             '</div>'
#                                         '</div>'
#                                         f'{join_telegram_content}'
#                                         f'{tip_note}'
#                                         f'{comment_note}',
#                                      'date'   : f'{p_date}',
#                                     'categories' : ['4', '185', f'{tip_category}'],
#                                     'tags' : ['63', '7', '66', '125', '127','53', '54', '153', '4', '16','14', '15', '51', '6', '11','52', '56', '58', '59', '57']
#     }

#     r = requests.post(url, headers=header, json=post)
#     print(r)