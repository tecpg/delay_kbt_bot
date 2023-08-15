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
from featured_match_wp_post import featured_match_wp_post
import kdb_config
import time as _time

_runtime = 1


session = requests.Session()
my_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
#my_headers = GET_UA
dt = []

p_date = date.today()
# calculating end date by adding 4 days
x_date = p_date - timedelta(days=1)

live_url = 'https://kingsbettingtips.com/wp-json/wp/v2/posts'

url = live_url

live_user = 'adminKBT'

user = live_user

live_pwd = kdb_config.live_pwd

password = live_pwd

creds = user + ':' + password

p_time = datetime.now() + timedelta(minutes=5)
p_date = p_time.strftime("%Y-%m-%dT%H:%M:%S")

def post():
    url = "https://kingsolomonbet.com"

    webpage = requests.get(url, headers = my_headers)
    bs = soup(webpage.content, "html.parser")

    match_list = []

    matches = bs.find_all('div', class_='single-match')

    for match in matches:
        match_title = match.find('h5', class_='match-title').text

        team_names = match.find_all('span', class_='team-name')
        team1_name = team_names[0].text
        team2_name = team_names[1].text

        match_time = match.find('span', class_='date').text
        match_tip = match.find('span', class_='time').text

        league_name =  match_title
        home_team = team1_name
        away_team = team2_name
        match_time = match_time
        try:
            if 'O 1.5' in match_tip:
                match_tip = 'Over 1.5 goals'

            elif match_tip.find("1") != -1:
                    match_tip = f'{home_team} to win'
            elif match_tip.find("1X") != -1:
                    match_tip = f'{home_team} to win or draw'
            elif match_tip.find("2") != -1:
                    match_tip = f'{away_team} to win'
            elif match_tip.find("2X") != -1:
                    match_tip = f'{away_team} to win or draw'
            
            else: match_tip = match_tip
                
                
        except:
            pass     
        
        prediction = match_tip
        match = {"league":league_name,"home_team":home_team, "away_team":away_team, "prediction":prediction,"match_time": match_time}
        dt.append(match)
        print(match_tip)


    welcome_note = """  """

    join_telegram_content = """ We have recently started a new Telegram group for sports fans to discuss and share their thoughts on the latest events and games.
    If you are interested in joining, please click on the link below to request access. We look forward to having you as a member of our community.
    See you in the group!<br> 
    <a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Our Telegram<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>
            
    """

    comment_note = """ <p>
    We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
    Your feedback is always valuable to us. Thank you!</p> """


    for match in dt:
        print(match["league"])

        post_title = f"{match['home_team']} vs {match['away_team']} Match: Predictions, Livescore, and Preview"
        tip_category = '208'
        category_note = """ 
        
        <h4>Unlock Winning Strategies with Our Premium Football Betting Tips!</h4>

    Are you ready to elevate your football betting game? Look no further! We are thrilled to introduce our premium football betting tips that can take your wagering experience to the next level.

    At Kingsbettingtips, we've gathered a team of seasoned experts who live and breathe football. Our analysts meticulously analyze matches, teams, player performances, and historical data to provide you with the most accurate and well-informed predictions.

    Why subscribe to our premium football betting tips?

    1. Expert Insights: Our team of experts has a deep understanding of the game, which enables us to identify valuable betting opportunities that others might miss.

    2. Proven Track Record: Our past predictions speak for themselves. We have a strong history of successful forecasts that have helped our subscribers make informed betting decisions.

    3. Comprehensive Coverage: From major leagues to international tournaments, we cover a wide range of football events, ensuring you never miss out on potential winning bets.

    4. Time-Saving: Don't spend hours researching matches and statistics. We do the hard work for you, providing you with concise and actionable tips that save you time and effort.

    5. Exclusive Benefits: Subscribers also get access to exclusive content, real-time updates, and special offers that will enhance your betting experience.

    Don't leave your bets to chance. Let our expertise guide you towards better betting decisions. Subscribe today and experience the thrill of winning with Kingsbettingtips.

    Remember, responsible gambling is key. Only bet what you can afford to lose. Our tips are meant to enhance your experience, not replace responsible betting practices.
    <a class="btn btn-base" href="https://kingsbettingtips.com/vip-subscriptions/">Subscribe now<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>
        """
        
        featured_post_content = f"""

    <h4>Featured Match: {match['home_team']} vs. {match['away_team']}</h4>

    <h5>Match Details</h5>
    League: {match['league']}
    Date: {match['match_time']}


    <h5>Match Overview</h5>
    The highly anticipated match between {match['home_team']} and {match['away_team']} is just around the corner. Fans are eagerly awaiting this thrilling showdown in the {match['league']} League.

    <h5>Match Prediction</h5>
    Considering the current form and strengths of both teams, this match promises to be a close battle. Our prediction for this encounter is <b>{match['prediction']}</b>.

    Remember to gamble responsibly and make informed decisions when placing bets.


            """

        featured_match_wp_post(post_title = post_title,
                tips_category = tip_category,
                category_note = category_note,
                telegram_content = join_telegram_content,
                post_content = featured_post_content,
            )
    _time.sleep(_runtime)
    
def run():
    post()


if __name__ == "__main__":
    run()