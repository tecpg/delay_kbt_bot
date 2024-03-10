from cmath import cos
from csv import DictReader, writer
import csv
from lib2to3.pgen2 import driver
import random
import string
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
from datetime import date
from lxml import etree
from consts import global_consts as gc
import kbt_funtions

def post_tips():
    url ="https://oddslot.com/tips/?page="
    dt = []
    for page in range(1,4):
    

        # # Here Chrome  will be used
        webpage = requests.get(url + str(page), headers = gc.MY_HEARDER)
        spider = soup(webpage.content, "html.parser")
        dom = etree.HTML(str(spider))

        with open(gc.JACKPOT_CSV, "w", encoding="utf8", newline="") as f:
            thewriter = writer(f)
           
            for x in range(0,10):

                c = 1 + x
                i = str(c)
            
                league = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[4]/strong')
                leagues = league[0].text
                timez = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[1]/strong')
                timez = timez[0].text
                picks = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[7]/strong')
                picks = picks[0].text
                home_teams = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[2]/div/div/a/h4/strong')
                home_teams = home_teams[0].text
                away_teams = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[3]/div/div/a/h4/strong')
                away_teams = away_teams[0].text
                odds = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[6]/a/strong')
                odds = float(odds[0].text)
                rates = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[5]/strong')
                rates = rates[0].text
                score = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[8]/a')
                score = score[0].text

                try:

                    results = dom.xpath(f'/html/body/div[2]/div[4]/div/div/div/div/div[2]/div/table/tbody/tr[{i}]/td[8]/a/font')
                    results = results[0].text
                    if results.find("WON") != -1:
                        continue

                    elif results.find("LOST") != -1:
                         continue
                    
                    elif results.find("IN PLAY") != -1:
                         continue
                    
                    else: results = "Not Yet"
                
                
                except:
                    pass     
        
                match =""
                source = "single_jackpot"
                flag = ""
                match_date = gc.PRESENT_DAY_DMY
                match_code = kbt_funtions.get_code(8)

                prediction = [leagues, home_teams +' vs '+ away_teams, picks, odds, timez, score, match_date, flag, results, match_code, source ]
                dt.append(prediction)
            

            my_list = dt
            max_value = float('-inf')
            max_sublist = None

            for sublist in my_list:
                if sublist[3] > max_value:
                    max_value = sublist[3]
                    max_sublist = sublist

            print("The sublist with the highest value at index[3] is:", max_sublist)
            max_sublist[3] = round(max_sublist[3] + 0.08, 2)
        
            match_list = [str(value) for value in max_sublist]
            

            thewriter.writerow(match_list)

            print(match_list)


def post_to_mysql():
    # #insert into db

    # csv_f = "oddslot_data.csv"
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

                
        with open(gc.JACKPOT_CSV, "r") as f:
        
            csv_data = csv.reader(f)
            for row in csv_data:
                print(row)
                cursor.execute('INSERT INTO soccerpunt(league,fixtures,tip,odd,match_time,score,date,flag,result,code,source)'\
                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)

        print("Inserting tips now... ", time.ctime())
        print(cursor.rowcount," record(s) created==============", time.ctime())

        
        time.sleep(3) 
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


def run():
    post_tips()
    post_to_mysql()


if __name__ == "__main__":
    run()
