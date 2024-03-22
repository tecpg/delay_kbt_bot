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
import kbt_load_env
from consts import global_consts as gc
import kbt_funtions


global csv_data
csv_f = gc.VENASBET_1_5_CSV


session = requests.Session()
my_headers = gc.MY_HEARDER
dt = []

# taking input as the current date
# today() method is supported by date
# class in datetime module

p_date = gc.PRESENT_DAY_DATE
# calculating end date by adding 4 days
x_date = gc.YESTERDAY_DATE

# # printing end date
# print("Ending date")
#print(x_date)



def get_today_over_1_5_prediction(bs, set_date):

    url ="https://www.r2bet.com/2_5_goals?dt="
   
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
            picks ="Over 1.5"



            results = "N/A"
            odds="N/A"
            source = "venasbet_o_1_5"
            flag = ""
            match_date = set_date
            match_code = kbt_funtions.get_code(8)
            score=""

            prediction = [leagues,kbt_funtions.remove(home_team +"vs "+away_team),  picks, odds, kbt_funtions.remove(timez), score, match_date, flag, results, match_code, source ]
            dt.append(prediction)
        

        thewriter.writerows(dt)

    print(dt)


def get_previous_over_1_5_prediction(nbs,set_previous_date):

    try:

        url ="https://www.r2bet.com/2_5_goals?dt="
    
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
                picks ="Over 1.5"
                score = dom.xpath(f'//*[@id="home"]/table/tbody/tr[{i}]/td[4]/strong')
                score = score[0].text

                results = kbt_funtions.get_result_by_score(picks, score)



                odds="N/A"
                source = "venasbet_o_1_5"
                flag = ""
                match_date = set_previous_date
                match_code = kbt_funtions.get_code(8)

                prediction = [leagues,kbt_funtions.remove(home_team +"vs "+away_team),  picks, odds, kbt_funtions.remove(timez), score, match_date, flag, results, match_code, source ]
                dt.append(prediction)
            

            thewriter.writerows(dt)

        print(dt)
    except:
        pass
        
    



#csv_f = "venasbet_over_1_5data.csv"
def connect_server():
    #NOTE::::::::::::when i experience bad connection: 10458 (28000) in ip i browse my ip address and paste it inside cpanel add host then copy my cpanel sharedhost ip
    #and paste here as my host ip address
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



    post_title = 'Daily Betting Tips - Todays Football Prediction'
    tip_category = '186'
    category_note = """ <h4>What is Over 1.5 goals Prediction</h4><br>
            Over 1.5 goals betting is a type of bet that involves predicting that there will be at least 2 goals scored in a football match. This type of bet is sometimes referred to as a "goal line" bet. Over 1.5 goals betting tips refer to recommendations or suggestions for over 1.5 goals bets made by experts or individuals with knowledge of the teams or events being bet on. It is important to note that betting tips and recommendations are not a guarantee of success and that all forms of gambling carry inherent risks and uncertainties. 
            It is always important to gamble responsibly and to understand the risks involved. """
    source_name = 'venasbet_o_1_5'
    more_tips_link = 'over-1-5-betting-tips'


    wp_post(post_title = post_title,
        tips_category = tip_category,
        category_note = category_note,
        source_name  = source_name,
        more_tips_link = more_tips_link)
    


def run():
    try:
        get_today_over_1_5_prediction(soup,p_date)
        #time.sleep(6) 
        #print("==============Bot is taking a nap... whopps!==================== ", time.ctime())  
        get_previous_over_1_5_prediction(soup,x_date)
        #print(get_result("2:2"))
        # #insert into db
        connect_server()
    except:
        pass


if __name__ == "__main__":
    run()
