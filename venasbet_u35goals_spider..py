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


global csv_data
csv_f = "venasbet_u_3_5_data.csv"


def GET_UA():
    uastrings = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',\
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',\
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25',\
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',\
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8',\
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',\
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',\
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10',\
                'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',\
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',\
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36'\
                ]

    return random.choice(uastrings)


def get_code(length):
    letters = string.ascii_lowercase
    r_letters = ''.join(random.choice(letters) for i in range(length))
    numbers =   str(random.randint(2220,333000333))
    code = r_letters+numbers
    return code

# Python code to remove whitespace
def remove(string):
    return string.replace("\n", "")

def get_result(score):
     if score != ":":
        if any(map(str.isdigit, score)) :
        #calculate over 2.5 score
            s_list = list(score.split(":"))
            try:
             s_n = [eval(i)for i in s_list]
            except NameError:
                results = "..."
            else:    
                s_n = sum(s_n)
                if s_n <= 3:
                    results = "Won"
                else:
                    results = "Lost"
                return results
     else:
         results = "..."
         return results
    






session = requests.Session()
my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
#my_headers = GET_UA
dt = []

# taking input as the current date
# today() method is supported by date
# class in datetime module

p_date = date.today()
# calculating end date by adding 4 days
x_date = p_date - timedelta(days=1)

# # printing end date
# print("Ending date")
print(x_date)
#print(get_result("1:1"))

def get_today_under_3_5_prediction(bs, set_date):

    url ="https://r2bet.com/draws?dt="
   
    webpage = requests.get(url+str(set_date), headers = my_headers)
    bs = bs(webpage.content, "html.parser")
    dom = etree.HTML(str(bs))

    #get table row count for the tr loop

    tables = bs.findChildren('table')
    web_table = tables[0]
    rows = web_table.findChildren(['tr'])
    tr_count = len(rows)
    print("Table has ",tr_count - 1," rows")

    #open csv file

   
    with open(csv_f, "w", encoding="utf8", newline="") as f:
        thewriter = writer(f)

        for x in range(0,tr_count - 1):

            c = 1 + x
            i = str(c)
            
            timez = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[1]')
            timez = timez[0].text
            league = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[2]')
            leagues = league[0].text
            home_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[3]/text()[1]')
            home_team = home_team[0]
            away_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[3]/text()[2]')
            away_team = away_team[0]
            # picks = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[4]')
            # picks = picks[0].text
            picks="Under 3.5"



            results = "N/A"
            odds="N/A"
            source = "venasbet_u_3_5"
            flag = ""
            match_date = set_date
            match_code = get_code(8)
            score=""

            prediction = [leagues,remove(home_team +"vs "+away_team),  picks, odds, remove(timez), score, match_date, flag, results, match_code, source ]
            dt.append(prediction)
        

        thewriter.writerows(dt)

    print(dt)


def get_previous_under_3_5_prediction(nbs,set_previous_date):

    url ="https://r2bet.com/draws?dt="
   
    webpage = requests.get(url+str(set_previous_date), headers = my_headers)
    nbs = nbs(webpage.content, "html.parser")
    dom = etree.HTML(str(nbs))

    #get table row count for the tr loop

    tables = nbs.findChildren('table')
    web_table = tables[0]
    rows = web_table.findChildren(['tr'])
    tr_count = len(rows)
    print("Table has ",tr_count - 1," rows")

    #open csv file

  
    with open(csv_f, "w", encoding="utf8", newline="") as f:
        thewriter = writer(f)

        for x in range(0,tr_count - 1):

            c = 1 + x
            i = str(c)
            
            timez ="N/A"
            league = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[1]')
         
            leagues = league[0].text
            home_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[2]/text()[1]')
            home_team = home_team[0]
            away_team = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[2]/text()[2]')
            away_team = away_team[0]
            # picks = dom.xpath(f' //*[@id="home"]/table/tbody/tr[{i}]/td[3]')
            # picks = picks[0].text
            picks="Under 3.5"
            score = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[4]/strong')
            score = score[0].text
            print(score)

            results = get_result(score)

            odds="N/A"
            source = "venasbet_u_3_5"
            flag = ""
            match_date = set_previous_date
            match_code = get_code(8)

            prediction = [leagues,remove(home_team +"vs "+away_team),  picks, odds, remove(timez), score, match_date, flag, results, match_code, source ]
            dt.append(prediction)
        

        thewriter.writerows(dt)

    print(dt)
        
    

get_today_under_3_5_prediction(soup,p_date)
#time.sleep(6) 
#print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
get_previous_under_3_5_prediction(soup,x_date)
#print(get_result("2X","2:2"))
# #insert into db

#csv_f = "venasbet_o_2_5_data.csv"
#NOTE::::::::::::when i experience bad connection: 10458 (28000) in ip i browse my ip address and paste it inside cpanel add host then copy my cpanel sharedhost ip
#and paste here as my host ip address
try:
    connection = mysql.connector.connect(host=kdb_config.db_host,
                                         database=kdb_config.db_dbname,
                                         user=kdb_config.db_user,
                                         password=kdb_config.db_pwd)
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



post_title = 'Under 3.5 Goals Betting Tips - Today Free Under 3.5 Goals Predictions'
tip_category = '188'
category_note = """ <h4>What is Under 3.5 goals Prediction</h4><br>
              Under 3.5 goals betting is a type of bet that involves predicting that there will be 3 goals or fewer scored in a football match. This type of bet is sometimes referred to as a "goal line" bet. Under 3.5 goals betting tips refer to recommendations or suggestions for under 3.5 goals bets made by experts or individuals with knowledge of the teams or events being bet on. It is important to note that betting tips and recommendations are not a guarantee of success and that all forms of gambling carry inherent risks and uncertainties. 
              It is always important to gamble responsibly and to understand the risks involved. """
source_name = 'venasbet_u_3_5'
more_tips_link = 'under-3-5-betting-tips'


wp_post(post_title = post_title,
    tips_category = tip_category,
    category_note = category_note,
    source_name  = source_name,
    more_tips_link = more_tips_link)