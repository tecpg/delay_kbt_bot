import random
import kbt_load_env
from datetime import datetime
from datetime import timedelta
from datetime import date
import base64
# all kbt CONSTANT variables indicated with capital snake case

#Wordpress constants
WP_LOCAL_URL = 'http://localhost:8080/wordpress/wp-json/wp/v2/posts/?post_type=predictions'
WP_LIVE_URL = 'https://kingsbettingtips.com/wp-json/wp/v2/posts'
WP_POST_TIME = datetime.now() + timedelta(minutes=5)
WP_POST_DATE = WP_POST_TIME.strftime("%Y-%m-%dT%H:%M:%S")
WP_LOCAL_USER = 'root'
WP_LIVE_USER = 'adminKBT'
WP_LOCAL_PASSWORD = kbt_load_env.local_pwd
WP_LIVE_PASSWORD = kbt_load_env.live_pwd
WP_CREDITIALS = WP_LIVE_USER + ':' + WP_LIVE_PASSWORD
WP_TOKEN = base64.b64encode(WP_CREDITIALS.encode())
WP_HEADER = {'Authorization': 'Basic ' + WP_TOKEN.decode('utf-8')}


WP_WELCOME_NOTE = """ Hello Kings!

We have just released a new set of football prediction tips for the upcoming matches. Our team of experts have analyzed the data and have come up with some highly accurate predictions.

Whether you are a casual fan or a serious bettor, these tips will help you make informed decisions about your bets. Be sure to check them out and let us know what you think.
<blockquote>
<small>As always, it is important to remember that these tips are not guaranteed and that there is always a risk of losing money when betting.</small> <strong>Please gamble responsibly.</strong></blockquote>

Thank you for your support and happy betting!<br> """

WP_JOIN_TELEGRAM_NOTE = """ We have recently started a new Telegram group for sports fans to discuss and share their thoughts on the latest events and games.
If you are interested in joining, please click on the link below to request access. We look forward to having you as a member of our community.
See you in the group!<br> 
<div class="media single-contact-info">
<a class="btn btn-base" href="https://t.me/+EQVAXh9ctNgwZDJk">Join our Telegram Group<i class="fas fa-arrow-alt-circle-right ms-2"></i></a>
        </div>  
"""

WP_COMMENT_NOTE = """ <p>
We would love to hear your thoughts and opinions on it. Please feel free to leave a comment below and let us know what you think. 
Your feedback is always valuable to us. Thank you!</p> """




#Time constants
MYSQL_DATE = date.today().strftime('%Y-%m-%d')

PRESENT_DAY_DATE = date.today()
YESTERDAY_DATE = PRESENT_DAY_DATE - timedelta(days = 1)
YESTERDAY_DMY = YESTERDAY_DATE.strftime('%d-%m-%Y')
PRESENT_DAY_DMY = date.today().strftime('%d-%m-%Y')
PRESENT_DAY_YMD = date.today().strftime('%Y-%m-%d')



#header constants
# Define a list of header dictionaries for different browsers
headers_list = [
    
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/91.0.864.59", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/92.0.902.55", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/93.0.961.38", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"},
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.818.62 Safari/537.36 Edg/90.0.818.62"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:88.0) Gecko/20100101 Firefox/88.0"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"},
    { "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0" },
    {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1" },
    {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"},
    {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
]
# Additional headers
additional_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com",
    "Connection": "keep-alive"
}
# Select a random header from the list
headers = random.choice(headers_list)
MY_HEARDER = headers.update(additional_headers)
 



#cvs file names
JACKPOT_CSV = 'csv_files/jackpot_data.csv'
TELEGRAM_BOT_CSV = "csv_files/1x2bet-code.csv"
BLOG_POST_TIPS_CSV= "csv_files/1x2bet-code.csv"
ODDSLOT_CSV = "csv_files/oddslot_data.csv"
PROTIPS_CSV = "csv_files_protips.csv"
HIGHODDS_CSV = "csv_files/highodds.csv"
BET99_CSV = "csv_files/bet99.csv"
BET99_BETDAY_CSV = "csv_files/bet99_betday.csv"
BET99_DRAWS_CSV = "csv_files/bet99_draws.csv"
BET99_OVERGOALS_CSV = "csv_files/bet99_overgoals.csv"
BETNUM_CSV = "csv_files/betnum.csv"
SAFE_BET_CSV = "csv_files/safe_bet.csv"
SAFE_BET_BTTS_CSV = "csv_files/safe_btts.csv"
SAFE_BET_DC_CSV = "csv_files/safe_dc.csv"
SAFE_BET_OVERGOALS_CSV = "csv_files/safe_bet_overgoals.csv"
TIPSBET_CSV = "csv_files/tipsbet_data.csv"
VENASBET_2_5_CSV = "csv_files/venasbet_o_2_5_data.csv"
VENASBET_1_5_CSV = "csv_files/venasbet_over_1_5data.csv"
VENASBET_ACCA_CSV = "csv_files/venasbet_acca_data.csv"
VENASBET_BTTS_CSV = "csv_files/venasbet_btts_data.csv"
VENASBET_DNB_CSV = "csv_files/venasbet_dnb_data.csv"
VENASBET_3_5_CSV = "csv_files/venasbet_u_3_5_data.csv"
VENASBET_O_3_5_CSV = "csv_files/venasbet_o_3_5_data.csv"
VENASBET_WAH_CSV = "csv_files/venasbet_wah.csv"
VENASBET_HANDICAP_CSV = "csv_files/venasbet_handicap.csv"
VIP_CSV = "csv_files/vip_tips_data.csv"
FEATURED_MATCH = "csv_files/featured_match.csv"





#telegram const
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6151016586:AAHnkIqKqBO01v1fQfd8noSOCzKLHjrWyGw'

# Replace 'CHANNEL_CHAT_ID' with the actual chat ID of your channel
CHANNEL_CHAT_ID = '-1001701327610'

# URL for the Telegram Bot API
# BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
# URL for the Telegram Bot API
# URL for the Telegram Bot API
TELEGRAM_BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"